# Iris Flower Classification using ML (머신러닝을 이용한 붓꽃 분류)

이 프로젝트는 유명한 Iris(붓꽃) 데이터셋을 활용하여 꽃잎과 꽃받침의 크기에 따라 붓꽃의 종(Species)을 분류하는 머신러닝 프로젝트입니다. EDA(탐색적 데이터 분석)부터 모델 학습 및 평가까지의 전 과정을 포함합니다.

## 주요 기능
- **데이터 탐색 및 시각화**: `seaborn`과 `matplotlib`을 사용하여 데이터의 분포, 상관관계, 이상치 등을 다양한 그래프로 확인합니다.
- **분류 모델 학습**: Scikit-learn의 SVM(Support Vector Machine) 알고리즘을 사용하여 높은 정확도의 분류 모델을 구축합니다.
- **성능 평가**: 테스트 데이터를 활용하여 모델의 분류 성능을 점수로 확인합니다.

## 코드 설명

### 1. 데이터 시각화
데이터의 특성을 파악하기 위해 다양한 종류의 그래프를 활용합니다.

```python
import seaborn as sn
import matplotlib.pyplot as plt

df = sn.load_dataset('iris')

# 밀도 그래프 (Density Plot)
df.plot(kind='density', subplots=True, layout=(3,3), sharex=False)

# 산점도 행렬 (Pairplot)
sn.pairplot(df)
```

### 2. 모델 학습 및 평가
SVM 알고리즘 중 하나인 `SVC`를 사용하여 모델을 정의하고 학습시킵니다.

```python
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# 모델 생성 및 학습
model = SVC()
model.fit(X_train, Y_train)

# 정확도 확인
accuracy = model.score(X_test, Y_test)
print(f"모델 정확도: {accuracy}")
```

## 참고 자료
- [Scikit-learn SVC Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- [Seaborn Pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)
- [Iris Flower Dataset (Wikipedia)](https://en.wikipedia.org/wiki/Iris_flower_data_set)
