'''11. Write a function sum_game(value) that runs a loop that takes numbers as input from command line,
and exits only when the sum of the numbers so far reaches value . Make sure value is positive, but the
numbers which come from command line can be negative.
'''
import sys

def sum_game(value):
    sum = 0
    c = []
    while value < 0:
        value = int(input('Enter a positive value: '))

    while sum < value:
        num = int(input('Enter your number: '))
        sum += num
        c.append(num)
    return c, value

value = int(sys.argv[1])
list_numb, value = sum_game(value)
print('The sum of numbers in ' + str(list_numb)+' exceeds the input '+str(value))
