#3. You already know how to calculate factorials from the lecture. Use that function (or better write it again
#yourself) to compute the value of sin(x) according to the Taylor formula upto k terms. Thus your function
#should be calculate_sin(x,k) .

import fact
import math

def sin_calc(x, k=10):
    x = x%math.pi # make the angle between 0 and pi
    sinx = 0
    for l, i in enumerate(range(1,k,2)):
        temp = (((-1)**l)*(x**i))/fact.fact(i)
        #print(temp)
        sinx += temp
    return sinx

#sin_calc(x)
if __name__ == '__main__':
    x = float(input('Enter the number: '))
    print(sin_calc(x))
