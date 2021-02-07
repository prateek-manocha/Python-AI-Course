#Implementation for factorial function that takes a number and returns its factorial.

def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

if __name__ == '__main__':
    number = 4
    print(fact(4))
