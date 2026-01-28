# IRIS_FLOWER_DETECTION (머신러닝을 이용한 붓꽃 분류)

이 프로젝트는 붓꽃(Iris) 데이터셋을 활용하여 꽃잎(Petal)과 꽃받침(Sepal)의 길이 및 너비를 기반으로 꽃의 종류를 인공지능으로 분류하는 머신러닝 프로젝트입니다.

## 주요 특징
- **데이터 탐색 및 시각화**: `pandas`, `matplotlib`, `seaborn` 라이브러리를 사용하여 데이터의 분포와 특성 간의 관계를 시각적으로 분석합니다.
- **머신러닝 모델 사용**: 서포트 벡터 머신(SVM) 알고리즘인 `SVC`를 사용하여 정교한 분류 모델을 생성합니다.
- **모델 최적화 (Hyperparameter Tuning)**: `GridSearchCV`를 활용하여 모델의 성능을 결정하는 파라미터(`C`, `gamma`)의 최적 조합을 찾습니다.
- **상세한 성능 평가**: 분류 보고서(Classification Report)와 혼동 행렬(Confusion Matrix)을 통해 모델이 얼마나 정확하게 분류했는지 평가합니다.

## 코드 설명
이 프로젝트의 핵심 머신러닝 단계는 다음과 같습니다.

### 1. 데이터 시각화 (EDA)
`seaborn`의 `pairplot`을 사용하여 각 품종별 데이터 분포를 한눈에 파악합니다.
```python
import seaborn as sns
sns.pairplot(iris, hue='species', palette='Dark2')
```

### 2. 모델 학습 및 최적화
`GridSearchCV`를 사용하여 최적의 파라미터를 찾고 모델을 학습시킵니다.
```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

param_grid = {'C': [0.1, 1, 10, 100], 'gamma': [1, 0.1, 0.01, 0.001]}
grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=2)
grid.fit(X_train, y_train)
```

### 3. 예측 및 평가
완성된 모델로 테스트 데이터를 예측하고 정확도를 분석합니다.
```python
from sklearn.metrics import classification_report, confusion_matrix
grid_predictions = grid.predict(X_test)
print(confusion_matrix(y_test, grid_predictions))
print(classification_report(y_test, grid_predictions))
```

## 참고 자료
- [Scikit-learn SVC Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)
- [Iris flower data set (Wikipedia)](https://en.wikipedia.org/wiki/Iris_flower_data_set)
