#User Input for Financial Details
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your monthly expenses:"))

#Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

#Project Annual Savings
#annual interest rate of 5%
#Projected savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Output Results
#user’s monthly savings
print("Your monthly savings are $",monthly_savings)
#projected annual savings after including interest
print("Projected savings after one year, with interest, is: $",projected_savings)
