# Letter Partner Game (글자 짝짓기 게임)

이 프로젝트는 영어 알파벳의 전반부(a-m)와 후반부(n-z)를 각각 'Pre-partner'와 'Post-partner'로 정의하고, 입력된 단어가 특정 대응 규칙을 만족하는지 검사하는 로직 퍼즐 게임입니다.

## 게임 규칙
알파벳 순서에 따라 'a'는 'n', 'b'는 'o', ..., 'm'은 'z'와 짝이 됩니다. 사용자가 입력한 단어 `w`가 다음 조건을 모두 만족하면 승리합니다.

1.  **필수 짝 존재**: 단어에 포함된 모든 Pre-partner는 반드시 대응하는 Post-partner를 가져야 합니다.
2.  **순서 원칙**: Pre-partner는 항상 대응하는 Post-partner보다 앞에 위치해야 합니다.
3.  **배치 제약**:
    -   Post-partner는 Pre-partner 바로 다음 칸(`i+1`)에 오거나,
    -   자신보다 먼저 나온 Pre-partner들의 짝보다는 앞에, 나중에 나온 Pre-partner들의 짝보다는 뒤에 위치해야 합니다. (중첩 구조 허용)

### 예시
-   **승리**: `abon` ('o'는 'b' 바로 뒤에 있고, 'n'은 'a'의 짝으로 전체 구조를 만족함)
-   **패배**: `abno` ('a'의 짝인 'n'이 'b'의 짝인 'o'보다 먼저 나왔으므로 규칙 위반)

## 코드 설명

### 1. 짝 데이터 구성
알파벳을 두 그룹으로 나누어 리스트로 관리합니다.
```python
list1=['a','b','c','d','e','f','g','h','i','j','k','l','m']
list2=['n','o','p','q','r','s','t','u','v','w','x','y','z']
```

### 2. 조건 검사 로직
입력된 단어를 순회하며 각 문자의 파트너 존재 여부와 위치 규칙을 검증합니다.
```python
for j in prepartner:
    list1index = list1.index(j)
    if not (list2[list1index] in postpartner):
        print("YOU LOST") # 짝이 없음
        sys.exit()
```

## 참고 자료
- [Python List Methods](https://docs.python.org/3/tutorial/datastructures.html)
- [String index() Method](https://www.w3schools.com/python/ref_string_index.asp)
