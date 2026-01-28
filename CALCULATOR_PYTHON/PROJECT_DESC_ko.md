# Simple Calculator (간단한 계산기)

이 프로젝트는 `tkinter`를 사용하여 사칙연산뿐만 아니라 삼각함수, 로그, 지수 연산 등이 가능한 공학용 계산기를 구현한 것입니다.

## 주요 기능
- **기본 연산**: 덧셈, 뺄셈, 곱셈, 나눗셈, 나머지 연산(%)
- **고급 연산**: 로그(log10, ln), 삼각함수(sin, cos, tan), 제곱근(Sqrt), 팩토리얼(x!), 역수(1/x), 거듭제곱(^)
- **상수**: 원주율(pi), 자연상수(e)
- **기타**: Degrees 변환, 괄호 사용 가능, 초기화(C), 한 글자 삭제(DEL)

## 코드 설명

### 1. GUI 설정 및 입력창
`tkinter`를 사용하여 검은색 배경에 흰색 글씨의 입력창을 생성합니다.

```python
from tkinter import *
import math as m

root = Tk()
root.title("Simple Calculator")

# 결과창 설정
e = Entry(root, width=50, borderwidth=5, relief=RIDGE, fg="White", bg="Black")
e.grid(row=0, column=0, columnspan=5, padx=10, pady=15)
```

### 2. 과학적 계산 기능을 담당하는 함수
`math` 라이브러리를 사용하여 복잡한 계산을 수행합니다. `bind`를 통해 버튼 클릭 이벤트를 처리합니다.

```python
def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''
    
    if text == 'sin':
        result = str(m.sin(float(no)))
    elif text == 'cos':
        result = str(m.cos(float(no)))
    # ... (기타 함수들)
    
    e.delete(0, END)
    e.insert(0, result)
```

### 3. 수식 계산 함수
입력창 전역의 수식을 `eval()` 함수를 사용하여 한꺼번에 계산합니다.

```python
def evaluate():
    ans = e.get()
    try:
        ans = eval(ans)
        e.delete(0, END)
        e.insert(0, ans)
    except:
        e.delete(0, END)
        e.insert(0, "Error")
```

## 사용 방법
- 숫 버튼과 연산자 버튼을 눌러 수식을 완성합니다.
- `=` 버튼을 누르면 전체 수식이 계산됩니다.
- `sin`, `log` 등의 과학적 함수는 숫자를 먼저 입력한 후 해당 버튼을 누르면 즉시 계산됩니다.

## 참고 자료
- [Math Module in Python](https://docs.python.org/3/library/math.html)
- [Tkinter Grid Geometry Manager](https://tkdocs.com/tutorial/grid.html)
