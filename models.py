from pydantic import BaseModel
from typing import Optional
from enum import Enum

class OrderSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderType(str, Enum):
    MARKET = "MARKET"
    LIMIT = "LIMIT"

class Order(BaseModel):
    id: str
    symbol: str  # "0005.HK" (HSBC)
    side: OrderSide
    type: OrderType
    qty: int
    price: Optional[float] = None

class Portfolio(BaseModel):
    cash: float
    positions: dict[str, float]
    pnl: float
