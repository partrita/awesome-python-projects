# File Rename Tool (파일 이름 변경 도구)

이 프로젝트는 지정된 디렉토리 내의 모든 파일 이름을 일정한 규칙(접두사 + 일련번호)에 맞게 일괄적으로 변경해 주는 간단하면서도 강력한 파이썬 스크립트입니다. 많은 양의 이미지나 데이터를 정리할 때 유용합니다.

## 주요 기능
- **일괄 변경**: 수많은 파일의 이름을 한 번에 변경합니다.
- **접두사(Prefix) 설정**: 사용자가 원하는 단어를 접두사로 설정할 수 있습니다.
- **확장자 유지**: 파일의 원래 확장자를 자동으로 인식하여 유지합니다.
- **일련번호 부여**: 파일마다 1부터 시작하는 번호를 자동으로 붙여줍니다.

## 코드 설명

### 1. 사용자 입력 및 파일 순회
파일 이름 앞에 붙일 접두사를 입력받고, `sys.argv[1]`로 전달된 경로 안의 파일들을 하나씩 처리합니다.

```python
import os
import sys

# 접두사 입력 (예: photo -> photo-1.jpg, photo-2.jpg ...)
prefix = input("Enter the Prefix- you want to use... \n")

# 지정된 경로의 파일 목록을 순회
for count, file in enumerate(os.listdir(sys.argv[1])):
    # ...
```

### 2. 확장 추출 및 새 이름 생성
파일 이름에서 확장자를 분리하고, 새로운 이름 규칙을 적용합니다.

```python
    # 확장자 분리
    extnsn = file.split('.')[-1]
    
    # 새 파일 이름 생성 (접두사-번호.확장자)
    new_file = f"{prefix}-{count+1}.{extnsn}"
```

### 3. 실제 이름 변경 실행
`os.rename` 함수를 사용하여 원본 경로(`src`)에서 대상 경로(`dst`)로 이름을 변경합니다.

```python
    src = sys.argv[1] + file
    dst = sys.argv[1] + new_file
    os.rename(src, dst)
```

## 사용 방법
터미널에서 다음과 같이 실행합니다:
```bash
python main.py /path/to/your/files/
```
(폴더 경로 끝에 `/`를 포함해야 정확히 작동합니다.)

## 참고 자료
- [Python os.rename() Documentation](https://docs.python.org/3/library/os.html#os.rename)
- [Python enumerate() Function](https://docs.python.org/3/library/functions.html#enumerate)
