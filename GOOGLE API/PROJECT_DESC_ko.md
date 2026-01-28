# Google Geocoding API 활용 지리 데이터 분석

이 프로젝트는 Google Geocoding API를 사용하여 주소 데이터를 위도와 경도로 변환하고, 이를 데이터베이스에 저장한 후 지도상에 시각화하는 과정을 다룹니다.

## 주요 기능
- **지오코딩(Geocoding)**: 텍스트 주소를 지리적 좌표로 변환합니다.
- **데이터 캐싱**: 지오코딩 결과를 `SQLite3` 데이터베이스에 저장하여 불필요한 API 호출을 방지합니다.
- **시각화**: 수집된 데이터를 바탕으로 HTML/JS 기반의 지도 위에 위치를 표시합니다.

## 코드 설명

### 1. 데이터 로드 및 API 호출 (geoload.py)
`where.data` 파일에 저장된 주소들을 한 줄씩 읽어 Google API로 정보를 요청합니다. 받아온 JSON 데이터는 `Locations` 테이블에 저장됩니다.

```python
import sqlite3
import urllib.request, urllib.parse

# 데이터베이스 연결
conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# API 서비스 주소 (Google API 또는 연습용 프록시)
serviceurl = "http://py4e-data.dr-chuck.net/json?"

# 주소 데이터를 URL 인코딩하여 요청
url = serviceurl + urllib.parse.urlencode({"address": address})
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
```

### 2. 데이터 베이스 저장
이미 처리된 주소는 데이터베이스에서 조회하여 넘어가고, 새로운 주소만 API를 호출함으로써 효율적으로 관리합니다.

```python
cur.execute('''INSERT INTO Locations (address, geodata) VALUES ( ?, ? )''',
            (memoryview(address.encode()), memoryview(data.encode())))
conn.commit()
```

### 3. 결과 확인 (geodump.py 및 where.html)
저장된 데이터를 읽어 JS 파일(`where.js`)을 생성하고, 브라우저에서 `where.html`을 열어 지도상에 표시된 위치를 확인할 수 있습니다.

## 참고 자료
- [Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview)
- [Python SQLite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)
