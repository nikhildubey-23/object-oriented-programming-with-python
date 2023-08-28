class Employee:
    ins = 1.5
    numberofemployee = 0
    def __init__(self,name,rank,salary):
        self.name = name
        self.rank = rank
        self.salary = salary
        Employee.numberofemployee += 1
    def inssalary(self):
        self.salary = int(self.salary*Employee.ins)
        
    # creating class method
    @classmethod #decorator 
    def salaryincrease(cls,amount):#when we create an obj we use self and when we create class method we use cls
        cls.ins = amount #changing the value of ins which is present inside the class 

Nikhil = Employee("Nikhil","Ethical hacker",140000) #suppling the arguments
Employee.salaryincrease(2) #this is how we use the class method Classname.Methodname(argument)
Nikhil.inssalary() #calling the inssalary method so that salary will increase
print(Nikhil.salary) #printing the salary
