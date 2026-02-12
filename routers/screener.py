from fastapi import APIRouter

router = APIRouter()

@router.get("/screener")
async def get_screener_data():
    return {"message": "Market screener data"}