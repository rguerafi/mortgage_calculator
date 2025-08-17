# this file contains the utility functions used for calculations and UI
import pandas as pd

# -------------------------------
# Mortgage calculation
# -------------------------------
def mortgage_analysis(total_cost, interest_rate, down_payment, initial_tilgung, years_fixed, yearly_extra=0):
    loan_amount = total_cost - down_payment
    r = interest_rate / 100
    t = initial_tilgung / 100
    annuity_rate = r + t
    monthly_payment = loan_amount * annuity_rate / 12
    balance = loan_amount
    total_interest = 0
    schedule = []

    for year in range(1, years_fixed + 1):
        for month in range(1, 13):
            interest_payment = balance * r / 12
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            total_interest += interest_payment
            schedule.append({
                "Month": (year - 1) * 12 + month,
                "Principal Part": principal_payment,
                "Interest Part": interest_payment,
                "Total Interest Paid": total_interest,
                "Remaining Debt": max(balance, 0),
            })
        if yearly_extra > 0:
            balance -= yearly_extra
            if balance < 0:
                balance = 0
        if balance <= 0:
            break

    return monthly_payment, pd.DataFrame(schedule), balance
