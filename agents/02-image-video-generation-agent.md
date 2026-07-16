# 이미지·영상 생성 특화 에이전트 — Generative-Media-Skills

## 원본 저장소
https://github.com/SamurAIGPT/Generative-Media-Skills

## 개요
Claude Code, Cursor, Gemini CLI 등에서 바로 사용할 수 있는 SKILL.md 모음으로, muapi.ai API를 통해 Midjourney v7, Flux, Kling, Veo3, Seedance 2.0 등 100개 이상의 모델에 접근해 고품질 이미지·영상·오디오를 생성합니다. 약 3.8천 개의 스타를 받았고 MIT 라이선스로 배포됩니다.

## 홍보영상 제작에 유용한 스킬
- Cinematic Product Ad — 제품 사진 한 장으로 5~10초 시네마틱 광고 영상 제작
- Product Video Ad Maker — 제품 사진 기반 고급 시네마틱 영상 광고
- Drone-Style Video — 버드아이·궤도샷·플라이오버 등 공중 시점 영상, 공중에 뜨는 화면 컨셉 표현에 활용 가능
- Multi-Angle Shots — 제품을 다양한 각도에서 촬영한 것 같은 이미지 세트 생성
- Logo + Branding Package — 브랜드 로고 및 아이덴티티 생성

## 단계별 사용법
1. muapi CLI 설치: npm install -g muapi-cli
2. API 키 설정: muapi auth configure
3. 스킬 설치: npx skills add SamurAIGPT/Generative-Media-Skills --all
4. 원하는 레시피 스킬의 스크립트 실행 (예: library/motion/cinema-director/scripts/generate-film.sh)
5. --view 옵션으로 결과 미리보기 후 필요 시 스타일·길이·카메라 무빙 등 파라미터를 조정해 재생성

## agents/01(MoneyPrinterTurbo)과 함께 쓰는 법
이 에이전트로 만든 고품질 제품 이미지·영상 클립을 MoneyPrinterTurbo의 로컬 소재 폴더에 넣으면, 통합 파이프라인이 내레이션·자막·배경음악과 자연스럽게 합쳐 최종 홍보영상을 완성합니다.

## 필요한 API
- muapi.ai API 키(유료, 크레딧 기반 과금) — https://muapi.ai/dashboard

발급과 설정 방법은 setup/api-key-setup-guide.md 문서를 참고하세요.

## 라이선스
MIT
