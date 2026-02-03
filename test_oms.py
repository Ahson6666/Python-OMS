import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert "OMS" in response.json()["status"]

def test_place_order():
    order_data = {
        "id": "test1",
        "symbol": "0005.HK",
        "side": "BUY", 
        "type": "MARKET",
        "qty": 100
    }
    response = client.post("/api/orders", json=order_data)
    assert response.status_code == 200
    assert response.json()["status"] == "FILLED"

def test_portfolio():
    response = client.get("/api/portfolio")
    assert response.status_code == 200
    assert "pnl" in response.json()
