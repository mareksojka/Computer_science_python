# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:49:40 2017

@author: marek
"""


balance = 20000
annualInterestRate=0.1

import math
monthlyInterestRate=annualInterestRate/12.0
monthlyPaymentLowerBound=round(balance/12.0,2)
monthlyPaymentUpperBound=round((balance+balance*math.pow(1+monthlyInterestRate,12))/12.0,2)
monthlyPayment=round((monthlyPaymentLowerBound+monthlyPaymentUpperBound)/2,2)
outstandingBalance=balance
prevcalc=0
while prevcalc!=monthlyPayment:
    prevcalc=monthlyPayment
    outstandingBalance=balance-monthlyPayment
    outstandingBalance+=monthlyInterestRate*outstandingBalance
    for month in range(2,13):
        outstandingBalance=outstandingBalance-monthlyPayment
        print("Monthly Payment", monthlyPayment)    
        print("Balance after",month," payment ",outstandingBalance)
        print("Lower, Upper ",monthlyPaymentLowerBound," ",monthlyPaymentUpperBound)
        outstandingBalance+=monthlyInterestRate*outstandingBalance
        """print("Balance after interest ",outstandingBalance)"""
    outstandingBalance=round(outstandingBalance,2)
    if outstandingBalance<0:
        monthlyPaymentUpperBound=monthlyPayment
    elif outstandingBalance>0:
        monthlyPaymentLowerBound=monthlyPayment
    monthlyPayment=round((monthlyPaymentLowerBound+monthlyPaymentUpperBound)/2,2)

print("Lowest Payment: ", monthlyPayment)