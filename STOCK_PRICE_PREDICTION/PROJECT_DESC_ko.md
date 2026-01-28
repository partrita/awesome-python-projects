# STOCK_PRICE_PREDICTION (주가 예측 프로젝트)

이 프로젝트는 딥러닝 알고리즘인 LSTM(Long Short-Term Memory)을 사용하여 구글(Google)의 과거 주가 데이터를 학습하고 미래의 종가를 예측하는 인공지능 프로젝트입니다.

## 주요 특징
- **시계열 데이터 처리**: 과거 100일간의 주가 흐름을 입력값으로 받아 다음 날의 가격을 예측하는 슬라이딩 윈도우(Sliding Window) 방식을 사용합니다.
- **순환 신경망(RNN) 모델**: 
  - 양방향 LSTM(Bidirectional LSTM)을 사용하여 데이터의 전후 맥락을 모두 파악합니다.
  - Keras의 `Sequential` API를 이용해 여러 층의 신경망을 구성했습니다.
- **데이터 정규화**: `MinMaxScaler`를 사용하여 주가 데이터를 0과 1 사이의 값으로 변환함으로써 모델의 학습 속도와 성능을 향상시켰습니다.
- **GPU 가속 학습**: 많은 양의 연산을 빠르게 처리하기 위해 GPU 가속 기능을 활용하여 모델을 훈련했습니다.

## 코드 설명

### 1. 데이터 정규화 및 변환
LSTM 모델에 적합하도록 데이터를 스케일링하고 타임스탬프 형식으로 변환합니다.
```python
from sklearn.preprocessing import MinMaxScaler

# 0~1 사이로 정규화
minmax = MinMaxScaler()
scaled_data = minmax.fit_transform(close_price.reshape(-1, 1))

# 100일 단위의 데이터 셋 생성
data_stamps = []
for i in range(len(scaled_data) - 100):
    data_stamps.append(scaled_data[i:i+100])
```

### 2. LSTM 신경망 모델 구축
양방향 LSTM 층과 Dense 층을 쌓아 모델을 정의합니다.
```python
from keras.models import Sequential
from keras.layers import Dense, LSTM, Bidirectional

model = Sequential()
model.add(Bidirectional(LSTM(100, return_sequences=True), input_shape=(100, 1)))
model.add(Bidirectional(LSTM(100)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear')) # 종가 예측을 위한 선형 활성화 함수
```

### 3. 모델 컴파일 및 학습
Adam 옵티마이저와 평균 제곱 오차(MSE) 손실 함수를 사용합니다.
```python
model.compile(optimizer='Adam', loss='mse')
model.fit(x_train, y_train, epochs=50)
```

## 참고 자료
- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/)
- [Keras Bidirectional Layer Documentation](https://keras.io/api/layers/recurrent_layers/bidirectional/)
- [Stock Price Prediction using Python and LSTM](https://www.geeksforgeeks.org/stock-price-prediction-using-lstm/)
