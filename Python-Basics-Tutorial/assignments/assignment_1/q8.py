'''8. Write a function to print only odd numbers in the range(a,b). Write it two times - once with a for loop
( print_odd_for(a,b) ) and once with a while loop ( print_odd_while(a,b) ).
'''
a = int(input('First Number: '))
b = int(input('Second Number: '))


# First method
if a%2 == 0:
    a = a+1
print('Result using range function: '+str(list(range(a,b+1,2))))

def print_odd_for(a,b):
    c = []
    for i in range(a,b+1):
        if i%2 ==1:
            c.append(i)
    print('Results using for loop: '+str(c))
    return c

def print_odd_while(a,b):
    c = []
    d = a
    while d<=b:
        if d%2 == 1:
            c.append(d)
            d += 2
        else:
            d += 1
    print('Results using while loop: '+str(c))

print_odd_for(a,b)
print_odd_while(a,b)
