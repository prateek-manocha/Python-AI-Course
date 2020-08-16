#10. Write a function that uses a loop to print the Fibonacci series upto n terms called fibonacci_loop(n) .
n = int(input('Number till which we want Fibo series: '))

def fibo(n):
    print('Fibo series till '+str(n))
    a = 1 #First Term
    b = 1 #Second term
    c = []
    c.append(a)
    c.append(b)

    for i in range(n-2):
        temp = a+b
        a = b
        b = temp
        c.append(temp)
    print(c)

fibo(n)
