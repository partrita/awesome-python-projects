# Housing Prices Prediction (주택 가격 예측)

이 프로젝트는 주택의 크기, 침실 수, 욕실 수, 에어컨 유무 등 다양한 특성을 분석하여 해당 주택의 가격을 예측하는 머신러닝/딥러닝 모델을 구축하는 예제입니다.

## 주요 기능
- **데이터 분석 및 시각화**: `seaborn`의 `pairplot` 등을 사용하여 데이터 간의 상관관계를 시각적으로 분석합니다.
- **데이터 전처리**: 수치 데이터의 범위를 맞추기 위해 `MinMaxScaler`를 사용하여 정규화(Normalization)를 수행합니다.
- **딥러닝 모델 학습**: TensorFlow/Keras 기반의 신경망 모델을 사용하여 주택 가격을 회귀 분석합니다.

## 코드 설명

### 1. 데이터 로드 및 확인
`pandas`를 사용하여 `Housing.csv` 데이터를 읽어옵니다. 이 데이터는 주택 가격에 영향을 미치는 다양한 변수들을 포함하고 있습니다.

```python
import pandas as pd
import seaborn as sns

data = pd.read_csv('Housing.csv', delimiter=';')
print(data.head())
```

### 2. 데이터 전처리 (Scaling)
모델의 학습 속도와 성능을 높이기 위해 데이터를 0과 1 사이의 값으로 변환합니다.

```python
from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()
# 'lotsize' 등 주요 변수 정규화
scaled = mm.fit_transform(np.array(data['lotsize']).reshape(-1, 1))
```

### 3. 데이터 상관관계 분석
변수들 간의 관계를 파악하기 위해 전체 데이터의 pairplot을 그립니다.

```python
import seaborn as sns
sns.pairplot(data)
```

## 참고 자료
- [Scikit-learn MinMaxScaler](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)
- [Seaborn Visualization Guide](https://seaborn.pydata.org/tutorial/axis_grids.html)
