# Task - # Complete the code in the editor below. The variables i. d, and s are already declared and initialized for you. You must:
# 1. Declare 3 variables: one of type int. one of type double, and one of type String.
# 2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
# 3. Use the + operator to perform the following operations:
#   1. Print the sum of i plus your int variable on a new line.
#   2. Print the sum of d plus your double variable to a scale of one decimal place on a new line.
#   3. Concatenate s with the string you read as input and print the result on a new line.

first_integer = 10
first_double = 3.14
first_string = 'Python'

second_integer = int(input())
second_double = float(input())
second_string = input()

print(first_integer+second_integer)
print(first_double+second_double)
print(first_string+second_string)