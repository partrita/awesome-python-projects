# SECURE_YOUR_PASSWORD (비밀번호 보안 강화 도구)

이 프로젝트는 입력된 문자열의 각 문자를 미리 정의된 특수 기호 맵에 따라 변환하여, 일반 범용 텍스트를 복잡한 기호 조합의 비밀번호로 바꿔주는 간단한 보안 유틸리티입니다.

## 주요 특징
- **기호 매핑 방식**: 딕셔너리(`sym`)를 사용하여 알파벳 각 문자에 대응하는 고유한 특수 기호를 설정합니다.
- **간단한 변환 로직**: 반복문을 이용해 입력값의 각 문자를 확인하고, 해당되는 기호로 치환하여 결과를 생성합니다.
- **커스터마이징 가능**: 매핑 딕셔너리를 수정하여 자신만의 고유한 암호화 규칙을 만들 수 있습니다.

## 코드 설명

### 1. 매핑 딕셔너리 구성
알파벳 소문자에 대응하는 특수 기호들을 정의합니다.
```python
sym = {
    'a' : '!!',
    'b' : '@',
    'c' : '#',
    # ... (생략)
    'z' : '|',
}
```

### 2. 변환 엔진
입력 문자열을 순회하며 비밀번호를 빌드합니다.
```python
inp = 'alphabet'
password = ''

for i in inp:
    for key, val in sym.items():
        if i in key:
            password = password + val

print("Original Name:", inp)
print("Secured Password:", password)
```

## 참고 자료
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
- [Python String Loop](https://www.w3schools.com/python/python_strings_looping.asp)
