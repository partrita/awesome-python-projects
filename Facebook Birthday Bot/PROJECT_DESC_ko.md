# Facebook Birthday Bot (페이스북 생일 축하 봇)

이 프로젝트는 `Selenium`을 사용하여 페이스북 친구들의 생일을 자동으로 확인하고 축하 메시지를 남겨주는 자동화 스크립트입니다.

## 주요 기능
- **자동 로그인**: 사용자의 ID와 비밀번호를 입력받아 페이스북에 자동으로 로그인합니다.
- **생일 확인**: 오늘 생일인 친구가 몇 명인지 확인합니다.
- **축하 메시지 자동 전송**: 친구의 타임라인에 "Happy Birthday" 메시지를 자동으로 작성하고 게시합니다.

## 코드 설명

### 1. 웹드라이버 설정 및 로그인
`webdriver`를 사용하여 브라우저를 제어하고, 이메일과 비밀번호 입력란을 찾아 정보를 입력한 뒤 로그인 버튼을 누릅니다.

```python
from selenium import webdriver

# 크롬 드라이버 경로 설정
cd = 'C:\\webdrivers\\chromedriver.exe'
browser = webdriver.Chrome(cd)
browser.get('https://www.facebook.com/')

# 로그인 정보 입력
user_box = browser.find_element_by_id("email")
user_box.send_keys(user_id)
password_box = browser.find_element_by_id("pass")
password_box.send_keys(password)

# 로그인 버튼 클릭
login_box = browser.find_element_by_id("u_0_b")
login_box.click()
```

### 2. 생일 이벤트 페이지 이동 및 메시지 전송
생일인 친구 목록 페이지로 이동하여 메시지 입력창(`xpath` 이용)을 찾고, 루프를 돌며 축하 글을 작성합니다.

```python
# 생일 페이지로 이동
browser.get('https://www.facebook.com/events/birthdays/')

# 메시지 입력창 목록 가져오기
bday_list = browser.find_elements_by_xpath("//*[@class ='...']")

for element in bday_list:
    element.send_keys("Happy Birthday, Best wishes.")
    element.send_keys(Keys.RETURN)
```

## 사용 방법
1. Python과 `selenium` 라이브러리를 설치합니다.
2. 시스템 환경에 맞는 `chromedriver`를 다운로드하고 소스 코드 내 경로를 수정합니다.
3. 스크립트를 실행하고 터미널에 페이스북 계정 정보를 입력합니다.

## 참고 자료
- [Selenium Python Documentation](https://selenium-python.readthedocs.io/)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)
