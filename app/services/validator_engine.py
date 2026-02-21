def validate_transactions(transactions):
    seen = set()
    valid = []
    invalid = []

    for t in transactions:
        if t["amount"] < 0:
            t["message"] = "Negative amounts are not allowed"
            invalid.append(t)
            continue
        if t["date"] in seen:
            t["message"] = "Duplicate transaction"
            invalid.append(t)
            continue
        seen.add(t["date"])
        valid.append(t)

    return {"valid": valid, "invalid": invalid}