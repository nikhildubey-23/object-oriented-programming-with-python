class Employee:
    ins = 1.5
    numberofemployee = 0
    def __init__(self,name,rank,salary):
        self.name = name
        self.rank = rank
        self.salary = salary
        Employee.numberofemployee += 1
    def inssalary(self):
        self.salary = self.salary*Employee.ins
    @classmethod
    def increaseamount(cls,amount):
        cls.ins =  amount
    @staticmethod
    def officeopen(day):
        if day == "sunday":
            return False
        else:
            return True

#inheritance 
class coder(Employee):
    def __init__(self, name, rank, salary , prolang , experience):
        super().__init__(name, rank, salary)
        self.prolang = prolang
        self.experience = experience

    def inssalary(self):
        self.salary = self.salary *(Employee.ins+0.2)


Nikhil = coder("Nikhil","Ethical hacker",140000,"python","5 years")
print(Nikhil.name)
print(Nikhil.rank)
print(Nikhil.salary)
print(Nikhil.prolang)
print(Nikhil.experience)

Nikhil.inssalary()
print(Nikhil.salary)

        