# ROCK_PAPER_SCISSOR (가위바위보 게임)

이 프로젝트는 파이썬의 `random` 모듈을 사용하여 사용자와 컴퓨터 간의 가위바위보 대결을 구현한 콘솔 기반 게임입니다.

## 주요 특징
- **사용자 맞춤형**: 플레이어의 이름을 입력받아 게임 결과에 반영합니다.
- **무작위 AI**: 컴퓨터는 `randint` 함수를 사용하여 바위(0), 보(1), 가위(2) 중 하나를 무작위로 선택합니다.
- **입력 유효성 검사**: 사용자가 잘못된 값을 입력했을 때 경고 메시지를 보여주고 다시 입력받도록 설계되었습니다.
- **반복 실행**: 사용자가 종료(0 입력)를 원할 때까지 게임이 계속 진행됩니다.

## 코드 설명

### 1. 무작위 선택 루프
컴퓨터의 선택을 생성하고 사용자의 유효한 입력을 기다립니다.
```python
from random import randint

# 컴퓨터의 무작위 선택 (0: 바위, 1: 보, 2: 가위)
y = randint(0, 2)

# 유효한 입력을 위한 내부 루프
inputs = ["rock", "paper", "scissor"]
while True:
    x = input("SELECT YOUR CHOICE rock paper scissor: ").lower()
    if x in inputs:
        break
    print("That's not a valid play. Check your spelling!")
```

### 2. 승패 판정 로직
각 선택에 따른 경우의 수를 `if-elif` 문으로 상세히 구분하여 승자를 결정합니다.
```python
if x == "rock" and y == 0:
    print("computer move is rock\nResult: TIE")
elif x == "rock" and y == 1:
    print("computer move is paper\nResult: CPU WON")
# ... (생략)
```

## 참고 자료
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [How to make a Rock Paper Scissors Game in Python](https://www.thepythoncode.com/article/make-a-rock-paper-scissors-game-python)
