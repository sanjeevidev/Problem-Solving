# Task - Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
# Context - Given a 6 x 6 2D Array, A:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.

def hourglass_sum(arr):
    max_sum=float('-inf')
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            current_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2] +
                           arr[i+1][j+1] +
                           arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if current_sum>max_sum:
                max_sum=current_sum
    return max_sum

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    print(hourglass_sum(arr))
