# SINE_VS_COSINE (사인 vs 코사인 그래프 시각화)

이 프로젝트는 파이썬의 `numpy`와 `matplotlib` 라이브러리를 사용하여 삼각함수인 사인(Sine)과 코사인(Cosine) 파형을 그래프로 그려보고 비교하는 데이터 시각화 기초 예제입니다.

## 주요 특징
- **데이터 생성**: `numpy.linspace`를 사용하여 -2π에서 2π까지의 구간을 정밀하게 나누어 X축 데이터를 생성합니다.
- **삼각함수 계산**: `numpy.sin`과 `numpy.cos` 함수를 통해 각 지점에서의 진폭(Amplitude)을 계산합니다.
- **그래프 커스터마이징**: 제목, 축 이름 설정 및 그리드(Grid)를 추가하여 그래프의 가독성을 높였습니다.

## 코드 설명

### 1. 데이터 준비
수학적 연산을 위해 넘파이 배열을 생성합니다.
```python
import numpy as np

# -2π 에서 2π 까지 256개의 점 생성
time = np.linspace(-2*np.pi, 2*np.pi, 256, endpoint=True)
amplitude_sin = np.sin(time)
amplitude_cos = np.cos(time)
```

### 2. 그래프 시각화
`matplotlib`을 사용하여 두 파형을 한 화면에 출력합니다.
```python
import matplotlib.pyplot as plot

plot.plot(time, amplitude_sin) # 사인 곡선
plot.plot(time, amplitude_cos) # 코사인 곡선

plot.title('Sine & Cos wave')
plot.grid(True, which='both') # 그리드 활성화
plot.axhline(y=0, color='k')  # X축 강조
plot.show()
```

## 참고 자료
- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [Matplotlib Pyplot Tutorial](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
