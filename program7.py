class Employee:
    ins = 1.2
    def __init__(self,name,age,rank):
        self.name = name
        self.age = age
        self.rank = rank
    def inssalary(self):
        self.salary = int(self.salary*Employee.ins)   
    # magic method/duber method
    def __add__(self,other):
        return self.age+other.age 
    def __repr__(self) :
        return "the information about the employee is {},{},{}".format(self.name,self.age,self.rank)
    def __str__(self):
        return "the name of the employee is :- {}".format(self.name)
    

Nikhil = Employee("NIkhil",19,"ethical hacker")
Shubham = Employee("Shubham",20,"developer")

print(Nikhil.__add__(Shubham))
print(Nikhil.__str__())
print(Nikhil.__repr__())