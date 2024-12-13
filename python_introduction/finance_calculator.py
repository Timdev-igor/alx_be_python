monthly_income = float(input("Enter your monthly income: "))  #  user to enter monthly income 
monthly_expenses = float(input("Enter your total monthly expenses: "))  # user to enter total monthly expenses

# Calculate the user's monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected annual savings with a 5% interest rate
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Print the user's monthly savings and projected annual savings
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")