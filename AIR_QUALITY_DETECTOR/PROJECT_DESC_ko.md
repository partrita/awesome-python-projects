# Air Quality Detector (대기 질 탐지기)

이 프로젝트는 지정된 우편번호의 실시간 대기 질 지수(AQI)를 가져와서 간단한 GUI 창에 표시하는 응용 프로그램입니다.

## 주요 기능
- `requests` 라이브러리를 사용하여 AirNow API에서 대기 질 데이터를 가져옵니다.
- `tkinter`를 사용하여 사용자 인터페이스를 생성합니다.
- 도시 이름, AQI 지수 및 대기 질 범주를 화면에 표시합니다.

## 코드 설명

먼저 필요한 라이브러리를 가져오고 Tkinter 루트 창을 설정합니다.

```python
from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title("Air quality detector")
root.geometry("400x100") # 원본은 800x40이나 가독성을 위해 조정 가능
root.configure(background='green')
```

그 다음, API 요청을 보내고 JSON 데이터를 파싱합니다.

```python
try:
    # AirNow API 호출
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=10&API_KEY=1415D85E-FB89-40EF-B8F0-63F99A595BC8")
    api = json.loads(api_request.content)
    
    # 필요한 정보 추출
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."
```

마지막으로 레이블을 생성하여 정보를 표시하고 GUI 루프를 시작합니다.

```python
myLabel = Label(root, text=city + " Air Quality: " + str(quality) + " " + category, font=("Helvetica", 14), background="green")
myLabel.pack(pady=20)

root.mainloop()
```

## 참고 자료
- [AirNow API Documentation](https://www.airnowapi.org/)
- [Tkinter Tutorial](https://docs.python.org/3/library/tkinter.html)
