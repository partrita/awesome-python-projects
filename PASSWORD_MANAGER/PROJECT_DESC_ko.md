# PASSWORD_MANAGER (비밀번호 관리 매니저)

이 프로젝트는 Tkinter를 사용하여 구현된 비밀번호 생성 및 관리 도구입니다. 임의의 강력한 비밀번호를 생성하고, 이를 사용자 이름 및 웹사이트 정보와 함께 파일에 저장할 수 있습니다.

## 주요 특징
- **비밀번호 생성**: 보안 수준(낮음, 중간, 높음)과 길이를 선택하여 무작위 비밀번호를 생성합니다.
- **클립보드 복사**: 생성된 비밀번호를 즉시 복사하여 편리하게 사용할 수 있습니다.
- **데이터 저장 및 조회**: `info.txt` 파일에 계정 정보(사용자 이름, 비밀번호, 웹사이트)를 안전하게 기록하고, 저장된 전체 정보를 콘솔에서 조회할 수 있습니다.
- **사용자 친화적 GUI**: 직관적인 레이아웃을 통해 누구나 쉽게 비밀번호를 관리할 수 있습니다.

## 코드 설명

### 1. 비밀번호 생성 로직
선택된 보안 등급에 따라 문자, 숫자, 특수문자를 조합합니다.
```python
def low(): 
    # 길이 및 문자 셋 설정
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "...(대문자 포함)..."
    digits = "...(특수문자 및 숫자 포함)..."
    
    # 보안 등급에 따른 생성
    if var.get() == 1: # Low
        for i in range(0, length): 
            password = password + random.choice(lower) 
    # ... (Medium, Strong 로직 생략)
```

### 2. 파일 입출기능
비밀번호 정보를 텍스트 파일에 추가로 기록합니다.
```python
def appendNew():
    file = open("info.txt", 'a')
    # 입력 폼에서 데이터 가져오기
    userName = entry1.get() 
    website = entry2.get()
    # 파일에 포맷팅하여 저장
    file.write(f"UserName: {userName}\nPassword: {pwd}\nWebsite: {web}\n")
    file.close()
```

## 참고 자료
- [Tkinter Widgets Reference](https://tkdocs.com/tutorial/widgets.html)
- [Python Random Module](https://docs.python.org/3/library/random.html)
- [Pyperclip Module (Clipboard Handling)](https://pypi.org/project/pyperclip/)
