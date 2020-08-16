from q1 import *

high = input('Enter the highest number: ')
try:
    high = int(high)
except:
    print('Invalid input, Enter an Integer.')

def find_primes(high):
    c = []
    for i in range(2,high+1):
        if check_prime(i):
            c.append(i)
    return c

result = find_primes(high)
print(result)


# Sieve of Eratosthenes
def soe(high):
    result = [True for i in range(high+1)]
    prime=2
    while prime*prime <= high:
        #print(prime)
        if result[prime] == True:
            for j in range(prime*prime, high+1, prime):
                result[j] = False
        prime += 1
    return result


result = soe(high)
for i in range(2,len(result)):
    if result[i]==True:
        print(i, end=' ')
