class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetail(self):
      print(f"The name of the employee ; {self.id}is {self.name}.")
      
      
class Programmer(Employee):
    def showLanguage(self):
        print("THe default language is puthon")
e1=Employee("ROhan Das",400)
e1.showDetail()
e2=Programmer("Sarad",4100)
e2.showDetail()
e2.showLanguage