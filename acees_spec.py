# class Employee:
#     def __init__(self):
#         self.__name="Sarad"

# a=Employee()
# # print(a.name)#yesari acess hudaina
# print(a._Employee__name)#can be acess indirect;
# print(a.__dir__)

class Student:
    def __init__(self) -> None:
        self._name="Sarad"
        
    def _funName(self):
        #protected method
        return "CodeWithSarad"
class Subject(Student):
    #inhertied class
    pass
obj=Student()
obj1=Subject()

#calling by obj of student class
print(obj._name)
print(obj._funName())

#calling by object of sbject classs
print(obj1._name)
print(obj1._funName())