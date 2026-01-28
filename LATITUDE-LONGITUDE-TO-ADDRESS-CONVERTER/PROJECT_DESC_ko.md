# LATITUDE-LONGITUDE-TO-ADDRESS-CONVERTER (좌표-주소 변환기)

이 프로젝트는 위도(Latitude)와 경도(Longitude) 좌표를 입력받아 해당 위치의 실제 도로명 주소를 찾아주는 Django 기반 웹 애플리케이션입니다.

## 주요 특징
- **역지오코딩(Reverse Geocoding)**: 위경도 좌표를 사용하여 전 세계 어디든 주소를 찾아주는 기술을 구현했습니다.
- **Geopy 라이브러리 활용**: 다양한 위치 기반 서비스를 제공하는 `geopy` 라이브러리의 `Nominatim` 엔진을 사용합니다.
- **사용자 친화적인 인터페이스**: 위도와 경도를 입력하고 주소를 즉시 확인할 수 있는 간단하고 직관적인 웹 폼을 제공합니다.

## 코드 설명
애플리케이션의 핵심 기능을 담당하는 코드의 일부입니다.

### 1. 주소 변환 클래스 (`app/latLongToAddressConverter.py`)
`geopy`의 `Nominatim`을 초기화하고 좌표를 주소로 변환하는 기능을 수행합니다.
```python
from geopy.geocoders import Nominatim

class AddressConverter:
    def findAddress(self, lat, lon):
        geolocator = Nominatim(user_agent="App", timeout=100)
        s = f"{lat},{lon}"
        try:
            location = geolocator.reverse(s)
            return location.address if location else "Location's Street Address Not Found!"
        except ValueError as e:
            return e
```

### 2. Django 뷰 처리 (`app/views.py`)
사용자의 POST 요청에서 좌표를 받아 변환기에 전달하고 결과를 화면으로 다시 보냅니다.
```python
from app.latLongToAddressConverter import AddressConverter

def index(request):
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
        addressConverter = AddressConverter()
        streetAddress = addressConverter.findAddress(lat, lon)
        context = {'streetAddress': streetAddress, 'lat': lat, 'lon': lon}
        return render(request, 'app/index.html', context)
    return render(request, 'app/index.html')
```

## 참고 자료
- [GeoPy Documentation](https://geopy.readthedocs.io/)
- [Nominatim OpenStreetMap Wiki](https://wiki.openstreetmap.org/wiki/Nominatim)
- [Django Documentation](https://docs.djangoproject.com/)
