# Credit Card Fraud Prediction (신용카드 부정 사용 예측)

이 프로젝트는 신용카드 결제 데이터를 분석하여 해당 거래가 정상인지, 아니면 부정 사용(Fraud)인지 감지하는 머신러닝 모델을 구축하는 예제입니다. 데이터의 불균형(정상 거래가 압도적으로 많음)을 처리하기 위해 `Isolation Forest`와 같은 이상 탐지 알고리즘을 사용합니다.

## 주요 기능
- **이상 탐지(Anomaly Detection)**: `Isolation Forest` 알고리즘을 사용하여 평소와 다른 패턴의 거래를 찾아냅니다.
- **데이터 시각화**: 상관관계 히트맵을 통해 다양한 특징(Features) 간의 관계를 분석합니다.
- **성능 평가**: 부정 사용 탐지 모델의 정확도와 정밀도를 평가합니다.

## 코드 설명

### 1. 데이터 로드 및 확인
약 28만 건의 거래 데이터가 포함된 `creditcard.csv` 파일을 읽어옵니다. 이 데이터는 보안상 실제 특징 대신 V1~V28로 이름 붙여진 PCA 변환 데이터로 구성되어 있습니다.

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('creditcard.csv')
print(data.shape) # (284807, 31)
```

### 2. 데이터 탐색 및 상관관계 분석
히트맵을 사용하여 결제 금액(`Amount`)이나 시간(`Time`)이 부정 사용(`Class`)과 어떤 연관이 있는지 분석합니다.

```python
corr_matrix = data.corr()
plt.figure(figsize=(30, 30))
sns.heatmap(corr_matrix, annot=True, cmap="RdYlGn")
plt.show()
```

### 3. Isolation Forest 모델 학습
이 알고리즘은 정상 데이터와 다른 '고립된' 데이터를 이상치로 판단합니다.

```python
from sklearn.ensemble import IsolationForest

# 모델 생성 (예상 오차율 0.01 설정 예시)
clf = IsolationForest(max_samples=len(X), contamination=0.01, random_state=42)
clf.fit(X)

# 예측 수행 (1: 정상, -1: 이상치)
y_pred = clf.predict(X)
```

## 참고 자료
- [Isolation Forest Algorithm Explained](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
