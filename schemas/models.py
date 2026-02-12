from pydantic import BaseModel

class Stock(BaseModel):
    symbol: str
    name: str
    price: float
    change: float
    percentage_change: float
    volume: int

class StockList(BaseModel):
    stocks: list[Stock]