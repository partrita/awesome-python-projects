# AI Algorithm Solvers (틱택토 minimax 및 알고리즘 문제 해결사)

이 프로젝트는 인공지능의 기초 알고리즘들을 활용하여 고전적인 퍼즐과 게임 문제를 해결하는 파이썬 구현체들을 담고 있습니다. 틱택토의 Minimax 알고리즘, 8-퍼즐의 탐색 알고리즘, 8-퀸 문제의 언덕 오르기 알고리즘을 포함합니다.

## 주요 구성 요소

### 1. Tic Tac Toe (Minimax Algorithm)
- **설명**: `tkinter` 라이브러리를 사용한 GUI 기반 틱택토 게임입니다.
- **알고리즘**: **Minimax 알고리즘**을 사용하여 컴퓨터가 모든 수의 경우의 수를 계산하고 최선의 수를 선택하도록 설계되었습니다. 이론적으로 사용자는 컴퓨터를 이길 수 없으며, 최선의 경우 무승부를 기록합니다.

### 2. 8-Puzzle Solver
- **설명**: 3x3 격자에서 숫자 타일을 이동시켜 목표 상태를 만드는 퍼즐입니다.
- **알고리즘**: **깊이 우선 탐색(DFS)** 및 **반복적 깊이 심화(Iterative Deepening)** 기법을 사용하여 최소한의 이동 경로를 찾아냅니다.

### 3. 8-Queens Solver
- **설명**: 8x8 체스판에 8개의 퀸을 서로 공격하지 못하게 배치하는 유명한 문제입니다.
- **알고리즘**: **언덕 오르기(Hill Climbing) 알고리즘**을 사용하여 충돌 횟수를 최소화하는 방향으로 위치를 조정하며 해답을 찾습니다.

## 코드 설명 (Tic Tac Toe Minimax)

### Minimax 핵심 로직
현재 상태에서 시작하여 재귀적으로 모든 가능한 수를 탐색하고 점수(승리: 1, 패배: -1, 무승부: 0)를 부여합니다.
```python
def minimax(self, board, ismax):
    res = self.check_win(board)
    if res != -1:
        return self.score[res]
    
    if ismax: # 컴퓨터의 턴 (점수 최대화)
        score = -2
        for i, j in self.get_vacant_places(board):
            # ... 재귀 호출 ...
            score = max(score, self.minimax(board, False))
        return score
    else: # 사용자의 턴 (점수 최소화)
        # ... 동일한 방식의 최소화 전략 ...
```

## 참고 자료
- [Minimax Algorithm in Game Theory](https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/)
- [Hill Climbing Algorithm in AI](https://www.javatpoint.com/hill-climbing-algorithm-in-ai)
- [Iterative Deepening Depth-First Search](https://en.wikipedia.org/wiki/Iterative_deepening_depth-first_search)
