# SENTIMENT_ANALYSIS_ML_PROJECT (트위터 감성 분석 프로젝트)

이 프로젝트는 트위터 데이터를 활용하여 긍정적 또는 부정적 감성을 분류하는 고도화된 머신러닝 프로젝트입니다. 텍스트 정제부터 다양한 분류 알고리즘 적용까지의 전 과정을 포함합니다.

## 주요 특징
- **고급 데이터 전처리**: 사용자 핸들(@user) 제거, 특수 문자 및 짧은 단어 필터링, 그리고 어간 추출(Stemming)을 통해 텍스트 데이터를 정규화합니다.
- **다양한 머신러닝 알고리즘**:
  - 로지스틱 회귀 (Logistic Regression)
  - XGBoost 분류기 (XGBClassifier)
  - 결정 트리 (Decision Tree)
- **성능 평가**: Accuracy와 F1-score를 사용하여 모델의 정밀도를 측정하고 비교합니다.
- **방대한 데이터셋**: 약 3만 건 이상의 트레이닝 데이터를 처리하여 높은 신뢰도의 모델을 구축합니다.

## 코드 설명

### 1. 텍스트 정제 (Tidying Tweets)
정규표현식을 사용하여 중복되거나 무의미한 패턴을 제거합니다.
```python
import re

def remove_pattern(text, pattern):
    r = re.findall(pattern, text)
    for i in r:
        text = re.sub(i, "", text)
    return text

# @user 패턴 제거 및 짧은 단어 필터링
combine['Tidy_Tweets'] = np.vectorize(remove_pattern)(combine['tweet'], "@[\w]*")
combine['Tidy_Tweets'] = combine['Tidy_Tweets'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
```

### 2. 토큰화 및 어간 추출
단어를 기본 형태로 변환하여 모델이 학습하기 좋은 상태로 만듭니다.
```python
from nltk import PorterStemmer
ps = PorterStemmer()

tokenized_tweet = combine['Tidy_Tweets'].apply(lambda x: x.split())
tokenized_tweet = tokenized_tweet.apply(lambda x: [ps.stem(i) for i in x])
```

### 3. 모델 학습 및 평가
Scikit-learn과 XGBoost를 활용하여 분류 모델을 생성합니다.
```python
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

# 모델 학습 예시 (Logistic Regression)
lreg = LogisticRegression()
lreg.fit(xtrain_bow, ytrain)
prediction = lreg.predict_proba(xvalid_bow)
```

## 참고 자료
- [NLTK Documentation](https://www.nltk.org/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Scikit-learn Text Feature Extraction](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)
