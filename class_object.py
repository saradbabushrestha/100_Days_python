class Person:
    name="sarad"
    occupation="developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a= Person()
a.name="shyam"
a.occupation="accountant"
b=Person()
b.name="nikita"
b.occupation="Driver"
print(a.name)
print(a.occupation)
a.info()
b.info()