# QUIZ APP (퀴즈 애플리케이션)

이 프로젝트는 파이썬 객체 지향 프로그래밍(OOP) 개념을 활용하여 제작된 간단한 콘솔 기반 퀴즈 프로그램입니다.

## 주요 특징
- **객체 지향 설계**: `Question` 클래스를 정의하여 문제 내용과 정답을 효율적으로 관리합니다.
- **다양한 문제 구성**: 파이썬 상식 및 코드 결과 예측과 관련된 여러 문항이 준비되어 있습니다.
- **점수 산출 및 피드백**: 테스트 종료 후 맞춘 개수에 따라 "EXCELLENT", "WELL DONE" 등의 맞춤형 피드백을 제공합니다.
- **정답 확인 기능**: 사용자가 원할 경우 테스트 완료 후 각 문항의 정답을 확인할 수 있습니다.

## 코드 설명

### 1. 문제 데이터 관리
문제 지문과 정답을 클래스 인스턴스로 생성하여 리스트에 저장합니다.
```python
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# 문제 리스트 생성
questions = [
    Question(question_prompt[0], "b"),
    # ...
]
```

### 2. 테스트 실행 로직
사용자의 입력을 받아 정답 여부를 판별하고 최종 점수를 계산합니다.
```python
def run_test(questions):
    score = 0
    for q in questions:
        answer = input(q.prompt)
        if answer == q.answer:
            score += 1
    print(f"You got {score} / {len(questions)} correct")
```

## 참고 자료
- [Python Classes and Objects](https://www.w3schools.com/python/python_classes.asp)
- [Python input() function](https://docs.python.org/3/library/functions.html#input)
