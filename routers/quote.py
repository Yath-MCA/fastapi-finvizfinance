from fastapi import APIRouter

router = APIRouter()

@router.get("/quote/{ticker}")
async def get_stock_quote(ticker: str):
    """
    Retrieve stock quote for a given ticker symbol.
    """
    # Here you would integrate with a stock quote service or database.
    return {"ticker": ticker, "price": 100.0}  # Placeholder value
