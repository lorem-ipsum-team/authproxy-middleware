from fastapi import APIRouter, Request, Response, HTTPException, status
from dependencies.keycloak import keycloak_openid

router = APIRouter()


@router.get('/{reqpath:path}', response_class=Response)
@router.post('/{reqpath:path}', response_class=Response)
@router.put('/{reqpath:path}', response_class=Response)
@router.patch('/{reqpath:path}', response_class=Response)
@router.options('/{reqpath:path}', response_class=Response)
async def check_auth(request: Request):
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    authorize_header = request.headers.get('authorization', None)

    if not authorize_header:
        return

    schema, token = authorize_header.split(maxsplit=1)

    if schema != 'Bearer':
        raise exception

    try:
        await keycloak_openid.a_decode_token(token, validate=True)
    except:
        raise exception
