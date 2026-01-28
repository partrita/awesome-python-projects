# Flight Fare Prediction (항공권 가격 예측)

이 프로젝트는 항공사, 여행 날짜, 출발지, 목적지 등 다양한 요인을 분석하여 항공권의 가격을 예측하는 머신러닝 모델을 구축하는 예제입니다. 데이터 전처리, 특징 공학(Feature Engineering), 시각화 과정을 상세히 포함하고 있습니다.

## 주요 기능
- **데이터 정제**: 결측치(Null values)를 제거하고 불필요한 정보를 필터링합니다.
- **특징 공학**: 여행 날짜에서 일/월 정보를 추출하고, 범주형 데이터를 수치 데이터로 변환(Label Encoding)합니다.
- **데이터 분석 및 시각화**: 항공사별 가격 분포, 소요 시간과 가격의 관계 등을 분석합니다.

## 코드 설명

### 1. 데이터 로드 및 결측치 처리
`pandas`를 사용하여 엑셀 데이터를 로드하고, 학습에 방해가 되는 결측치를 제거합니다.

```python
import pandas as pd

# 데이터 로드
df = pd.read_excel("data/data_train.xlsx")

# 결측치 확인 및 제거
df.dropna(inplace=True)
```

### 2. 범주형 데이터 인코딩
머신러닝 알고리즘이 처리할 수 있도록 항공사(`Airline`), 출발지(`Source`) 등 텍스트 데이터를 숫자로 변환합니다.

```python
from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()
df['Airline'] = encoder.fit_transform(df['Airline'])
df['Source'] = encoder.fit_transform(df['Source'])
df['Destination'] = encoder.fit_transform(df['Destination'])
```

### 3. 소요 시간 처리
`2h 50m`과 같은 문자열 형식의 소요 시간을 머신러닝 모델이 이해할 수 있는 형식으로 변환하거나 특징을 추출합니다.

```python
# 요일, 시간 등의 특징을 추출하는 과정이 Notebook에 포함되어 있습니다.
```

## 참고 자료
- [Scikit-learn LabelEncoder Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)
- [Machine Learning for regression problems](https://scikit-learn.org/stable/supervised_learning.html#supervised-learning)
