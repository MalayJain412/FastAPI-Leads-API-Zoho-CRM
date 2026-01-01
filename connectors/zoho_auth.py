import httpx
from core.config import settings


async def get_access_token():
    async with httpx.AsyncClient() as client:
        res = await client.post(
            settings.TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "client_id": settings.CLIENT_ID,
                "client_secret": settings.CLIENT_SECRET,
                "refresh_token": settings.REFRESH_TOKEN
            }
        )

        res.raise_for_status()
        return res.json()["access_token"]
