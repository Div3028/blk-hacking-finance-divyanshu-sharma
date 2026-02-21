from fastapi import APIRouter
from app.utils.metrics import performance_report
import time

router = APIRouter()

@router.get("/performance")
def performance():
    return performance_report()