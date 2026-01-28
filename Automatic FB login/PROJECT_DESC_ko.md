# Automatic FB Login (자동 페이스북 로그인)

이 프로젝트는 `selenium` 브라우저 자동화 라이브러리를 사용하여 페이스북에 자동으로 로그인하는 스크립트입니다.

## 주요 기능
- 사용자로부터 아이디(이메일)와 비밀번호를 입력받습니다.
- `webdriver.Chrome`을 사용하여 크롬 브라우저를 제어합니다.
- 페이스북 로그인 페이지의 요소(이메일함, 비밀번호함, 로그인 버튼)를 찾아 자동으로 데이터를 입력하고 클릭합니다.

## 코드 설명

### 1. 입력 및 설정
사용자로부터 계정 정보를 입력받고 크롬 드라이버의 위치를 설정합니다.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 사용자 정보 입력
user_id = input('페이스북 계정 아이디를 입력하세요: ')
password = input('비밀번호를 입력하세요: ')

# 크롬 드라이버 경로 설정
cd = 'C:\\webdrivers\\chromedriver.exe'
browser = webdriver.Chrome(cd)
```

### 2. 페이지 접속 및 로그인 수행
`browser.get`으로 페이스북에 접속한 후, HTML 요소의 ID를 사용하여 로그인 폼을 제어합니다.

```python
browser.get('https://www.facebook.com/')

# 이메일 입력창 찾기 및 입력
user_box = browser.find_element_by_id("email")
user_box.send_keys(user_id)

# 비밀번호 입력창 찾기 및 입력
password_box = browser.find_element_by_id("pass")
password_box.send_keys(password)

# 로그인 버튼 찾기 및 클릭
login_box = browser.find_element_by_id("u_0_b")
login_box.click()
```

## 주의 사항
- `chromedriver`의 버전이 현재 설치된 크롬 브라우저의 버전과 일치해야 합니다.
- 페이스북의 로그인 버튼 ID(`u_0_b`)는 시간이 지남에 따라 변경될 수 있으므로, 실제 작동하지 않을 경우 브라우저 개발자 도구(F12)로 현재 ID를 확인해야 합니다.
- 자동화된 접근은 서비스의 약관에 위배될 수 있으므로 주의하여야 합니다.

## 참고 자료
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [Chrome Driver Downloads](https://chromedriver.chromium.org/downloads)
