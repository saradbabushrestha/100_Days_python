class Emoployee:
    company="Apple"
    def show(self):
        print(f"THe name is {self.name} and company is {self.company}.")
    @classmethod
    def changeCOmpany(cls,newcompany):
        cls.company=newcompany
e1=Emoployee()
e1.name="Sarad"
e1.show()
e1.changeCOmpany("Tesla")
e1.show()
print(Emoployee.company)