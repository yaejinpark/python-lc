class Employee: 
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1 

    # print full name using method
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self): 
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Ace', 'Richard', 50000)
emp2 = Employee('Max', 'Ron', 40000)

print("Number of employees:")
print(Employee.num_of_emps)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

emp1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

# print(emp1.__dict__)
# print(emp2.__dict__)
# print(Employee.__dict__)
'''
print(emp1.first)
print(emp2.email)
# Print full name using long way 
print('{} {}'.format(emp1.first, emp1.last))
print('{} {}'.format(emp2.first, emp2.last))

Employee.fullname(emp1)
print(emp1.fullname())
print(emp2.fullname())



emp1.first = "Ace"
emp1.last = "Richard"
emp1.email = "ace.richard@company.com"
emp1.pay = 50000

emp2.first = "Max"
emp2.last = "Ron"
emp2.email = "max.ron@company.com"
emp2.pay = 40000

print(emp1.email)
print(emp2.last)

'''