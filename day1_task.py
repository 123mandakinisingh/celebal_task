# first program 
print("Hello everyone")

#variables in python 





#example1
n=10
string="Easy programming language"
print(n)
print(string)

#example2
a=10
b=20
print(a+b)

#example3
s1="hello"
s2="world"
print(s1+" "+s2)

#example4
x=y=z=50
print(x)
print(y)
print(z)
#example5
p,q,r=10,30,70
print(p)
print(q)
print(r)







#DATA TYPES IN PYTHON HACKERRANK
# Read a full line of input from stdin and save it to our dynamically typed variable, input_string.
input_string = input()

# Print a string literal saying "Hello, World." to stdout.
print('Hello, World.')
print(input_string)

# TODO: Write a line of code here that prints the contents of input_string to stdout.






i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
var_int = 0
var_double = 0
var_string = ""

# Read and save an integer, double, and String to your variables.
var_int = int(input())
var_double =float(input())
var_string = input()

# Print the sum of both integer variables on a new line.
print(i+var_int)

# Print the sum of the double variables on a new line.
print(d+var_double)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s+var_string)





#COMPARE THE TRIPLETS

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    x=0
    y=0
    for i in range(len(a)):
        if a[i] > b[i]:
            x += 1
    for i in range(len(b)):
        if b[i] > a[i]:
            y += 1
        result = (x,y)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()