# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:44:16 2017

@author: marek
"""

high=100
low=0
guess=50
userinput='a'
print("Please think of a number between 0 and 100!")
while userinput!='c':
    guess=int((high-low)/2)+low
    userinput='a'
    
    while userinput not in ['h','l','c']:
        print ("Is your secret number ",guess,"?")        
        userinput=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
        if userinput not in ['h','l','c']:
            print("Sorry, I did not understand your input.")
    if userinput=='h':
      high=guess
    elif userinput=='l':
        low=guess
    elif userinput=='c':
        print("Game over. Your secret number was: ",guess,"?")