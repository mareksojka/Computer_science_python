# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 20:16:56 2017

@author: marek
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    # Your code here
    vowels=[ 'a', 'e', 'i', 'o', 'u','A','E','I','O','U']
    s_without_vowels=''
    for letter in s:
        if letter not in vowels:        
            s_without_vowels=s_without_vowels+letter
    print(s_without_vowels)
    
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    Sorted_list=sorted(L,reverse=True)
    while len(Sorted_list)>0:
        maximum_value_in_list=Sorted_list[0]
        max_value_frequency=Sorted_list.count(maximum_value_in_list)
        if max_value_frequency%2==1:
            return maximum_value_in_list
        else:
            for i in range(max_value_frequency):
                Sorted_list.remove(maximum_value_in_list)
    return None
        
        
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    #YOUR CODE HERE
    inverted_dict={}
    for key in d.keys():
        if d[key] in inverted_dict.keys():
            inverted_dict[d[key]].append(key)
            inverted_dict[d[key]].sort()
        else:
            inverted_dict[d[key]]=[key]
    return inverted_dict
    
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    
    def poly(x):
        expression=0
        for k in range(len(L)):
            
            expression+=L[k]*x**(len(L)-k-1)
            
        return expression
    return poly
    
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    if len(L1)==len(L2):
        frequency_dict={}
        test_value=1  
        for i in range(len(L1)):
            value=L1[i]
            if L1.count(value)==L2.count(value):
                frequency_dict[value]=L1.count(value)
                test_value*=1
            elif L1.count(value)!=L2.count(value):
                return False
        maximum_value_count=0
        maximum_value=None        
        for key in frequency_dict:
            if frequency_dict[key]>maximum_value_count:
                maximum_value_count=frequency_dict[key]
                maximum_value=key
96n        if maximum_value_count==0:
            maximum_value_count=None
        return (maximum_value,maximum_value_count,type(maximum_value))    
        
        
    else:
        return False
