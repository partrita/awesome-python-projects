# SENTIMENT_ANALYSER_ML_PROJECT (감성 분석기 프로젝트)

이 프로젝트는 텍스트 데이터를 분석하여 그 안에 담긴 감정(Emotion)을 분류하고 시각화하는 자연어 처리(NLP) 기반의 기초 머신러닝 프로젝트입니다.

## 주요 특징
- **텍스트 전처리**: 대소문자 변환, 문장 부호 제거, 불용어(Stop words) 제거를 통해 분석에 필요한 핵심 단어들을 추출합니다.
- **감정 매핑**: `emotions.txt` 파일을 활용하여 각 단어가 어떤 특정 감정(행복, 슬픔, 화남 등)을 나타내는지 매칭합니다.
- **결과 시각화**: `matplotlib` 라이브러리를 사용하여 분석된 감정들의 분포를 막대 그래프(Bar Chart)로 시각화합니다.

## 코드 설명

### 1. 데이터 클리닝 및 토큰화
텍스트에서 의미 없는 기호나 불용어를 걸러냅니다.
```python
# 문장 부호 제거 및 소문자 변환
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
tokenized_words = cleaned_text.split()

# 불용어(Stop words) 필터링
final_words = [word for word in tokenized_words if word not in stop_words]
```

### 2. 감정 분석 알고리즘
준비된 감정 사전을 읽어와 추출된 단어들과 비교합니다.
```python
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        word, emotion = line.replace("\n", '').replace(",", '').split(':')
        if word in final_words:
            emotion_list.append(emotion)
```

### 3. 결과 그래프 저장
분석된 감정의 빈도수를 그래프로 나타냅니다.
```python
from collections import Counter
w = Counter(emotion_list)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
plt.savefig('graph.png') # 결과를 이미지로 저장
```

## 참고 자료
- [A Beginner's Guide to Sentiment Analysis in Python](https://uclalibrary.github.io/research-tips-workshops/python-sentiment-analysis/)
- [Matplotlib Bar Chart Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html)
