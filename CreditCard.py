totalPayment =0
month =1
outstandingBal = float (raw_input("Enter the outstanding balance on your credit card: "))
AnnInterestRate = float (raw_input("Enter the annual credit card interest rate as a decimal: "))
minPaymentRate = float (raw_input("Enter the minimum monthly payment rate as a decimal: "))

while month<=12:
  minMonthlyPayment = minPaymentRate * outstandingBal
  interestPaid = (AnnInterestRate/12) * outstandingBal
  outstandingPaid = minMonthlyPayment - interestPaid
  totalPayment += minMonthlyPayment
  outstandingBal -= outstandingPaid
  
  print "\nMONTH: ", month
  print "Minimum monthly payment = ", minMonthlyPayment
  print "Principal paid = ", outstandingPaid
  print "Remaining balance = ", outstandingBal
  month +=1
  
print "\nRESULT: "
print "Total amount paid = ", totalPayment
print "Remaining balance = ", outstandingBal

raw_input("Press Enter key to exit....")
  
  
  
  
