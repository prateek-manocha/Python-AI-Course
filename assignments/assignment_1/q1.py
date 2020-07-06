#1. Write a function am_gm_hm(x,y) that takes as input two numbers and returns the Arithmetic Mean,
#Geometric Mean and Harmonic mean of the two - in that order. What happens if one of the numbers is 0?

x = input('Enter first number')
y = input('Enter second number')
try:
    x = int(x)
    y = int(y)
except:
    print('Error: Input not an integer')
    exit()

import math

def am_gm_hm(f,s):
    am = (f+s)/2
    gm = math.sqrt(f*s) #gm = (f*s)**(1/2)
    hm = (f*s)/(f+s)
    print('AM:'+str(am))
    print('GM: '+str(gm))
    print('HM: '+str(hm))
    return am, gm, hm

am_gm_hm(x,y)
#print(am[0])
