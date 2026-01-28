# Titanic Survival Prediction 2 (타이타닉 생존 예측 프로젝트 2)

이 프로젝트는 Kaggle의 타이타닉 데이터셋을 사용하여 승객의 생존 여부를 예측하는 머신러닝 데이터 분석 프로젝트입니다. 데이터 전처리, 특성 공학(Feature Engineering), 그리고 모델 학습의 전 과정을 다룹니다.

## 주요 특징
- **데이터 전처리**: 결측치 처리 및 불필요한 열(Cabin, Ticket, Name, PassengerId) 제거를 통해 학습 데이터의 품질을 높입니다.
- **특성 공학 (Feature Engineering)**:
  - **One-Hot Encoding**: 'Embarked'(승선 항구) 데이터를 수치형 데이터로 변환하기 위해 원-핫 인코딩을 적용합니다.
  - **Label Encoding**: 'Sex'(성별) 데이터를 0(남성)과 1(여성)로 매핑합니다.
- **시각화 및 분석**: 데이터의 형태(Shape)와 정보(Info)를 확인하며 생존에 영향을 미치는 주요 변수들을 파악합니다.

## 코드 설명

### 1. 데이터 로드 및 확인
Pandas를 사용하여 CSV 데이터를 읽어오고 기본 구조를 확인합니다.
```python
import pandas as pd
tit_data = pd.read_csv(r'./input/train.csv')
print(tit_data.shape)
print(tit_data.head())
```

### 2. 범주형 데이터 변환 (One-Hot Encoding)
승선 항구 정보를 개별적인 이진 열로 분리합니다.
```python
ports = pd.get_dummies(tit_data.Embarked, prefix = 'Embarked')
tit_data = tit_data.join(ports)
tit_data.drop(['Embarked'], axis = 1, inplace = True)
```

### 3. 성별 매핑 및 데이터 정제
```python
tit_data.Sex = tit_data.Sex.map({'male':0, 'female':1})
X = tit_data.drop(['Survived', 'Cabin', 'Ticket', 'Name', 'PassengerId'], axis = 1)
y = tit_data.Survived
```

## 참고 자료
- [Kaggle Titanic competition](https://www.kaggle.com/c/titanic)
- [Pandas get_dummies documentation](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html)
