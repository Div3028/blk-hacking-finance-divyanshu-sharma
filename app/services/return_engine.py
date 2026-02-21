from app.utils.math_utils import compound, inflation_adjust, calculate_tax

def calculate_returns(amount, age, wage, inflation, mode):
    years = max(60 - age, 5)
    annual_income = wage * 12

    if mode == "nps":
        rate = 0.0711
        deduction = min(amount, annual_income * 0.10, 200000)
        tax_benefit = calculate_tax(annual_income) - calculate_tax(annual_income - deduction)
    else:
        rate = 0.1449
        tax_benefit = 0

    future = compound(amount, rate, years)
    real = inflation_adjust(future, inflation/100, years)
    profit = real - amount

    return real, profit, tax_benefit