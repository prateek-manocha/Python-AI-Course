#Python file to take input for q7.py

import argparse

parser = argparse.ArgumentParser(description='Take input.')
parser.add_argument('-first', '--f', type=float, default=10, help='first argument')
parser.add_argument('-second', '--s', type=float, default = 10, help='second argument')

args = parser.parse_args()
print(args)
