def calculate_tax(income, tax_rate):
    """Calculate tax based on income and tax rate."""
    return income * tax_rate
def net_income(income, tax_rate):
    """Calculate net income based on income and tax rate."""
    return income - calculate_tax(income, tax_rate)