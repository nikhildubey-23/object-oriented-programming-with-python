''' now we create ststic method'''
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
    @classmethod  
    def salaryincrease(cls,amount):
        cls.ins = amount 
    @classmethod
    def from_str(cls,emp_string):
        name , rank, salary =  emp_string.split("-") 
        return cls(name,rank,salary) 

    #suppose we do not want to use the cls as well as the self instance than we create static method lets see how we create the static  method
    @staticmethod 
    def officeopen(day):
        if day == "sunday":
            return False
        else :
            return True


Nikhil = Employee("Nikhil","Ethical hacker",140000)
Employee.salaryincrease(2) 
Nikhil.inssalary() 
print(Nikhil.name) 
print(Nikhil.rank) 
print(Nikhil.salary) 
print("\n")
Abhinay = Employee.from_str("Abhinay-full stack developer -140000")
print(Abhinay.name) 
print(Abhinay.rank)
print(Abhinay.salary)

# taking use of static method
print(Employee.officeopen("monday")) #we get the output true
