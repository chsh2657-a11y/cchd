# 배경음악 생성 에이전트

## 옵션 1 — muapi.ai (Suno 연동), 유료
agents/02-image-video-generation-agent.md에 포함된 muapi CLI의 muapi_audio_create 도구로 Suno 모델을 통해 원하는 분위기의 배경음악을 텍스트 설명만으로 생성할 수 있습니다.

## 옵션 2 — Meta Audiocraft(MusicGen), 무료·로컬 실행
https://github.com/facebookresearch/audiocraft

Meta(구 Facebook) 연구팀이 공개한 오디오 생성 라이브러리로, MusicGen 모델을 이용해 텍스트 설명으로 배경음악을 생성할 수 있습니다. 약 2만 3천 개의 스타를 받았고, API 키가 필요 없으며 로컬 GPU 환경에서 실행합니다(GPU가 없으면 속도가 느립니다).

## 단계별 사용법 (Audiocraft 예시)
1. 저장소를 클론하고 파이썬 환경을 설치합니다 (pip install -e .)
2. 모델을 로드합니다 (musicgen-small, musicgen-medium, musicgen-large 중 선택)
3. 텍스트 프롬프트로 음악을 생성합니다 (예: "미래지향적이고 몽환적인 신스 배경음악, 홀로그램 기술 홍보영상용")
4. 생성된 wav 파일을 영상 합성 단계(MoneyPrinterTurbo의 resource/songs 폴더)에 등록합니다

## 홍보영상 배경음악 톤 제안
공중영상홀로그램 기기의 미래지향적 이미지를 살리기 위해 신스웨이브, 미니멀 일렉트로닉, 잔잔한 앰비언트 계열의 프롬프트를 추천합니다.

## 참고 논문
비전-음악 매칭, 음악 생성 모델 전반에 대한 배경은 papers/references.md의 음악 생성 항목을 참고하세요.

## 필요한 API
- muapi.ai 사용 시: muapi.ai API 키 (유료)
- Audiocraft 사용 시: 없음 (로컬 실행)

발급과 설정 방법은 setup/api-key-setup-guide.md 문서를 참고하세요.
