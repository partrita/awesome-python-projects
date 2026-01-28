# LICENSE_PLATE_DETECTION (자동차 번호판 검출 및 인식)

이 프로젝트는 OpenCV와 Pytesseract 라이브러리를 사용하여 이미지 파일에서 자동차 번호판을 검출하고, 번호판에 적힌 텍스트를 인식하여 출력하는 예제입니다.

## 주요 특징
- **이미지 전처리**: `cv2.cvtColor`, `cv2.bilateralFilter`, `cv2.Canny` 등을 사용하여 노이즈를 제거하고 외곽선을 강조합니다.
- **윤곽선 검출**: `cv2.findContours`를 통해 이미지 내의 다양한 윤곽선을 찾고, 번호판 특유의 사각형 모양을 식별합니다.
- **OCR 인식**: 오픈소스 OCR 엔진인 Tesseract를 연동하여 검출된 번호판 영역에서 텍스트를 추출합니다.

## 코드 설명

### 1. 이미지 읽기 및 전처리
사용자로부터 이미지를 선택받아 흑백 전환 및 필터링을 거쳐 외곽선을 추출합니다.
```python
import cv2
import imutils

image = cv2.imread(file)
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17) # 노이즈 제거
edged = cv2.Canny(gray, 170, 200) # 외곽선 검출
```

### 2. 번호판 영역 식별
검출된 윤곽선 중 면적이 큰 상위 30개를 분석하여 4개의 꼭짓점을 가진 사각형 영역을 찾습니다.
```python
contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

for c in contours:
    perimeter = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * perimeter, True)
    if len(approx) == 4: # 사각형 모양인 경우 번호판으로 간주
        Number_Plate_Contour = approx
        break
```

### 3. OCR을 이용한 텍스트 추출
추출된 번호판 영역을 이진화 처리한 후 Tesseract를 통해 문자를 인식합니다.
```python
import pytesseract

# Tesseract 실행 경로 설정 (Windows 환경 예시)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(processed_img)
print("Detected Number is:", text)
```

## 참고 자료
- [OpenCV-Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)
- [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)
