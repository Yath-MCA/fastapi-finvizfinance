from fastapi import APIRouter

router = APIRouter()

@router.get('/news')
async def get_news():
    return {"message": "News endpoint"}
