from math import ceil

def round_up_100(amount: float):
    ceiling = ceil(amount / 100) * 100
    return ceiling, ceiling - amount

def compound(P, r, years):
    return P * ((1 + r) ** years)

def inflation_adjust(A, inflation, years):
    return A / ((1 + inflation) ** years)

def calculate_tax(income):
    tax = 0
    slabs = [
        (700000, 0),
        (1000000, 0.10),
        (1200000, 0.15),
        (1500000, 0.20),
        (float("inf"), 0.30)
    ]
    prev = 700000
    if income <= 700000:
        return 0
    for limit, rate in slabs[1:]:
        if income > prev:
            taxable = min(income, limit) - prev
            tax += taxable * rate
            prev = limit
    return tax