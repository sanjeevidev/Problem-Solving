# Task - Given a string, S, of length N that is indexed from O to N — 1, print its even-indexed and odd-indexed characters as 2 space-
# separated strings on a single line (see the Sample below for more detail).
# Note: O is considered to be an even index.
# Example : s = adbecf
# Print abc def

s = input()
for i in range(int(s)):
    x = input()
    for i in range(0, len(x), 2):
        print(x[i], end='')
    print(end=' ')
    for i in range(1, len(x), 2):
        print(x[i], end='')
    print('')
