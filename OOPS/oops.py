#Python Object-Oriented Programming

class Employee:
    raise_amount=1.04
    num_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@company.com'
        #runs everytime we create a new employee
        Employee.num_of_emps+=1

    def fullname(self): 
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay=int(self.pay*Employee.raise_amount)# or self.raise_amount


print(Employee.num_of_emps)
print("**************")
emp_1=Employee('Sanjay', 'Singh',50000)
emp_2=Employee('Test','User',60000)


print(emp_1.__dict__)
Employee.raise_amount=1.05
emp_1.raise_amount=2 #2 set for only emp_1

print(Employee.__dict__)

#first instance in checked for raise_amount, then class variables is checked.
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)



print("*************************")
print(Employee.num_of_emps)
