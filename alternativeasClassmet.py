class Employee:
    def __init__(self,name,salary):
        self.name=name 
        self.salary=salary
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
        
e=Employee("Sarad",120000)
print(e.name)
print(e.salary)
string="Sarad-1200"
        
e2=Employee.fromStr(string)
print(e.name)
print(e.salary)