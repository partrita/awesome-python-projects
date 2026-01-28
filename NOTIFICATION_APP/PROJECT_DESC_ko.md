# NOTIFICATION_APP (데스크탑 알림 애플리케이션)

이 프로젝트는 파이썬의 `plyer` 라이브러리를 사용하여 사용자의 데스크탑이나 노트북 화면에 시스템 알림을 표시하는 간단한 도구입니다.

## 주요 특징
- **간편한 알림 설정**: `plyer.notification`을 사용하여 제목(Title), 내용(Message), 그리고 알림이 표시될 시간(Timeout)을 쉽게 설정할 수 있습니다.
- **크로스 플랫폼 지원**: `plyer` 라이브러리는 Windows, macOS, Linux 등 다양한 운영체제에서 알림 기능을 지원합니다.

## 코드 설명
알림을 생성하는 코드는 다음과 같이 매우 간단합니다.

```python
from plyer import notification

# 데스크탑 알림 실행
notification.notify(
    title = "e-mail notification", # 알림 제목
    message = "you have 3 unread messages", # 알림 내용
    timeout = 10, # 알림이 표시되는 시간(초)
)
```

## 참고 자료
- [Plyer Documentation](https://plyer.readthedocs.io/en/latest/)
- [Plyer GitHub Repository](https://github.com/kivy/plyer)
