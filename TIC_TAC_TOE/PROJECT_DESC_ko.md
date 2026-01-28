# Tic Tac Toe (틱택토 게임 - 2인 대전형)

이 프로젝트는 파이썬의 딕셔너리(Dictionary) 자료형을 활용하여 구현된 단순하고 직관적인 2인용 틱택토 게임입니다. 숫자 패드(1-9)의 레이아웃을 게임 보드의 위치로 사용하여 편의성을 높였습니다.

## 주요 특징
- **딕셔너리 기반 보드 관리**: 1부터 9까지의 키를 사용하여 보드의 각 칸을 관리하며, 플레이어의 선택에 따라 값을 'X' 또는 'O'로 업데이트합니다.
- **콘솔 기반 인터페이스**: 매 수마다 업데이트된 보드 상태를 텍스트 형식으로 화면에 출력하여 실시간 게임 진행 상황을 제공합니다.
- **턴 시스템**: 플레이어 'X'와 'O'가 번갈아 가며 수를 두는 로직이 포함되어 있습니다.
- **승리 및 무승부 판별**: 가로, 세로, 대각선의 모든 승리 조합을 확인하며, 9칸이 모두 찼음에도 승자가 없을 경우 무승부를 선언합니다.
- **재시작 기능**: 게임 종료 후 사용자의 입력에 따라 보드를 초기화하고 게임을 다시 시작할 수 있습니다.

## 코드 설명

### 1. 보드 초기화 및 출력
```python
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    # ... 격자 출력 ...
```

### 2. 게임 루프와 유효성 검사
10번의 반복(최대 9수) 내에서 각 턴의 유효성을 검사합니다.
```python
if theBoard[move] == ' ':
    theBoard[move] = turn
    count += 1
else:
    print("이미 채워진 자리입니다.")
```

### 3. 승리 조건 로직
5번째 수부터 승리 조건을 검사하여 효율성을 높였습니다.
```python
if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # 상단 가로줄
    # ... 승리 출력 ...
```

## 참고 자료
- [Python Dictionary Tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [How to make a Tic-Tac-Toe Game in Python](https://www.youtube.com/results?search_query=python+tic+tac+toe+tutorial)
