"""
Arthur Gramlich
Data Structures Section 1
August 9th, 2024
"""

#Initial Pay Rates
HourRate = 20
CommissionRate = 0.10

#Individual's Information
while True:
    try:
        HoursWorked = float(input("Enter how many hours you worked this week. "))
        break
    except ValueError:
        print ("Please enter value as a number.")
        
while True:
    try:
        WeeklySales = float(input("Enter your total weekly sales for the week. "))
        break
    except ValueError:
        print ("Please enter value as a number.")

# Calculation
HourlyPay = HourRate * HoursWorked
CommissionPay = CommissionRate * WeeklySales
WeeklyPay = HourlyPay + CommissionPay

print ("You worked", HoursWorked, "hours this week.", "Your hourly pay is $", HourRate, ". Your commission pay this week is $", CommissionPay, ". Your total pay for the week is $", WeeklyPay, ".");
