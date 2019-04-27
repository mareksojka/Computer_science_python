# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:25:36 2017

@author: marek
"""
import math

balance = 3926
annualInterestRate=0.2

monthlyInterestRate=annualInterestRate/12.0
monthlyPayment=10
outstandingBalance=balance
while outstandingBalance>0:
    outstandingBalance=balance-monthlyPayment
    outstandingBalance+=monthlyInterestRate*outstandingBalance
    for month in range(1,12):
         
        outstandingBalance=outstandingBalance-monthlyPayment
        print("Minimum Payment", monthlyPayment)    
        print("Balance after",month," payment ",outstandingBalance)
        print("Interest ",monthlyInterestRate*outstandingBalance) 
        outstandingBalance+=monthlyInterestRate*outstandingBalance
        print("Balance after interest ",outstandingBalance)
    monthlyPayment+=10

print("Lowest Payment: ", monthlyPayment-10)






"""

FixedRatePayment=balance*monthlyInterestRate/(1-math.pow((1+monthlyInterestRate),-12))
FixedRatePayment=round((FixedRatePayment+5)/10)*10
"""