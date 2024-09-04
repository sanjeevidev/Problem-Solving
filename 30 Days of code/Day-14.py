# Task - Complete the Difference class by writing the following:
# A class constructor that takes an array of integers as a parameter and saves it to the _elements instance variable.
# A computeDifference method that finds the maximum absolute difference between any 2 numbers in —elements and 
# stores it in the maximumDifference instance variable.

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
	# Add your code here
    def computeDifference(self):
        max_element = max(self.__elements)
        min_element = min(self.__elements)
        self.maximumDifference = max_element - min_element
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
