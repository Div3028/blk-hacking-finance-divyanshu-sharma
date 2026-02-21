from fastapi import FastAPI, Request
import time

from app.routers import transactions, returns, performance
from app.utils.metrics import set_last_execution_time

app = FastAPI()

@app.middleware("http")
async def measure_time(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = (time.time() - start) * 1000
    set_last_execution_time(duration)
    return response

app.include_router(transactions.router, prefix="/blackrock/challenge/v1")
app.include_router(returns.router, prefix="/blackrock/challenge/v1")
app.include_router(performance.router, prefix="/blackrock/challenge/v1")