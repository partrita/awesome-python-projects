# Contact Manager App with Django (장고 기반 연락처 관리 앱)

이 프로젝트는 파이썬의 대표적인 웹 프레임워크인 `Django`를 사용하여 웹 기반으로 연락처를 관리하는 애플리케이션입니다. 사용자 인증, 검색, 성별 필터링 등 실무적인 웹 서비스 기능을 포함하고 있습니다.

## 주요 기능
- **사용자 인증**: 회원가입, 로그인 기능을 통해 개인별 연락처 목록을 관리합니다.
- **연락처 검색**: 이름이나 번호로 저장된 연락처를 빠르게 찾을 수 있습니다.
- **실시간 관리자 업데이트**: 장고의 Admin 패널을 통해 데이터를 실시간으로 관리할 수 있습니다.
- **성별 필터링**: 등록된 연락처를 성별에 따라 나누어 볼 수 있습니다.
- **프로필 이미지**: 연락처마다 사진을 업로드하고 관리할 수 있습니다.

## 코드 및 프로젝트 구조 설명

### 1. 모델 설정 (models.py)
연락처 정보를 저장하기 위한 데이터 구조를 정의합니다. 이름, 전화번호, 이메일, 성별, 프로필 이미지 등을 포함합니다.

```python
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female')))
    image = models.ImageField(upload_to='images/', blank=True)
    # ...
```

### 2. 검색 및 필터링 기능
`Django ORM`의 `filter` 기능을 사용하여 검색어와 성별에 맞는 데이터를 추출합니다.

```python
def search(request):
    if request.method == 'POST':
        search_str = request.POST.get('search')
        contacts = Contact.objects.filter(name__icontains=search_str)
        return render(request, 'index.html', {'contacts': contacts})
```

## 실행 방법
1. 저장소를 클론하고 해당 폴더로 이동합니다.
2. `pip install -r requirements.txt`로 필요한 패키지를 설치합니다.
3. 데이터베이스 정보를 생성합니다: `python manage.py migrate`
4. 서버를 실행합니다: `python manage.py runserver`
5. 웹 브라우저에서 `127.0.0.1:8000`에 접속합니다.

## 참고 자료
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Girls Tutorial (Korean)](https://tutorial.djangogirls.org/ko/)
