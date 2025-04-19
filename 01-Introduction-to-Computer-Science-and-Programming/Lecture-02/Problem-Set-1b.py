# Calculating the months needed for a down payment - including with a 6 months salary raise

# Getting user input needed for calculation
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:  "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Constants
portion_down_payment = 0.25
amount_saved = 0
r = 0.05

# Calculating the coast of a down payment and the monthly salary
total_down_payment = cost_of_dream_home * portion_down_payment

# Looping through each month and checking if the amount saved is enough for a down payment
months = 0

while True:
    if amount_saved >= total_down_payment:
        print(f"Number of months: {months}")
        break

    months += 1

    amount_saved += amount_saved * (r / 12)
    amount_saved += (yearly_salary / 12) * portion_saved

    # Adding semi-annual raise
    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise
