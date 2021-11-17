
class Employee(object):
    num_employee = 0

    def __init__(self, name , rate):
        self.name = name
        self.rate = rate
        self.owed = 0
        Employee.num_employee += 1

    def __def__(self):
        Employee.num_employee -= 1

    def hours(self, num_hours):
        self.owed += num_hours * self.rate
        return ("%.2f hours worked" % num_hours)

    def pay(self):
        self.owed = 0
        return ("Payed %s " % self.name)

emp1 = Employee('Jill', 18.50)
print(emp1.hours(24))
print(emp1.owed)
print(emp1.pay())
print()

class My_clas():

    def __init__(self, greet):
        self.greet = greet

    def __repr__(self):
        return ("a custom object (%r)" % (self.greet))

a = My_clas('giday')
print(a)
