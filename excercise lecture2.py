# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 20:33:05 2017

@author: marek
"""

x = 23
epsilon = 0.1
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    print(guess**2-x)    
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print(guess**2)
    print('failed')
else:
    print('succeeded: ' + str(guess))