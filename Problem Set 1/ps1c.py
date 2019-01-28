# Problem Set 3
# Name: John Smith
# Collaborators: None
# Time Spent: 180
#
# Use bisection search to find the smallest monthly payment to pay a debt within 1 year
#
# had to use examples to implement bisection search while accounting for interest rate
#
# retrieve user input
initial_balance = float(raw_input("Enter the outstanding balance on your credit card: "))
annual_interest = float(raw_input("Enter the annual credit card interest rate as a decimal: "))

# initialiize state variables
monthly_interest = annual_interest / 12.0

# lowest possible answer
low = initial_balance / 12.0
# highest possible answer
high = (initial_balance * (1 + (annual_interest / 12.0)) ** 12.0) / 12.0
# find the middle
mid = (low + high) / 2.0

balance = initial_balance
#print "low = ", low, "mid = ", mid, "high = ", high

# bisection search
# loop until the balance is solved
while balance > 0:

    balance = initial_balance

    # iterate once for every month
    for months in range (0, 13):

        balance += balance * monthly_interest
        balance -= mid
       # print "for, mid", mid
       # print "balance = ", balance

        # answer is not between low and mid
        # remove low
        if balance > 0:
            low = mid
            #print "if, mid", mid
            #print "balance = ", balance
        else:
            high = mid
            #print "else, mid", mid
           # print "balance = ", balance
        # set mid with new values
        mid = (low + high) / 2.0
        
#print mid
    
            
# show total
print "RESULT"
print ("Monthly payment to pay off debt in 1 year: %s%s" % ("$", round(mid, 2)))
print "Number of months needed: ", months
# needs work
print ("Balance: %s%s" % ("$", round(initial_balance - balance, 2)))
