'''6. Write a function greet_me() to take your name as input from the command line and print a
personalized greeting like "Hello, Rani, how are you today?"'''

import argparse

parser = argparse.ArgumentParser(description='Take input name.')
parser.add_argument('-name', '--n', type=str, default='Rani', help='person to greet')

args = parser.parse_args()
name = args.n
def greet_me(name):
    print("Hello, "+name+', how are you today?')

greet_me(name)
