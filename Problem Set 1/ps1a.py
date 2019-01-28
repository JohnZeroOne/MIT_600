# Problem Set 1
# Name: John Smith
# Collaborators: None
# Time Spent: 140

# retrieve user input
outstanding_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))
monthly_rate = float(raw_input("Enter the minimum monthly payment rate as a decimal: "))

# initialiize state variables
interest_paid = 0
min_monthly_pay = 0
principle_paid = 0
month_num = 0
total_paid = 0

# calculate and print every month within a year
while month_num < 12:
    # iterate each month
    month_num += 1
    print "Month:", month_num

    # calculate monthly interest paid
    interest_paid = annual_interest / 12 * outstanding_balance

    # calculate how much to pay each month
    min_monthly_pay = monthly_rate * outstanding_balance
    # sum each month's payment to total 1 year
    total_paid += min_monthly_pay
    print ("Minimum monthly payment: %s%s" % ("$", round(min_monthly_pay, 2)))

    # calculate monthly principle paid
    principle_paid = min_monthly_pay - interest_paid 
    print ("Principle paid: %s%s" % ("$", round(principle_paid, 2)))

    # update the balance after principle is taken
    outstanding_balance -= principle_paid
    print ("Remaining balance: %s%s" % ("$", round(outstanding_balance, 2)))

# show total
print "RESULT"
print ("Total amount paid: %s%s" % ("$", round(total_paid, 2)))
print ("Remaining balance: %s%s" % ("$", round(outstanding_balance, 2)))



