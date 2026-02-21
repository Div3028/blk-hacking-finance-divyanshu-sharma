from app.utils.math_utils import round_up_100

def build_transactions(expenses):
    result = []
    for e in expenses:
        ceiling, rem = round_up_100(e.amount)
        result.append({
            "date": e.date,
            "amount": e.amount,
            "ceiling": ceiling,
            "remanent": rem
        })
    return result