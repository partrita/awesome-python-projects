# Alarm Clock (알람 시계)

이 프로젝트는 `tkinter`를 사용하여 GUI 기반의 알람 시계를 구현한 것입니다. 사용자가 원하는 시간을 설정하면 해당 시간에 `pygame`을 사용하여 알람 소리를 재생합니다.

## 주요 기능
- `tkinter`를 사용하여 시간(시/분/AM/PM)을 선택할 수 있는 드롭다운 메뉴를 제공합니다.
- `pygame.mixer`를 사용하여 알람 소리(`MyAlarm.wav`)를 재생하고 제어합니다.
- `datetime` 라이브러리를 사용하여 현재 시간을 실시간으로 확인합니다.
- 알람 설정, 취소, 및 소리 중지 기능을 완벽하게 지원합니다.

## 코드 설명

### 1. 초기화 및 사운드 설정
`pygame`의 오디오 믹서를 초기화하고 재생할 알람 파일을 로드합니다.

```python
import pygame
from datetime import datetime
import tkinter as tk

# 오디오 믹서 초기화 및 알람 소리 로드
pygame.mixer.init(42050, -16, 2, 2048)
alarm_sound = pygame.mixer.Sound("MyAlarm.wav")
```

### 2. GUI 구성
`OptionMenu`를 사용하여 사용자가 시, 분, AM/PM을 선택할 수 있는 인터페이스를 만듭니다.

```python
class AlarmApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Alarm Clock")
        
        # 시/분/AM/PM 변수 초기화
        self.hr = tk.IntVar(self)
        self.min = tk.IntVar(self)
        self.ampm = tk.StringVar(self)
        
        # 드롭다운 메뉴 배치
        self.popmenuhours = tk.OptionMenu(self, self.hr, *range(1, 13))
        self.popmenuminutes = tk.OptionMenu(self, self.min, *["%02d" % i for i in range(60)])
        self.popmenuAMPM = tk.OptionMenu(self, self.ampm, "AM", "PM")
        
        self.popmenuhours.pack(side="left")
        self.popmenuminutes.pack(side="left")
        self.popmenuAMPM.pack(side="left")
        
        # 버튼들
        self.alarmbutton = tk.Button(self, text="Set Alarm", command=self.start_clock)
        self.alarmbutton.pack()
```

### 3. 알람 로직
`after` 메서드를 사용하여 1초마다 현재 시간을 확인하고, 설정된 시간과 일치하는지 체크합니다.

```python
    def Alarm(self, myhour, myminute):
        if not done:
            now = datetime.now()
            current_hour = now.strftime("%H")
            current_minute = now.strftime("%M")
            
            if current_hour == myhour and current_minute == myminute:
                # 알람 소리 무한 반복 재생
                pygame.mixer.Sound.play(alarm_sound, loops=-1)
                print("Alarm is ringing!")
            else:
                # 1초 후에 다시 확인
                self.after(1000, self.start_clock)
```

## 사용 방법
1. 드롭다운 메뉴에서 원하는 알람 시간을 선택합니다.
2. 'Set Alarm' 버튼을 클릭하여 알람을 설정합니다.
3. 알람이 울리면 'Stop Alarm' 버튼을 눌러 소리를 끕니다.

## 참고 자료
- [Pygame Mixer Documentation](https://www.pygame.org/docs/ref/mixer.html)
- [Tkinter OptionMenu](https://tkdocs.com/tutorial/menus.html)
