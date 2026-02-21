from bisect import bisect_left, bisect_right

def apply_q(transactions, q_periods):
    sorted_q = sorted(
        enumerate(q_periods),
        key=lambda x: (-x[1].start.timestamp(), x[0])
    )
    dates = [t["date"] for t in transactions]

    for _, q in sorted_q:
        left = bisect_left(dates, q.start)
        right = bisect_right(dates, q.end)
        for i in range(left, right):
            if not transactions[i].get("q_applied"):
                transactions[i]["remanent"] = q.fixed
                transactions[i]["q_applied"] = True
    return transactions

def apply_p(transactions, p_periods):
    dates = [t["date"] for t in transactions]
    for p in p_periods:
        left = bisect_left(dates, p.start)
        right = bisect_right(dates, p.end)
        for i in range(left, right):
            transactions[i]["remanent"] += p.extra
    return transactions

def aggregate_k(transactions, k_periods):
    transactions.sort(key=lambda x: x["date"])
    dates = [t["date"] for t in transactions]

    prefix = [0]
    for t in transactions:
        prefix.append(prefix[-1] + t["remanent"])

    result = []
    for k in k_periods:
        left = bisect_left(dates, k.start)
        right = bisect_right(dates, k.end)
        amount = prefix[right] - prefix[left]
        result.append({
            "start": k.start,
            "end": k.end,
            "amount": amount
        })
    return result