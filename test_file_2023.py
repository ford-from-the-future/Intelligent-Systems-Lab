class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

Emp_1 = Employee('Corey', 'Schafer', 50000)
Emp_2 = Employee('Test', 'Employee', 60000)

"---------------------------------------------"

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

"---------------------------------------------"

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_01 = Employee('Corey', 'Schafer', 50000)
emp_02 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_01.raise_amt)
print(emp_02.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

"---------------------------------------------"

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'Employee', 60000)

print(dev_1.email)
print(dev_2.email)

"---------------------------------------------"

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_10 = Employee('Corey', 'Schafer', 50000)
emp_20 = Employee('Test', 'Employee', 60000)

# print(emp_1 + emp_2)

print(len(emp_10))

"---------------------------------------------"

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_100 = Employee('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_100.first)
print(emp_100.email)
print(emp_100.fullname)

del emp_100.fullname

"---------------------------------------------"

class Point:


    def __init__(self, x, y, z):
        self.assign(x, y, z)


    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    def printPoint(self):
        print(self.x, self.y, self.z)

p1 = Point(2, 3, 5)
p1.printPoint()

p2 = Point(6, 2, -4)
p2.printPoint()

"---------------------------------------------"

class Point:
    'Sample docstring of class Point!'

    def __init__(self, x, y, z):
        self.assign(x, y, z)


    def assign(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def printPoint(self):
        print(self.x, self.y, self.z)

p1 = Point(2, 3, 5)
p2 = Point(6, 2, -4)

a = 5
pi = 3.14
text = "Hello World!"

print(type(3))

"---------------------------------------------"
