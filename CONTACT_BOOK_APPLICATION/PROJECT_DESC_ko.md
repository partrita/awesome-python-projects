# Contact Book Application (연락처 관리 애플리케이션)

이 프로젝트는 `Tkinter`와 `Sqlite3`를 사용하여 연락처 정보를 데이터베이스에 저장하고 관리(생성, 조회, 수정, 삭제)하는 GUI 애플리케이션입니다.

## 주요 기능
- **데이터베이스 연동**: `sqlite3`를 사용하여 로컬 파일(`mysq.db`)에 연락처를 영구 저장합니다.
- **GUI 인터페이스**: `Tkinter`를 통해 이름과 전화번호를 입력받고 버튼으로 명령을 실행합니다.
- **CRUD 작업**:
  - **Submit**: 연락처 추가
  - **Show**: 전체 연락처 터미널 출력
  - **Update**: 전화번호를 기준으로 이름 변경
  - **Delete**: 이름 기준으로 연락처 삭제
  - **Drop table**: 테이블 전체 삭제

## 코드 설명

### 1. 데이터베이스 초기화
프로그램 실행 시 `people` 테이블이 없으면 자동으로 생성합니다.

```python
import sqlite3

db = sqlite3.connect('mysq.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS people(name TEXT, phone TEXT)")
db.commit()
```

### 2. 연락처 추가 (Insert)
사용자가 입력한 이름과 전화번호를 DB에 저장합니다.

```python
def insert():
    name1 = textin.get()
    phone1 = textinn.get()
    conn = sqlite3.connect('mysq.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO people(name, phone) VALUES(?,?)', (name1, phone1))
    # conn.commit()은 with 문에 의해 자동 처리됩니다.
```

### 3. 연락처 수정 및 삭제 (Update & Delete)
특정 조건을 만족하는 레코드를 수정하거나 삭제하는 SQL 쿼리를 실행합니다.

```python
def updateContact():
    nam = name.get()
    ph = phone.get()
    connnt = sqlite3.connect('mysq.db')
    cursor = connnt.cursor()
    cursor.execute("UPDATE people SET name = ? WHERE phone = ?", (nam, ph))
    connnt.commit()

def det():
    dee = dell.get()
    connnt = sqlite3.connect('mysq.db')
    cursor = connnt.cursor()
    cursor.execute("DELETE FROM people WHERE name = ?", (dee,))
    connnt.commit()
```

## 사용 방법
1. 'Name'과 'Phone' 칸에 정보를 입력하고 'Submit'을 누릅니다.
2. 'Show'를 누르면 콘솔(터미널)에 현재 저장된 목록이 출력됩니다.
3. 수정이 필요하면 'Update Name'과 'Provide Phone No.'를 입력하고 'Update'를 누릅니다.

## 참고 자료
- [Python Sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [Tkinter Geometry Management: place()](https://tkdocs.com/tutorial/concepts.html#geometry)
