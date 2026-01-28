# ROLLING_DICE (주사위 굴리기 게임)

이 프로젝트는 무작위 숫자를 생성하여 주사위를 굴리는 과정을 시뮬레이션하는 간단한 파이썬 프로그램입니다.

## 주요 특징
- **무작위성**: `random.randint(1, 6)` 함수를 사용하여 실제 주사위와 동일하게 1에서 6 사이의 숫자를 임의로 생성합니다.
- **반복성**: 주사위를 한 번 굴린 후, 사용자의 선택에 따라 계속해서 다시 굴릴 수 있도록 루프 구조를 갖추고 있습니다.
- **재귀적 입력 확인**: 사용자가 빈 값을 입력하거나 잘못된 경로를 입력했을 때, `roll_dice` 함수를 재귀적으로 호출하여 올바른 입력을 유도합니다.

## 코드 설명

### 1. 주사위 굴리기 루프
주사위 값을 출력하고 사용자의 게임 지속 여부를 확인합니다.
```python
import random

# 게임 시작
dice_value = random.randint(1, 6)
print('You got ', dice_value)

# 반복 실행 로직
while True:
    choice = input("Do you want to play again? (Yes/No): ")
    if choice.lower() == 'no':
        break
    elif choice.lower() == 'yes':
        print('You got ', random.randint(1, 6))
    else:
        print('Wrong Input !!!')
```

## 참고 자료
- [Python Random Module - randint()](https://www.w3schools.com/python/ref_random_randint.asp)
- [Python While Loops](https://www.w3schools.com/python/python_while_loops.asp)
