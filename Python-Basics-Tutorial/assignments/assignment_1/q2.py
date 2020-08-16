#2. Triangle inequality states that for the sum of any two sides of a triangle is greater than the third side. Write
#a function check_triangle_inequality(a,b,c) that returns False if some combination of sides
#violates the triangle inequality (Hint: there are 3 scenarios) and True otherwise.

x = int(input('Enter first side: '))
y = int(input('Enter second side: '))
z = int(input('Enter third side: '))

'''Conditions to check:
x < z+y
z < x+y
y < x+z'''

def check_triangle_inequality(x,y,z):
    result = (x<z+y) and (z<x+y) and (y<x+z)
    return result

result = check_triangle_inequality(x,y,z)
print(result)
if result:
    print('Triangle of sides:'+str(x)+','+str(y)+','+str(z)+' is possible.')
else:
    print('Triangle not possible')
