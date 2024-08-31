# Task - Given a base-10 integer. n, convert it to binary (base-2). Then find and 
# print the base-10 integer denoting the maximum number of consecutive I's in n's binary representation.
# Example
# n 125
# The binary representation of  125^10 is 11111101^2. In base , there are 5 and 1 consecutive ones in two groups. Print the maximum - 5.

n = int(input())
binary_representation = bin(n).replace("0b", "")
max_count = 0
current_count = 0
    
for bit in binary_representation:
  if bit == '1':
    current_count += 1
    max_count = max(max_count, current_count)
else:
  current_count = 0
        print(max_count)
print(max_count)
