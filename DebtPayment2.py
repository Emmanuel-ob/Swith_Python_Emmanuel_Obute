import math

totalBal = float(raw_input("Enter the outstanding balance on your credit card: "))
interestRate = float(raw_input("Enter the annual credit card interest rate as decimal: "))
totalDue = (totalBal * (1+(interestRate/12))**12)
totalAmount = totalBal 
monthlyInerest = interestRate/12
lowerBound = totalBal/12
upperBound = totalDue/12
monthlyPayment = (lowerBound + upperBound)/2
count = 0

while totalAmount>0:
    count +=1
    totalAmount = totalAmount*(1+monthlyInerest) - monthlyPayment
   

print "\nRESULT"
print "Monthly payment to pay off debt in 1 year = ", monthlyPayment
print "Number of months needed = ", count
print "Balance = ", totalAmount
