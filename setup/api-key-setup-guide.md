# API 키 설정 가이드

이 문서는 agents 폴더의 각 에이전트를 실제로 사용할 때 필요한 API 키를 어디서 발급받고 어떻게 설정하는지 설명합니다. 실제 키 값은 이 문서나 저장소 어디에도 절대 넣지 마세요. 로컬 환경변수(.env) 또는 각 프로젝트의 설정 파일(예: config.toml)에만 보관하세요.

## 1. LLM API (MoneyPrinterTurbo의 스크립트 생성용, 택1)
- OpenAI: https://platform.openai.com/api-keys 에서 로그인 후 발급
- Google Gemini: https://aistudio.google.com/apikey 에서 로그인 후 발급
- DeepSeek: https://platform.deepseek.com 에서 로그인 후 발급
설정 방법: MoneyPrinterTurbo WebUI의 기본 설정(Basic Settings) 화면에서 Provider 선택 후 키를 입력하거나, config.toml의 해당 provider 항목에 입력합니다.

## 2. Pexels API (영상·이미지 소재, 선택 사항)
- https://www.pexels.com/api/ 에서 무료 계정 생성 후 발급
- 자신의 제품 사진·영상만 사용할 경우 이 키는 필요하지 않습니다.

## 3. ElevenLabs API (고품질 TTS, 선택 사항)
- https://elevenlabs.io 가입 후 프로필의 API Keys 메뉴에서 발급
- MoneyPrinterTurbo WebUI의 음성 설정(Voice Settings)에서 Provider를 ElevenLabs로 선택하고 키를 입력합니다.

## 4. muapi.ai API (이미지·영상·음악 생성 에이전트용)
- https://muapi.ai/dashboard 가입 후 대시보드에서 발급
- 터미널에서 muapi auth configure 명령으로 키를 등록합니다.
- 크레딧을 충전해야 실제 생성이 가능한 유료 서비스입니다. 사용 전 요금제를 확인하세요.

## 5. Azure Speech / Google Gemini TTS (선택 사항)
- Azure: https://portal.azure.com 에서 Speech 리소스를 생성한 뒤 키와 지역 정보를 확인
- Google Gemini TTS: https://aistudio.google.com/apikey 에서 발급한 키를 그대로 사용

## 키 보관 원칙
1. 모든 키는 .env 또는 config.toml 같은 로컬 파일에만 저장합니다.
2. .gitignore에 config.toml, .env를 반드시 포함시켜 실수로 커밋되지 않도록 합니다.
3. 이 저장소(cchd)에는 설명 문서만 두고, 실제 키나 토큰은 절대 포함하지 않습니다.
4. 키가 노출되었다면 즉시 해당 서비스 대시보드에서 재발급(rotate)하세요.
