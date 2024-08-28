# Task - Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
for i in range(len(arr)-1, -1, -1):
  print(arr[i], end=' ')
