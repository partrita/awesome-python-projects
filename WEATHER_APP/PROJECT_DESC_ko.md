# Weather App (날씨 정보 조회 앱)

이 프로젝트는 파이썬의 `tkinter` 라이브러리와 OpenWeatherMap API를 사용하여 특정 도시의 실시간 날씨 정보를 조회하는 GUI 애플리케이션입니다.

## 주요 특징
- **실시간 날씨 검색**: 사용자가 입력한 도시 이름을 기반으로 전 세계 어디든 실시간 날씨 데이터를 가져옵니다.
- **다양한 정보 제공**: 기온(Kelvin), 기압(hPa), 습도(%), 그리고 일반적인 기상 상태 설명을 화면에 표시합니다.
- **사용자 친화적인 GUI**: 간단한 입력 창과 버튼으로 구성되어 있으며, 'Submit' 버튼으로 조회하고 'Clear' 버튼으로 내용을 초기화할 수 있습니다.
- **예외 처리**: 존재하지 않는 도시 이름을 입력할 경우 에러 메시지 상자를 통해 사용자에게 알립니다.

## 코드 설명

### 1. API 호출 및 데이터 처리
`requests` 라이브러리를 사용하여 OpenWeatherMap API에 HTTP GET 요청을 보내고 JSON 형식의 응답을 파싱합니다.
```python
def tell_weather():
    api_key = "YOUR_API_KEY"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_field.get()
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    # ... 데이터 추출 및 출력 ...
```

### 2. GUI 구성 (Tkinter)
레이블(Label), 입력창(Entry), 버튼(Button) 등을 Grid 레이아웃 시스템을 사용하여 배치합니다.
```python
root = Tk()
root.title("Weather Application")
# ... 레이블 및 입력창 생성 ...
city_field = Entry(root)
button1 = Button(root, text="Submit", command=tell_weather)
```

## 참고 자료
- [OpenWeatherMap API Documentation](https://openweathermap.org/api)
- [Tkinter Reference (Python Docs)](https://docs.python.org/3/library/tkinter.html)
- [Requests Library Documentation](https://docs.python-requests.org/en/latest/)
