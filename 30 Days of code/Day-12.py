# Task - You are given two classes. Person and Student, where Person is the base class and Student is the derived class. 
# Completed code for Person and a declaration for Student are provided for you in the editor. 
# Observe that Student inherits all the properties of Person.
# Complete the Student class by writing the following:
# A Student class constructor, which has 4 parameters:
# 1. A string, firstName.
# 2. A string, lastName.
# 3. An integer. idNumber.
# 4. An integer array (or vector) of test scores, scores.
# A char calculate() method that calculates a Student object's average and returns the
# grade character representative of their calculated average:

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores
        
    def calculate(self):
        score = sum(self.scores) / len(self.scores)
        if (score <=100 and score >=90):
            return 'O'
        elif (score <90 and score >=80):
            return 'E'
        if (score <=80 and score >=70):
            return 'A'
        if (score <70 and score >=55):
            return 'P'
        if (score <55 and score >=40):
            return 'D'
        if (score <40):
            return 'T'
      
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
