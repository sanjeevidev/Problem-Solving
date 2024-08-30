# Task - Complete the factorial function with the following paramter:
# • int n: an integer
# Returns
# • int: the factorial of n

# Note: If you fail to use recursion or fail to name your recursive function factorial or
# Factorial, you will get a score of O.

def factorial(n):
    if (n==1 or n==2):
        return n
    else:
        return n*factorial(n-1)

n = int(input().strip())
result = factorial(n)
print(result)
