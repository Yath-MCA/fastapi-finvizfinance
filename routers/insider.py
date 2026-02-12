from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/insider-trading/{ticker}")
async def get_insider_trading(ticker: str):
    # Placeholder for actual insider trading data retrieval logic
    # Example response structure
    example_response = {
        "ticker": ticker,
        "insider_trades": [
            {
                "name": "John Doe",
                "position": "CEO",
                "trade_date": "2026-02-10",
                "transaction_type": "buy",
                "shares": 1000,
                "price_per_share": 50.0
            }
        ]
    }
    return example_response
