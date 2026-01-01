from fastapi import APIRouter, Request, HTTPException
from core.config import settings
import urllib.parse
import httpx
from models.oauth import AuthCode

router = APIRouter(prefix="/zoho/oauth", tags=["Zoho OAuth"])


@router.get("/url")
async def get_authorize_url():
    """
    Returns the Zoho OAuth authorization URL
    """

    params = {
        "scope": "ZohoCRM.modules.ALL",
        "client_id": settings.CLIENT_ID,
        "response_type": "code",
        "access_type": "offline",
        "redirect_uri": settings.REDIRECT_URI
    }

    url = f"{settings.AUTH_URL}?{urllib.parse.urlencode(params)}"

    return {"authorize_url": url}


@router.post("/token")
async def exchange_code_for_token(payload: AuthCode):
    async with httpx.AsyncClient() as client:
        res = await client.post(
            settings.TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": settings.CLIENT_ID,
                "client_secret": settings.CLIENT_SECRET,
                "redirect_uri": settings.REDIRECT_URI,
                "code": payload.code
            }
        )

        res.raise_for_status()
        return res.json()
