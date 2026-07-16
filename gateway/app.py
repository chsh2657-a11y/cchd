"""
cchd 통합 게이트웨이 (Unified AI Agent Gateway)
--------------------------------------------------
여러 AI 에이전트(영상 제작, 이미지 생성, TTS, 음악 생성)를
하나의 서버, 하나의 API 주소로 호출할 수 있게 묶어주는 FastAPI 게이트웨이입니다.

실제 생성 작업은 각 백엔드(MoneyPrinterTurbo, Audiocraft, muapi.ai 등)가 수행하며,
이 파일은 요청을 적절한 백엔드로 중계(proxy)하는 역할만 합니다.

사용 전 .env 파일에 필요한 API 키와 백엔드 주소를 설정하세요. (.env.example 참고)

주의: 이 파일은 통합 구조를 보여주는 스캐폴드입니다. MoneyPrinterTurbo 등
백엔드의 실제 API 경로와 응답 형식은 버전에 따라 다를 수 있으므로,
실제 배포 전 각 원본 저장소의 최신 문서를 반드시 확인하세요.
"""

import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="cchd Unified AI Agent Gateway")

MONEYPRINTERTURBO_URL = os.getenv("MONEYPRINTERTURBO_URL", "http://moneyprinterturbo:8080")
AUDIOCRAFT_URL = os.getenv("AUDIOCRAFT_URL", "")
MUAPI_KEY = os.getenv("MUAPI_API_KEY", "")
MUAPI_URL = os.getenv("MUAPI_BASE_URL", "https://api.muapi.ai")


class VideoRequest(BaseModel):
    script: str
    voice_name: str = "ko-KR-SunHiNeural"
    subject: str = "공중영상홀로그램 홍보영상"


class MusicRequest(BaseModel):
    prompt: str
    duration: int = 30


class ImageRequest(BaseModel):
    prompt: str
    style: str = "cinematic product ad"


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/video")
async def create_video(req: VideoRequest):
    """MoneyPrinterTurbo로 대본 -> 영상(이미지+TTS+자막+배경음악 포함) 생성 요청을 전달합니다."""
    payload = {
        "video_subject": req.subject,
        "video_script": req.script,
        "voice_name": req.voice_name,
    }
    async with httpx.AsyncClient(timeout=120) as client:
        try:
            r = await client.post(f"{MONEYPRINTERTURBO_URL}/api/v1/videos", json=payload)
            r.raise_for_status()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=502, detail=f"MoneyPrinterTurbo 호출 실패: {e}")
    return r.json()


@app.get("/api/video/{task_id}")
async def get_video_status(task_id: str):
    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(f"{MONEYPRINTERTURBO_URL}/api/v1/tasks/{task_id}")
    return r.json()


@app.post("/api/music")
async def create_music(req: MusicRequest):
    """AUDIOCRAFT_URL이 설정되어 있으면 자체 서버(Audiocraft)를 사용하고,
    없으면 muapi.ai(Suno 등, 유료)로 요청을 전달합니다."""
    if AUDIOCRAFT_URL:
        async with httpx.AsyncClient(timeout=120) as client:
            r = await client.post(f"{AUDIOCRAFT_URL}/generate", json={"prompt": req.prompt, "duration": req.duration})
        return r.json()

    if not MUAPI_KEY:
        raise HTTPException(status_code=400, detail="AUDIOCRAFT_URL 또는 MUAPI_API_KEY 중 하나를 설정해야 합니다.")

    headers = {"Authorization": f"Bearer {MUAPI_KEY}"}
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(
            f"{MUAPI_URL}/v1/music/generate",
            json={"prompt": req.prompt, "duration": req.duration},
            headers=headers,
        )
    return r.json()


@app.post("/api/image")
async def create_image(req: ImageRequest):
    """muapi.ai(Generative-Media-Skills 기반)로 제품 이미지·시네마틱 컷 생성 요청을 전달합니다."""
    if not MUAPI_KEY:
        raise HTTPException(status_code=400, detail="MUAPI_API_KEY를 설정해야 합니다.")

    headers = {"Authorization": f"Bearer {MUAPI_KEY}"}
    async with httpx.AsyncClient(timeout=120) as client:
        r = await client.post(
            f"{MUAPI_URL}/v1/image/generate",
            json={"prompt": req.prompt, "style": req.style},
            headers=headers,
        )
    return r.json()
