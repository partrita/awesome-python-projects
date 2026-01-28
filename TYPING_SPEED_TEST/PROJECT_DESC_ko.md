# Typing Speed Test (타이핑 속도 측정기)

이 프로젝트는 파이썬의 `time` 모듈을 사용하여 사용자의 타이핑 속도(WPM)와 정확도를 측정하는 간단한 콘솔 기반 애플리케이션입니다.

## 주요 특징
- **속도 측정**: 사용자가 문장을 입력하는 데 걸린 시간을 초 단위로 계산하고, 이를 분당 단어 수(WPM, Words Per Minute)로 환산하여 보여줍니다.
- **정확도 계산**: 원본 문장과 사용자가 입력한 문장을 비교하여 단어 수준의 정확도를 백분율(%)로 계산합니다.
- **반복 기능**: 측정이 끝난 후 사용자의 선택에 따라 테스트를 재시도하거나 종료할 수 있습니다.

## 코드 설명

### 1. 시간 측정 및 입력
`time.time()`을 사용하여 입력 시작 시점과 종료 시점의 타임스탬프를 기록합니다.
```python
t0 = time.time()
# ... 문구 출력 ...
inputText = str(input())
t1 = time.time()
timeTaken = (t1 - t0)
```

### 2. 정확도 및 속도 산출
세트(Set) 인터섹션을 활용하여 정확하게 입력된 단어의 개수를 파악합니다.
```python
# 정확도 계산 (교집합 활용)
accuracy = len(set(inputText.split()) & set(string.split()))
accuracy = (accuracy / word_count)

# WPM 계산
wordsperminute = (lengthOfInput / timeTaken) * 60
```

### 3. 결과 출력
측정된 총 단어 수, 소요 시간, 정확도, 그리고 최종 속도를 보기 쉽게 출력합니다.
```python
print('Time used \t :', round(timeTaken, 2), 'seconds')
print('Your accuracy \t :', round(accuracy, 3) * 100, '%')
print('Speed is \t :', round(wordsperminute, 2), 'words per minute')
```

## 참고 자료
- [Python time module documentation](https://docs.python.org/3/library/time.html)
- [Words per minute (Wikipedia)](https://en.wikipedia.org/wiki/Words_per_minute)
