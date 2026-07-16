# cchd — AI 영상 제작 에이전트 모음

## 프로젝트 소개
이 저장소는 기획안(대본)만 입력하면 이미지, 음성(TTS 내레이션), 배경음악, 최종 영상 합성까지 하나의 흐름으로 자연스럽게 이어지는 영상을 만들기 위한 오픈소스 AI 에이전트와 스킬 파일을 분야별로 정리한 참고 저장소입니다. 특히 공중에 화면이 뜨고 손으로 조작 가능한 공중영상홀로그램 기기의 홍보영상을 제작하는 것을 목표로, 실제 사용 가능한 오픈소스 프로젝트 링크와 사용법, 결과물 품질을 높이기 위한 참고 논문, 필요한 API 설정 방법을 함께 담았습니다.

## 이 저장소의 활용법
1. agents/01 문서를 먼저 확인해 대본 입력만으로 스크립트, 내레이션, 자막, 배경음악, 최종 영상까지 한 번에 만드는 통합형 파이프라인을 로컬에 설치합니다.
2. 홍보영상의 제품 이미지나 시네마틱 컷 품질을 높이고 싶다면 agents/02 문서의 스킬을 함께 사용합니다.
3. 내레이션 음성 품질을 더 자연스럽게 조정하려면 agents/03 문서를 참고합니다.
4. 배경음악을 별도로 만들거나 다양화하려면 agents/04 문서를 참고합니다.
5. 각 에이전트 실행에 필요한 API 키 발급과 설정은 setup/api-key-setup-guide.md 문서를 따라 진행합니다.
6. 결과물의 완성도를 높이기 위한 이론적 배경은 papers/references.md에서 분야별 논문을 확인합니다.

## 폴더 구조
- agents : 분야별 추천 AI 에이전트 설명과 사용법
- papers : 품질 향상을 위한 참고 논문 링크 모음
- setup : 필요한 API 키 발급 및 설정 가이드

## 분야별 에이전트 파일 (발행 주소)
- 통합형 영상 제작 에이전트 (MoneyPrinterTurbo) : https://github.com/chsh2657-a11y/cchd/blob/chhc/agents/01-integrated-video-agent-moneyprinterturbo.md
- 이미지·영상 생성 특화 에이전트 (Generative-Media-Skills) : https://github.com/chsh2657-a11y/cchd/blob/chhc/agents/02-image-video-generation-agent.md
- 음성(TTS·내레이션) 에이전트 안내 : https://github.com/chsh2657-a11y/cchd/blob/chhc/agents/03-tts-voice-agent.md
- 배경음악 생성 에이전트 안내 : https://github.com/chsh2657-a11y/cchd/blob/chhc/agents/04-music-generation-agent.md
- 참고 논문 모음 : https://github.com/chsh2657-a11y/cchd/blob/chhc/papers/references.md
- API 키 설정 가이드 : https://github.com/chsh2657-a11y/cchd/blob/chhc/setup/api-key-setup-guide.md

## 원본 오픈소스 프로젝트 (참고용 원저작자 주소)
- https://github.com/harry0703/MoneyPrinterTurbo
- https://github.com/SamurAIGPT/Generative-Media-Skills
- https://github.com/facebookresearch/audiocraft
- https://github.com/responsivevoice/skills
- https://github.com/hudeven/chichi-speech

## 공중영상홀로그램 홍보영상 제작 시 권장 조합
제품 사진이나 데모 영상을 로컬 소재로 준비한 뒤, MoneyPrinterTurbo에 직접 작성한 홍보 대본을 입력하고, 더 고급스러운 제품 컷이 필요하면 Generative-Media-Skills의 시네마틱 제품광고·드론뷰 스킬을 보조적으로 활용하는 방식을 권장합니다. 배경음악은 미래지향적인 신스웨이브나 미니멀 일렉트로닉 계열의 프롬프트를 사용하는 것이 제품 이미지와 잘 어울립니다.

## 주의사항
- 실제 API 키, 토큰 등 민감한 값은 이 저장소에 절대 커밋하지 마세요. 로컬 환경변수나 설정 파일에만 보관하세요.
- 각 문서에 소개된 원본 오픈소스 프로젝트는 각자의 라이선스를 따릅니다. 실제 사용 전 라이선스를 직접 확인하세요.
- 이 저장소의 문서는 각 프로젝트의 README를 참고해 요약, 정리한 것으로 원문 전체를 복제하지 않았습니다. 최신 사용법은 각 원본 저장소를 확인하세요.
