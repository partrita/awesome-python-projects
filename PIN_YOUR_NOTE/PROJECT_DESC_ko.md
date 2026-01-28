# PIN_YOUR_NOTE (핀 유어 노트)

이 프로젝트는 파이썬의 `tkinter` 라이브러리를 사용하여 개발된 간단한 메모 애플리케이션입니다. 사용자가 입력한 메모를 화면 상의 새 창에 현재 시간과 함께 표시해 줍니다.

## 주요 특징
- **간단한 입력 인터페이스**: 콘솔(CLI)을 통해 사용자의 노트를 입력받습니다.
- **GUI 메모 표시**: 입력된 메모를 별도의 GUI 창(`tkinter`)에 띄워줍니다.
- **시간 기록**: 메모를 작성하여 게시한 시점의 시간을 자동으로 기록하여 시각화합니다.

## 코드 설명

### 1. CLI 및 GUI 통합 실행
콘솔에서 입력을 받고 이를 GUI 창의 라벨로 전달합니다.
```python
def cli():
    import time
    # 현재 시간 포맷팅
    current_time = time.strftime("%H:%M")
    
    # 사용자 입력 받기
    note_input = input("Type your notes here: ")
    
    # GUI 창 구성
    root = tk.Tk()
    root.title("Pin Your Note")
    
    # 시간과 메모를 라벨로 추가
    tk.Label(root, text=current_time).pack()
    tk.Label(root, text=note_input).pack()
    
    root.mainloop()
```

## 참고 자료
- [Tkinter get started guide](https://tkdocs.com/tutorial/firstapp.html)
- [Python time module](https://docs.python.org/3/library/time.html)
