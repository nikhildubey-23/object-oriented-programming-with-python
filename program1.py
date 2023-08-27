''' by program number 1 we are going to start object oriented programing in python .
# in object oriented programing there is a classes and there object's are included class means templete like this you can understand '''

# creating class by the class name employee
class Employee:
    ''' if we are creating a class then we also have to create a constructor for that so in python the formate of constructor is pre define we cannot change its way''' 

# creating constructor 
    # def __init__(self):
    '''this is a way of defining the constructor which we cannot change yes but we can increase the argument taken by the constructor '''
    '''we passes the argument fname,lname,salary'''
    def __init__(self , fname,lname,salary):
        self.fname = fname
        '''self.fname is the class varibal in which we are assing the value of fname'''
        self.lname = lname
        self.salary = salary

    '''now we create a object of the class '''
Nikhil = Employee("nikhil","dubey",100000)
Preeto = Employee("preeto","sahu",100000)

'''now we try to access the vlaue'''
print(Nikhil.fname,Preeto.fname,"\n",Nikhil.salary,Preeto.salary)
        
