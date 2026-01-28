# Search and edit Gui Application (위키백과 검색 및 편집 도구)

이 프로젝트는 `tkinter` GUI 라이브러리와 `wikipedia` 라이브러리를 결합하여 위키백과의 정보를 검색하고, 가져온 내용을 자유롭게 편집할 수 있는 데스크탑 애플리케이션입니다.

## 주요 특징
- **위키백과 통합 검색**: 사용자가 입력한 키워드를 바탕으로 위키백과 API를 호출하여 요약 정보를 가져옵니다.
- **텍스트 편집 기능**: 가져온 정보를 편집기 모드에서 수정할 수 있습니다. (편집 활성화/비활성화 기능 포함)
- **사용자 편의성**: 스크롤바가 포함된 텍스트 영역, 검색어 초기화 기능, 에러 메시지 알림 기능을 갖추고 있습니다.
- **다크 모드 지원**: 배경색과 버튼 색상에 어두운 테마를 적용하여 시각적 피로도를 줄였습니다.

## 코드 설명

### 1. 필드 및 UI 구성
클래스 기반으로 GUI 요소를 배치하고 변수를 관리합니다.
```python
class searchwiki:
    def __init__(self, root):
        self.root = root
        self.root.title("The Searching and Editing App")
        # 검색어 저장 변수
        self.var_search = StringVar()
        # 텍스트 영역 및 스크롤바 설정
        self.txt_area = Text(frame1, font=("times new roman", 15))
        # ... (생략)
```

### 2. 검색 및 데이터 연동
`wikipedia.summary`를 사용하여 온라인 데이터를 실시간으로 가져옵니다.
```python
def searchword(self):
    if self.var_search.get() == "":
        messagebox.showerror("ERROR", "Search box shouldn't be empty")
    else:
        # 위키백과 정보 수집
        fetch_data = wikipedia.summary(self.var_search.get())
        # 텍스트 영역에 삽입
        self.txt_area.insert('1.0', fetch_data)
```

### 3. 편집 모드 제어
텍스트 영역의 상태(`state`)를 변경하여 편집 여부를 결정합니다.
```python
def enable(self):
    self.txt_area.config(state=NORMAL) # 편집 가능

def disable(self):
    self.txt_area.config(state=DISABLED) # 읽기 전용
```

## 참고 자료
- [Wikipedia Python Library Documentation](https://wikipedia.readthedocs.io/en/latest/code.html)
- [Tkinter Text Widget Reference](https://www.tutorialspoint.com/python/tk_text.htm)
