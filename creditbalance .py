# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 14:16:59 2017

@author: marek
"""

balance = 5000
annualInterestRate=0.18
monthlyPaymentRate =0.02


monthlyInterestRate=annualInterestRate/12.0
minimumMonthlyPayment=monthlyPaymentRate*balance
outstandingBalance=balance-minimumMonthlyPayment
print("Balance ",outstandingBalance)
print("Minimum Payment", minimumMonthlyPayment)
outstandingBalance+=monthlyInterestRate*outstandingBalance
for month in range(1,12):
    minimumMonthlyPayment=monthlyPaymentRate*outstandingBalance 
    outstandingBalance=outstandingBalance-minimumMonthlyPayment
    print("Minimum Payment", minimumMonthlyPayment)    
    print("Balance after",month," payment ",outstandingBalance)
    print("Interest ",monthlyInterestRate*outstandingBalance) 
    outstandingBalance+=monthlyInterestRate*outstandingBalance
    print("Balance after interest ",outstandingBalance)
    
print("Remaining balance: ",round(outstandingBalance,2))

