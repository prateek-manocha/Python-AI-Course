def check_prime(n):
    #n should not be divisible by any no. less than n, other than 1.
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input('Enter the number: '))
    result = check_prime(n)
    print(result)
