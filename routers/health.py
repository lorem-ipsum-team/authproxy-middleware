from fastapi import APIRouter, Response

router = APIRouter()


@router.get('/health', response_class=Response)
async def health():
    pass
