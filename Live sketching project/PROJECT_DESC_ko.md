# Live sketching project (실시간 스케치 변환 프로젝트)

이 프로젝트는 웹캠 피드를 실시간으로 분석하여 연필로 그린 듯한 스케치 효과를 적용하는  OpenCV 기반의 파이썬 애플리케이션입니다.

## 주요 특징
- **실시간 비디오 처리**: 웹캠에서 실시간으로 프레임을 캡처하여 처리합니다.
- **이미지 세분화 및 효과 적용**: 그레이스케일 변환, 가우시안 블러, 캐니 엣지 검출(Canny Edge Detection) 및 임계값 처리(Thresholding)를 통해 스케치 효과를 구현합니다.
- **상호작용성**: 웹캠이 켜진 상태에서 실시간으로 변화를 확인할 수 있으며, 엔터(Enter) 키를 눌러 종료할 수 있습니다.

## 코드 설명
스케치 효과를 만드는 핵심 함수와 실행 과정은 다음과 같습니다.

### 1. 스케치 생성 함수
입력받은 이미지를 필터링하여 스케치 이미지로 변환합니다.
```python
def sketch(image):
    # 이미지를 흑백으로 변환
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 가우시안 블러로 노이즈 제거
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # 에지 추출 (Canny Edge Detection)
    canny_edges = cv2.Canny(img_gray_blur, 20, 50)
    
    # 이진화 처리로 결과 반전
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask
```

### 2. 웹캠 제어 및 루프
웹캠을 활성화하고 매 프레임마다 스케치 기능을 적용합니다.
```python
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # 변환된 스케치 이미지를 보여줌
    cv2.imshow('Our Live Sketcher', sketch(frame))
    # 엔터 키(13)가 눌리면 루프 종료
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
```

## 참고 자료
- [OpenCV-Python Edge Detection](https://docs.opencv.org/master/da/d22/tutorial_py_canny.html)
- [How to use Webcam with OpenCV Python](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html)
