# Hangman Game (행맨 게임)

이 프로젝트는 파이썬의 `random` 모듈을 사용하여 구현한 고전적인 단어 맞추기 게임인 '행맨(Hangman)'입니다. 컴퓨터가 영화 제목 목록 중 하나를 무작위로 선택하면, 사용자는 알파벳을 하나씩 입력하여 단어를 완성해야 합니다.

## 주요 기능
- **무작위 단어 선택**: 여러 영화 제목이 포함된 리스트에서 `random.choice()`를 통해 단어를 선택합니다.
- **게임 로직**: 사용자가 입력한 알파벳이 단어에 포함되어 있는지 확인하고, 일치하는 위치에 표시합니다.
- **기회 제한**: 총 10번의 기회가 주어지며, 틀릴 때마다 기회가 차감됩니다.
- **반복 플레이**: 게임이 끝난 후 다시 플레이할지 여부를 선택할 수 있습니다.

## 코드 설명

### 1. 단어 선택 및 초기 설정
게임에 사용될 단어 리스트를 정의하고, 그중 하나를 무작위로 골라 대문자로 변환합니다.

```python
import random

words = [
    "Forrest Gump", "The Godfather", "The Green Mile", "Goodfellas",
    "Scarface", "The Terminal", "Million Dollar Baby", "Chinatown"
]

word = random.choice(words).upper()
guesses = ""
turns = 10
```

### 2. 단어 출력 및 사용자 입력 검증
단어를 돌면서 사용자가 맞춘 글자는 표시하고, 아직 맞추지 못한 글자는 밑줄(`_`)로 표시합니다.

```python
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        elif char == " ":
            print(' / ', end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\n축하합니다! 이겼습니다. :)")
        break

    guess = input("\n알파벳을 입력하세요: ").upper()
    guesses += guess

    if guess not in word:
        turns -= 1
        print("\n틀렸습니다! 남은 기회: ", turns)
```

## 참고 자료
- [Python random module documentation](https://docs.python.org/3/library/random.html)
- [Python while loops](https://www.w3schools.com/python/python_while_loops.asp)
