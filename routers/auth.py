from fastapi import APIRouter, HTTPException, Query, status
from fastapi.responses import RedirectResponse
from dependencies.keycloak import keycloak_openid
from schema import Tokens
from config import REDIRECT_URI

router = APIRouter(prefix='/auth')


@router.get("/redirect")
async def token():
    auth_url = await keycloak_openid.a_auth_url(redirect_uri=REDIRECT_URI)
    return RedirectResponse(auth_url)


@router.post("/callback", response_model=Tokens)
async def callback(code=Query(...)):
    try:
        tokens = await keycloak_openid.a_token(
            grant_type='authorization_code',
            code=code,
            redirect_uri=REDIRECT_URI
        )

        return tokens
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='authorization code expired')


@router.post("/refresh", response_model=Tokens)
async def refresh(refresh_token=Query(...)):
    try:
        tokens = await keycloak_openid.a_refresh_token(refresh_token)
        return tokens
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='refresh token expired')
