# Task - Given n names and phone numbers. assemble a phone book that maps friends' names to their respective phone numbers.
# You will then be given an unknown number of names to query your phone book for. For each name queried, 
# print the associated entry from your phone book on a new line in the form name=phoneNumber; 
# if an entry for name is not found, print Not found instead.
# Note: Your phone book should be a Dictionary/Map/HashMap data structure.

n = int(input())
d = {}

for i in range(n):
    x = input().split()
    d[x[0]] = x[1]

while True:
    try:
        NAME = input()
        if NAME in d:
            print(NAME, "=", d[NAME], sep="")
        else: print("Not found")
    except:
        break
