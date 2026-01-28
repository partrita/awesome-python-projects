# MyAlarm (알람 시계 프로젝트)

이 프로젝트는 파이썬의 `tkinter` 라이브러리를 사용하여 구현한 간단한 GUI 알람 시계 애플리케이션입니다.

## 주요 특징
- **GUI 인터페이스**: `tkinter`를 사용하여 시간(시, 분)을 입력할 수 있는 사용자 인터페이스를 제공합니다.
- **실시간 시간 모니터링**: `datetime` 모듈을 사용하여 현재 시간을 초 단위로 확인하고 설정된 알람 시간과 비교합니다.
- **사운드 알람**: 설정된 시간에 도달하면 파일 시스템을 통해 지정된 음악 파일(예: `HeyYa.mp3`)을 실행합니다.

## 코드 설명

### 1. 알람 기능 로직
설정된 시간과 현재 시간을 비교하여 일치하면 음악을 실행합니다.
```python
def alarm(set_alarm):
    while True:
        time.sleep(1) # 1초마다 확인
        current_time = datetime.datetime.now().time()
        current_time = str(current_time)[:5] # HH:MM 형식으로 변환
        if current_time == set_alarm:
            print("Time to wake up")
            os.system("start HeyYa.mp3") # 음악 파일 실행
            break
```

### 2. GUI 구성
사용자로부터 알람 시간을 입력받기 위한 화면을 구성합니다.
```python
hour = StringVar()
minute = StringVar()

# 시간 및 분 입력 칸 생성
Entry(root, textvariable=hour, width=5).place(x=10, y=30)
Entry(root, textvariable=minute, width=5).place(x=50, y=30)

# 알람 설정 버튼
Button(root, text="Set alarm", command=actual_time).place(x=10, y=70)
```

## 참고 자료
- [Tkinter - Python interface to Tcl/Tk](https://docs.python.org/3/library/tkinter.html)
- [Python datetime — Basic date and time types](https://docs.python.org/3/library/datetime.html)
