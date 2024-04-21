class employee:
    companyName="Apple"
    noOfEMployees=0
    def __init__(self,name) :
        self.name= name
        self.raise_amount=0.02
        employee.noOfEMployees+=1
    def showdetail(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEMployees} in {self.companyName} is {self.raise_amount}.")
emp1=employee("sarad")
emp1.raise_amount=0.3
emp1.companyName="Apple Nepal"
emp1.showdetail()
# employee.showdetail(emp1)
emp2=employee("ram")
emp2.showdetail()
