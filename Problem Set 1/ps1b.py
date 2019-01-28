# Problem Set 2
# Name: John Smith
# Collaborators: None
# Time Spent: 120
#
# Had to use solution, couldn't get it to work for large numbers
# Couldn't figure out how to increment monthly_guess outside of the 12 iteration loop
# Didn't feel the course material had taught enough to complete this problem

# retrieve user input
initial_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# initialiize state variables
monthly_guess = 0
monthly_interest = annual_interest / 12.0
balance = initial_balance

while balance > 0:
    
    monthly_guess += 10
    balance = initial_balance
    months = 0
    
    while months < 12 and balance > 0:
        
        months += 1

        interest = monthly_interest * balance
        
        balance -= monthly_guess

        balance += interest
        
# show total
print "RESULT"
print ("Monthly payment to pay off debt in 1 year: %s%s" % ("$", round(monthly_guess, 2)))
print "Number of months needed: ", months
print ("Balance: %s%s" % ("$", round(balance, 2)))



## doesn't account for compounding monthly interest
##total = outstanding_balance + outstanding_balance * annual_interest
##monthly_total = total / 12
##print monthly_total

### guess rate
##while (monthly_guess * 12 < outstanding_balance + annual_interest * outstanding_balance):
##    # not working for large values
##    # not compounding monthly interest
##    monthly_guess += 10
##    months += 1
