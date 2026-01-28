# Credit Card Fraud Detection (신용카드 부정 사용 탐지)

이 프로젝트는 머신러닝 알고리즘(Random Forest)을 사용하여 신용카드 거래 데이터 중 사기(Fraudulent) 거래를 탐지하는 보안 솔루션 모델입니다. 고객이 구매하지 않은 항목에 대해 요금이 청구되는 것을 방지하는 데 목적이 있습니다.

## 주요 특징
- **데이터 불균형 처리**: 정상 거래와 사기 거래의 비율 차이가 매우 큰 실제 금융 데이터를 다루며, 사기 사례의 희소성을 고려한 분석을 수행합니다.
- **탐색적 데이터 분석 (EDA)**: 상관관계 행렬(Correlation Matrix) 및 히트맵을 사용하여 각 변수 간의 관계와 사기 거래의 특성을 시각화합니다.
- **Random Forest 모델**: 앙상블 학습 기법인 랜덤 포레스트 분류기를 사용하여 높은 정확도와 정밀도로 사기 거래를 분류합니다.
- **성능 평가 지표**: 정확도(Accuracy)뿐만 아니라 불균형 데이터셋에 중요한 정밀도(Precision), 재현율(Recall), F1-Score, Matthews 상관계수(MCC)를 통해 모델을 다각도로 평가합니다.

## 코드 설명

### 1. 데이터 확인 및 결측치 처리
데이터셋의 형태를 확인하고 결측치를 평균값으로 대체하여 안정적인 학습 환경을 구축합니다.
```python
# 결측치 확인 및 대체
data['Class'] = data['Class'].fillna(0)
items = data.columns
for item in items:
    if item != 'Class':
        data[item] = data[item].fillna(data[item].mean())
```

### 2. 사기 사례 분석
정상 거래와 사기 거래의 분포 및 금액 차이를 분석합니다.
```python
fraud = data[data['Class'] == 1]
valid = data[data['Class'] == 0]
print("사기 사례 수:", len(fraud))
print("정상 사례 수:", len(valid))
```

### 3. 모델 학습 및 평가
랜덤 포레스트 분류기를 생성하고 테스트 데이터를 통해 성능을 측정합니다.
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 모델 생성 및 학습
rfc = RandomForestClassifier()
rfc.fit(xTrain, yTrain)

# 예측 및 성능 출력
yPred = rfc.predict(xTest)
print("정확도 (Accuracy):", accuracy_score(yTest, yPred))
```

## 참고 자료
- [Scikit-learn Random Forest Classifier Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Credit Card Fraud Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
