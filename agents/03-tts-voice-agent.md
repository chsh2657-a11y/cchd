# 음성(TTS·내레이션) 에이전트 안내

## 결론
현재 GitHub에는 TTS만 전문으로 다루는 독립 AI 에이전트 스킬 중 검증된 대형 프로젝트가 많지 않습니다. 따라서 agents/01-integrated-video-agent-moneyprinterturbo.md에 내장된 TTS 기능을 기본으로 사용하는 것을 권장합니다.

## MoneyPrinterTurbo 내장 TTS 옵션
- Edge TTS — 무료, API 키 불필요, 기본값
- Azure TTS V2, SiliconFlow, Google Gemini TTS, 소형 MiMo TTS — 각각 해당 플랫폼 API 키 필요
- ElevenLabs — 가장 자연스러운 음성 품질, 유료, 다국어 지원
- Chatterbox — 자체 호스팅 가능한 오픈소스 TTS

## 참고할 수 있는 소규모 대안 (검증 필요)
- https://github.com/responsivevoice/skills — ResponsiveVoice TTS API용 코딩 에이전트 스킬
- https://github.com/hudeven/chichi-speech — qwen3-tts 모델 기반 REST API·CLI, AI 에이전트 스킬로 사용 가능

두 프로젝트 모두 스타 수가 매우 적어 안정성이 충분히 검증되지 않았으니 직접 테스트 후 사용을 권장합니다.

## 자연스러운 음성을 위한 설정 팁
- 문장 단위로 대본을 나누고 마침표와 쉼표를 명확히 표기하면 TTS의 억양이 더 자연스러워집니다.
- 제품명이나 전문 용어는 발음 커스터마이징(SSML 또는 발음 사전) 기능이 있는 제공자를 사용하는 것이 좋습니다.
- 내레이션 트랙과 배경음악 트랙의 볼륨을 각각 따로 조정해 대사가 음악에 묻히지 않도록 합니다(MoneyPrinterTurbo에서 지원).

## 참고 논문
음성 합성의 자연스러움·표현력에 대한 이론적 배경은 papers/references.md의 TTS 항목을 참고하세요.

## 필요한 API
- 무료: Edge TTS (키 불필요)
- 유료(고품질): ElevenLabs, Azure Speech, Google Gemini TTS

발급과 설정 방법은 setup/api-key-setup-guide.md 문서를 참고하세요.
