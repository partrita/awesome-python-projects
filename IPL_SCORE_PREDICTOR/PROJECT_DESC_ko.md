# IPL Score Predictor (IPL 점수 예측기)

이 프로젝트는 과거 IPL(Indian Premier League) 경기 데이터를 바탕으로 현재 경기의 최종 점수를 예측하는 웹 애플리케이션입니다. Flask 프레임워크를 사용하며, 머신러닝 알고리즘인 Random Forest Regressor를 활용하여 예측 모델을 구현했습니다.

## 주요 기능
- **실시간 예측**: 사용자가 타격 팀, 투구 팀, 현재 오버, 득점, 아웃 카운트 등을 입력하면 최종 점수 범위를 예측합니다.
- **머신러닝 기반**: `model.pkl`에 저장된 Random Forest 모델을 사용하여 학습된 데이터를 바탕으로 결과를 산출합니다.
- **웹 인터페이스**: Flask를 이용한 직관적인 웹 화면을 통해 누구나 쉽게 점수를 예측해 볼 수 있습니다.

## 코드 설명

### 1. 예측 로직 (`app.py`)
Flask 서버는 사용자의 입력을 받아 적절한 형태로 변환(One-Hot Encoding 등)한 뒤 모델에 전달합니다.

```python
@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    if request.method == 'POST':
        batting_team = request.form['batting-team']
        # 팀 이름을 숫자로 변환 (One-Hot Encoding 형식)
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1,0,0,0,0,0,0,0]
        # ... 기타 팀 변환 로직 ...
        
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        
        # 모델 입력 데이터 구성
        temp_array = temp_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        data = np.array([temp_array])
        
        # 점수 예측
        my_prediction = int(regressor.predict(data)[0])
        return render_template('index1.html', prediction_text="예측 점수 범위: {} ~ {}".format(my_prediction-10, my_prediction+5))
```

### 2. 모델 로드
`pickle` 라이브러리를 사용하여 미리 학습된 머신러닝 모델을 불러옵니다.

```python
import pickle

filename = 'model.pkl'
regressor = pickle.load(open(filename, 'rb'))
```

## 참고 자료
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Scikit-learn Random Forest Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html)
- [Pickle - Python object serialization](https://docs.python.org/3/library/pickle.html)
