class Person:
    name="Sarad"
    occ="Developer"
    
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a=Person()
print(a.name)


a.name="Divya"
a.occ="HR"
a.info()