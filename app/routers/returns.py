from fastapi import APIRouter
from app.models import ReturnsRequest
from app.services.transaction_engine import build_transactions
from app.services.interval_engine import apply_q, apply_p, aggregate_k
from app.services.return_engine import calculate_returns

router = APIRouter()

def process_returns(req: ReturnsRequest, mode: str):
    # Step 1: Build transactions
    tx = build_transactions(req.transactions)

    # Sort BEFORE bisect logic
    tx.sort(key=lambda x: x["date"])

    # Totals (PDF requirement)
    transactions_total_amount = sum(t["amount"] for t in tx)
    transactions_total_ceiling = sum(t["ceiling"] for t in tx)

    # Step 2 & 3: Apply q and p
    tx = apply_q(tx, req.q)
    tx = apply_p(tx, req.p)

    # Step 4: Aggregate by k
    grouped = aggregate_k(tx, req.k)

    savings = []

    for g in grouped:
        real, profit, tax = calculate_returns(
            g["amount"],
            req.age,
            req.wage,
            req.inflation,
            mode
        )

        savings.append({
            "start": g["start"].strftime("%Y-%m-%d %H:%M:%S"),
            "end": g["end"].strftime("%Y-%m-%d %H:%M:%S"),
            "amount": g["amount"],
            "profits": profit,
            "taxBenefit": tax if mode == "nps" else 0
        })

    return {
        "transactionsTotalAmount": transactions_total_amount,
        "transactionsTotalCeiling": transactions_total_ceiling,
        "savingsByDates": savings
    }


@router.post("/returns:nps")
def nps(req: ReturnsRequest):
    return process_returns(req, "nps")


@router.post("/returns:index")
def index(req: ReturnsRequest):
    return process_returns(req, "index")