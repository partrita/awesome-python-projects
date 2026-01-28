# LOAN PREDICTION (대출 승인 예측)

이 프로젝트는 고객의 개인정보와 금융 데이터를 분석하여 대출 승인 여부를 예측하는 머신러닝 프로젝트입니다. 데이터 전처리, 탐색적 데이터 분석(EDA), 그리고 모델링 과정을 포함하고 있습니다.

## 주요 특징
- **데이터 전처리 및 EDA**: 결측치 처리, 파생 변수 생성, 그리고 `seaborn` 라이브러리를 이용한 데이터 시각화를 통해 승인 여부에 영향을 미치는 주요 요인을 분석합니다.
- **분류 모델 구축**: SVM(Support Vector Machine) 알고리즘을 사용하여 대출 승인 가능성을 이진 분류(Binary Classification)합니다.
- **성능 분석**: 성별, 결혼 여부, 부양 가족 수, 교육 수준 등에 따른 대출 승인 확률의 차이를 시각적으로 확인하고 모델의 성능을 평가합니다.

## 코드 설명
분석 및 모델링 과정의 주요 단계는 다음과 같습니다.

### 1. 데이터 탐색 및 시각화
대출 승인 상태(`Loan_Status`)에 따른 성별, 결혼 여부 등의 분포를 확인합니다.
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 성별에 따른 대출 승인 여부 시각화
sns.countplot(data['Loan_Status'], hue=data['Gender'])
```

### 2. 데이터 전처리
불필요한 열을 제거하고 머신러닝 모델 학습을 위해 데이터를 정제합니다.
```python
import pandas as pd

data = pd.read_csv('dataset.csv')
# Loan_ID 열 제거
data.drop(['Loan_ID'], axis=1, inplace=True)
# 결측치 확인
print(data.isnull().sum())
```

### 3. 모델 학습 및 평가
Scikit-learn을 사용하여 분류 모델을 학습시키고 성능을 확인합니다. (노트북에는 `model_svm.pkl` 파일이 포함되어 있어 학습된 모델을 불러와 사용할 수도 있습니다.)

## 참고 자료
- [Scikit-learn Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)
- [Pandas Documentation for Data Analysis](https://pandas.pydata.org/docs/)
- [Seaborn Visualization Guide](https://seaborn.pydata.org/)
