# Admission Prediction using ML (머신러닝을 이용한 입학 예측)

이 프로젝트는 학생들의 GRE 성적, TOEFL 성적, 대학 평점(CGPA) 등을 기반으로 대학 입학 확률을 예측하는 머신러닝 모델을 구축한 것입니다.

## 주요 기능
- **데이터 분석 및 시각화**: `seaborn` 및 `matplotlib`을 사용하여 데이터 간의 상관관계를 탐색합니다.
- **데이터 전처리**: 불필요한 열(Serial No.)을 삭제하고 데이터를 학습에 적합하게 정리합니다.
- **선형 회귀(Linear Regression)**: `sklearn`의 선형 회귀 모델을 사용하여 성적과 입학 확률 간의 관계를 모델링합니다.
- **성능 평가**: 예측값과 실제값을 비교하여 모델의 정확도를 평가합니다.

## 코드 설명

### 1. 데이터 로드 및 확인
`pandas` 라이브러리를 사용하여 CSV 데이터를 읽어오고 상위 행을 확인합니다.

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드
df = pd.read_csv("Admission_Predict_Ver1.1.csv")
print(df.head(8))
```

### 2. 데이터 탐색 (EDA)
상관관계 행렬과 히트맵을 통해 어떤 성적이 입학 확률에 가장 큰 영향을 미치는지 확인합니다.

```python
# 상관관계 히트맵 시각화
sns.heatmap(df.corr(), annot=True)
plt.show()

# CGPA 분포 시각화
sns.distplot(df.CGPA)
plt.show()
```

### 3. 모델 구축 및 학습
입학 확률에 영향이 큰 요소들을 독립 변수(X)로 설정하고, 선형 회귀 모델을 학습시킵니다.

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 특징값(X)과 타겟값(y) 설정
x = df[['GRE Score', 'TOEFL Score', 'CGPA']]
y = df[['Chance of Admit ']]

# 데이터셋 분리 (학습용 80%, 테스트용 20%)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

# 선형 회귀 모델 생성 및 학습
linreg = LinearRegression()
linreg.fit(x_train, y_train)
```

### 4. 결과 평가
평균 절대 오차(MAE)를 계산하여 모델의 성능을 확인합니다.

```python
from sklearn import metrics
y_pred = linreg.predict(x_test)
print(metrics.mean_absolute_error(y_test, y_pred)) # MAE 출력
```

## 참고 자료
- [Scikit-learn Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Seaborn Visualization Guide](https://seaborn.pydata.org/tutorial.html)
