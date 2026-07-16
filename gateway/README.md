# cchd 통합 게이트웨이 (gateway)

## 이게 뭔가요?

이 폴더는 agents/ 문서에서 소개한 여러 에이전트(MoneyPrinterTurbo, Audiocraft, muapi.ai 등)를 각각 따로 등록·호출하지 않고, 하나의 서버 · 하나의 API 주소로 묶어서 쓸 수 있게 만든 실행 가능한 코드입니다. 지금 개발 중인 프로젝트에서는 이 gateway 서버의 주소 하나만 등록하면 영상·이미지·음악 생성 기능을 모두 사용할 수 있도록 설계했습니다.

## 구성 파일

- app.py : 통합 API 서버(FastAPI). /api/video, /api/music 등 단일 엔드포인트를 제공하고, 내부적으로 각 백엔드(MoneyPrinterTurbo, Audiocraft, muapi.ai)로 요청을 중계합니다.
- Dockerfile : gateway 서버를 위한 컨테이너 이미지 정의
- docker-compose.yml : MoneyPrinterTurbo + gateway + nginx(리버스 프록시)를 한 번에 실행하는 설정
- nginx.conf : 하나의 도메인·포트(80번)에서 /api/ 요청은 gateway로, 나머지는 MoneyPrinterTurbo 웹UI로 라우팅
- requirements.txt : gateway 서버 실행에 필요한 Python 패키지 목록
- .env.example : 필요한 모든 API 키를 한 곳에 모아 놓은 예시 파일 (실제 값은 .env 파일에만 입력하고 git에는 절대 커밋하지 않습니다)

## 사용법 (내 서버에 배포하기)

1. 서버(SSH로 접속 가능한 VPS, 클라우드 인스턴스 등)에서 이 저장소를 git clone 합니다.
2. gateway 폴더의 .env.example을 복사해 .env 파일을 만들고 실제 API 키를 입력합니다.
3. gateway 폴더에서 docker-compose up -d --build 를 실행합니다.
4. 서버의 IP 또는 도메인 주소 하나로 접속합니다: http://내서버주소/ (MoneyPrinterTurbo 웹UI), http://내서버주소/api/video (통합 API).
5. 개발 중인 프로젝트에서는 이 하나의 주소(http://내서버주소/api/...)만 등록해서 호출하면 됩니다.

## API 예시

```
curl -X POST http://내서버주소/api/video \
  -H "Content-Type: application/json" \
  -d '{"script": "공중영상홀로그램 홍보 대본...", "subject": "공중영상홀로그램"}'
```

## 주의사항

- 이 코드는 뼈대(스캐폴드) 수준의 예시입니다. MoneyPrinterTurbo의 실제 API 경로·응답 형식은 버전에 따라 달라질 수 있으므로, 실제 배포 전 원본 저장소(harry0703/MoneyPrinterTurbo)의 최신 API 문서를 다시 확인하세요.
- .env 파일과 실제 API 키·토큰은 절대 GitHub에 커밋하지 마세요.
- 실제 도메인을 연결하려면 nginx.conf의 server_name을 원하는 도메인으로 바꾸고, HTTPS(Let's Encrypt 등) 설정을 추가로 진행하는 것을 권장합니다.
