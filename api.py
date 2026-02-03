from fastapi import APIRouter, HTTPException
from models import Order, Portfolio, OrderSide, OrderType

router = APIRouter()

# Mock portfolio
portfolio = {"cash": 1000000.0, "positions": {"0005.HK": 1000}, "pnl": 2500.0}

@router.post("/orders")
async def place_order(order: Order):
    if order.qty <= 0:
        raise HTTPException(status_code=400, detail="Invalid quantity")
    
    # Mock matching engine
    filled = min(order.qty, 1000)  # Simplified matching
    
    return {
        "order": order,
        "status": "FILLED",
        "filled_qty": filled,
        "message": f"HSBC order matched on HKEX"
    }

@router.get("/portfolio")
async def get_portfolio() -> Portfolio:
    return Portfolio(**portfolio)

@router.get("/orders")
async def list_orders():
    return [
        {"id": "1", "symbol": "0005.HK", "side": "BUY", "qty": 100, "status": "FILLED"}
    ]
