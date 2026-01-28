# Twitter Bot (트위터 자동화 봇)

이 프로젝트는 파이썬의 `tweepy` 라이브러리를 사용하여 트위터(X) 작업을 자동화하는 봇입니다. 특정 키워드를 검색하여 리트윗, 좋아요, 팔로우를 하거나 매일 정해진 메시지를 게시할 수 있습니다.

## 주요 특징
- **트윗 검색 및 인터랙션**: 설정된 쿼리(Query)에 부합하는 트윗을 찾아 자동으로 리트윗하거나 '좋아요'를 누릅니다.
- **자동 팔로우**: 특정 주제에 대해 트윗을 올린 사용자를 자동으로 팔로우하여 네트워크를 확장합니다. (이미 팔로우 중인지 확인하는 로직 포함)
- **일일 트윗 게시**: 현재 요일에 맞춰 미리 설정된 메시지(예: "Happy Monday")를 자동으로 게시합니다.
- **유연한 설정**: `config.py`를 통해 각 기능의 활성화 여부와 작업 간격(Sleep Time)을 쉽게 조정할 수 있습니다.

## 코드 설명

### 1. 인증 및 API 설정
`tweepy`를 사용하여 트위터 개발자 계정의 자격 증명을 인증하고 API 인스턴스를 생성합니다.
```python
import tweepy
from credientials import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
```

### 2. 검색 및 작업 자동화
`tweepy.Cursor`를 사용하여 실시간 트윗을 탐색하고 설정된 작업을 수행합니다.
```python
for tweet in tweepy.Cursor(api.search, q=QUERY).items():
    if RETWEET:
        tweet.retweet()
    if LIKE:
        tweet.favorite()
    if FOLLOW and not tweet.user.following:
        tweet.user.follow()
```

### 3. 요일별 자동 트윗
`datetime` 모듈을 활용하여 요일을 판별하고 맞춤 메시지를 업데이트합니다.
```python
if EVERYDAY_TWEETS:
    weekday = datetime.date.today().weekday()
    # 요일에 따른 메시지 선택 (0=월요일, 6=일요일)
    api.update_status(tweettopublish)
```

## 참고 자료
- [Tweepy Documentation](https://docs.tweepy.org/)
- [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api)
