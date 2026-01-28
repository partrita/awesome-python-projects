# URL Shortener (URL 단축기)

이 프로젝트는 TinyURL의 외부 API를 활용하여 긴 웹 주소를 짧게 변환해주는 파이썬 유틸리티입니다. 커맨드라인 인수를 통해 하나 이상의 URL을 전달받아 단축된 결과를 즉시 출력합니다.

## 주요 특징
- **외부 API 통합**: TinyURL에서 제공하는 `api-create.php` 엔드포인트를 호출하여 안정적인 단축 서비스를 제공합니다.
- **다중 처리 지원**: `map` 함수를 사용하여 여러 개의 긴 URL을 한 번에 처리하고 출력할 수 있습니다.
- **간결한 구현**: 별도의 라이브러리 설치 없이 파이썬 표준 라이브러리(`urllib`)만을 사용하여 가볍고 빠르게 동작합니다.

## 코드 설명

### 1. 단축 로직 (TinyURL API 호출)
`urllib`를 사용하여 TinyURL 서버에 요청을 보내고, 변환된 단축 주소를 응답받아 디코딩합니다.
```python
def short_url(url): 
    # TinyURL API 엔드포인트 구성
    request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))     
    with contextlib.closing(urlopen(request_url)) as response:                       
        return response.read().decode('utf-8 ')
```

### 2. 메인 실행 루프
프로그램 실행 시 인자로 전달된 모든 URL에 대해 단축 함수를 실행합니다.
```python
def main():                                                                 
    for url in map(short_url, sys.argv[1:]):                    
        print(url) 
```

## 사용 방법
터미널에서 다음과 같이 실행합니다:
```bash
python app.py https://www.google.com https://github.com
```

## 참고 자료
- [TinyURL API Information](https://tinyurl.com/app/dev)
- [Python urllib documentation](https://docs.python.org/3/library/urllib.html)
