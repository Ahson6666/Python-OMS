from fastapi import FastAPI
from api import router as api_router

app = FastAPI(
    title="OMS - Order Management System", 
    version="1.0.0",
    description="FastAPI trading platform for HK investment banks"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "OMS running! Ready for HKEX trading."}

@app.get("/api/health")
async def health():
    return {"status": "healthy", "oms": "HSBC order matching ready"}
