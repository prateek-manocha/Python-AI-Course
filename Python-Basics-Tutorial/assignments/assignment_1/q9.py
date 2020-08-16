'''9. Write a function that uses recursion to calculate the nth term of the Fibonacci series called
fibonacci(n) . (Google fibonacci series if you don't know it.)
'''
n = int(input('Number till which we want Fibo series: '))

def fibo(n):
    print('Fibo series till '+str(n))
    a = 1 #First term
    b = 1 #Second term
    for i in range(n-2):
        temp = a+b
        a = b
        b = temp
        #c.append(temp)
    print(b)

fibo(n)
