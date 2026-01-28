# Breast Cancer Detection (유방암 검출)

이 프로젝트는 텐서플로우(TensorFlow)와 케라스(Keras)를 사용하여 유방암 데이터를 분류하는 인공 신경망 모델을 구축하는 예제입니다. 1D CNN(Convolutional Neural Network) 구조를 사용하여 악성(Malignant)과 양성(Benign) 종양을 구별합니다.

## 주요 기능
- **데이터셋**: Scikit-learn에서 제공하는 위스콘신 유방암 데이터셋을 사용합니다.
- **모델 구조**: `Conv1D`, `Dropout`, `Flatten`, `Dense` 레이어를 결합하여 구축합니다.
- **성능 최적화**: `StandardScaler`를 통한 데이터 정규화와 `Dropout`을 통한 과적합 방지를 수행합니다.

## 코드 설명

### 1. 라이브러리 및 데이터 준비
텐서플로우와 데이터 처리를 위한 판다스, 넘파이를 가져옵니다.

```python
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dropout, Conv1D, Dense, Flatten
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 데이터셋 로드
cancer = datasets.load_breast_cancer()
X = pd.DataFrame(data=cancer.data, columns=cancer.feature_names)
y = cancer.target
```

### 2. 전처리
학습 성능을 높이기 위해 데이터를 표준화(Standardization)하고, CNN 입력 형식에 맞게 리셰이프(Reshape)합니다.

```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 3D 텐서로 변환 (샘플 수, 특징 수, 채널 수)
X_train = X_train.reshape(455, 30, 1)
X_test = X_test.reshape(114, 30, 1)
```

### 3. CNN 모델 구축
1차원 합성곱 레이어를 사용하여 특징을 추출하고, 마지막 레이어에서 시그모이드(Sigmoid) 활성화 함수를 통해 확률 값을 출력합니다.

```python
model = Sequential()
model.add(Conv1D(filters=32, kernel_size=2, activation='relu', input_shape=(30, 1)))
model.add(Dropout(0.2))
model.add(Conv1D(filters=64, kernel_size=2, activation='relu'))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
```

## 참고 자료
- [TensorFlow Conv1D Layer](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv1D)
- [UCI Breast Cancer Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))
