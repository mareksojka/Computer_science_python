

import math

"""
function polysum  computes the sum of are and squared perimiter rounded to four digits.
area computation uses math module to compute tan and pi, and built-in function round to round the result to four digits.
"""
def polysum(n,s):
    perimiter = n*s
    area= 0.25*n*s**2/(math.tan(math.pi/n))
    return round(area+perimiter**2,4)