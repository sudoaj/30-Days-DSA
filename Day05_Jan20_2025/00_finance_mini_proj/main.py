from finance import calculate_monthly_salary, annual_salary_from_monthly, calculate_tax, net_income

if __name__ == "__main__":
    annual_salary = 120000
    monthly_salary = calculate_monthly_salary(annual_salary)
    print(f"Monthly salary: {monthly_salary}")
    print(f"Annual salary: {annual_salary_from_monthly(monthly_salary)}")
    tax_rate = 0.2
    tax = calculate_tax(annual_salary, tax_rate)
    print(f"Tax: {tax}")
    print(f"Net income: {net_income(annual_salary, tax_rate)}")