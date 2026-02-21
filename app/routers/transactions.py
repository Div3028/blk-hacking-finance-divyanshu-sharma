from fastapi import APIRouter
from app.models import Expense, ValidatorRequest
from app.services.transaction_engine import build_transactions
from app.services.validator_engine import validate_transactions
from app.models import FilterRequest


router = APIRouter()

@router.post("/transactions:parse")
def parse(expenses: list[Expense]):
    return build_transactions(expenses)

@router.post("/transactions:validator")
def validator(req: ValidatorRequest):
    return validate_transactions([t.dict() for t in req.transactions])

@router.post("/transactions:filter")
def filter_transactions(req: FilterRequest):
    valid = []
    invalid = []

    for t in req.transactions:
        if t.remanent < 0:
            invalid.append({**t.dict(), "message": "Negative remanent"})
        else:
            valid.append(t)

    return {
        "valid": valid,
        "invalid": invalid
    }
