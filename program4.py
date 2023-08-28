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

    # creating alternative method by the help of classmethod
    @classmethod
    def from_str(cls,emp_string):
        name , rank, salary =  emp_string.split("-") #split function use to split the string when it found the "-"
        return cls(name,rank,salary) #this is how we assing the value

Nikhil = Employee("Nikhil","Ethical hacker",140000) #suppling the arguments
Employee.salaryincrease(2) #this is how we use the class method Classname.Methodname(argument)
Nikhil.inssalary() #calling the inssalary method so that salary will increase
print(Nikhil.name) #printing the name
print(Nikhil.rank) #printing the rank
print(Nikhil.salary) #printing the salary
print("\n")
Abhinay = Employee.from_str("Abhinay-full stack developer -140000")
print(Abhinay.name) #printing the salary
print(Abhinay.rank)
print(Abhinay.salary)
