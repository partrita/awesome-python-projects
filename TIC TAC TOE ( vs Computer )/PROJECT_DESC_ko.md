# Tic Tac Toe (vs Computer) (틱택토 게임 - 컴퓨터 대전형)

이 프로젝트는 파이썬의 기본 문법과 `random` 모듈을 사용하여 구현된 고전적인 틱택토(Tic-Tac-Toe) 게임입니다. 사용자 간의 2인 대전뿐만 아니라 인공지능(컴퓨터)과의 대전 모드도 지원합니다.

## 주요 특징
- **두 가지 게임 모드**: 
  - **1:1 대전**: 두 명의 사용자가 번갈아가며 착수할 수 있습니다.
  - **컴퓨터 대전**: 사용자가 'X', 컴퓨터가 'O'가 되어 대결하며, 컴퓨터는 간단한 알고리즘을 통해 최선의 수를 판단하려 시도합니다.
- **컴퓨터 AI 로직**: 
  - 자신이 이길 수 있는 자리가 있다면 즉시 착수합니다.
  - 상대방(사용자)이 이길 수 있는 자리가 있다면 방해합니다.
  - 특정한 상황에 따라 중앙 또는 구석 자리를 우선적으로 점유하려 시도합니다.
- **게임 상태 관리**: 보드가 가득 찼는지, 누가 이겼는지, 혹은 비겼는지를 실시간으로 판단하고 최종 점수를 집계합니다.

## 코드 설명

### 1. 보드 출력 및 생성
3x3 격자를 생성하고 현재 상태를 콘솔에 시각적으로 표시합니다.
```python
def displayBoard(board):
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('---------')
    # ... 중략 ...
```

### 2. 승리 조건 확인
가로, 세로, 대각선 중 어느 한 줄이라도 같은 표식('X' 또는 'O')이 완성되었는지 확인합니다.
```python
def iswon(board):
    # 가로, 세로, 대각선 승리 조합 체크
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or ...:
        return True
    return False
```

### 3. 컴퓨터의 수 결정 (AI 로직)
컴퓨터는 빈 자리를 파악하고, 승리 가능성이나 방어 필요성에 따라 우선순위를 정해 착수합니다.
```python
def computermove(board, letter):
    # 1. 이길 수 있는 자리가 있는지 확인
    # 2. 방어해야 할 자리가 있는지 확인
    # 3. 중앙(4번 인덱스) 확인
    # 4. 무작위 착수
```

## 참고 자료
- [Python Random Module Documentation](https://docs.python.org/3/library/random.html)
- [Tic-Tac-Toe Strategy (Wikipedia)](https://en.wikipedia.org/wiki/Tic-tac-toe)
