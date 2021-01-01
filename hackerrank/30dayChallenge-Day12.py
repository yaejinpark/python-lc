class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self, firstName, lastName, idNumber)
        self.scores = scores

    # Write calculate() here
    def calculate(self):
        possibleGrades = 'OEAPDT'
        gradeCondition = lambda a: [90 <= a <= 100, 80 <= a < 90, 70 <= a < 80, 55 <= a < 70, 40 <= a < 55, a < 40]
        avgGrade = sum(self.scores) / len(self.scores)
        for i, condition in enumerate(gradeCondition(avgGrade)):
            if condition:
                return possibleGrades[i]