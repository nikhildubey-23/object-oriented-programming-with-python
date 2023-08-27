class Employee:
    # created for incrementation in salary
    ins = 1.5
    # created for Know the number of employee and giving the defalut value zero
    numberofemployee = 0
    def __init__(self,name,rank,salary):
        self.name = name
        self.rank = rank
        self.salary = salary
        # how we know that how many employee do we have for that we created a variable numberofemployee and give a default value one and it will increment it self by one when we call 
        # we used Employee. because we are using Employee variable not the self instance variable for incrementation
        Employee.numberofemployee += 1
    # suppose you want to increase the salary of anyemployee in any festivel how we will do  
    def inssalary(self):
        self.salary = self.salary*Employee.ins
        
print("Number of employee :-",Employee.numberofemployee)
Nikhil = Employee("nikhil","ethical hacker",150000)
print(Nikhil.name,"\n")        
print(Nikhil.rank,"\n")        
print(Nikhil.salary,"\n")

print("after getting the diwali bonous\n")
Nikhil.inssalary()
print(Nikhil.salary,"\n")
print("Number of employee :-",Employee.numberofemployee)

Preeto = Employee("preeto","ethical hacker",133000)
print("the name of the employee is ",Preeto.name,"\n")
print("the rank of the employee is ",Preeto.rank,"\n")
print("the salary of the employee is ",Preeto.salary,"\n")

print("after getting the diwali bonous\n")
Preeto.inssalary()
print(Preeto.salary,"\n")
print("Number of employee :-",Employee.numberofemployee)
