class Vector:
    def __init__(self,i,j,k) :
        self.i=i
        self.j=j
        self.k=k
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return f"{self.i + x.i}i + {self.j+x.j}j + {self.k+x.k}k"
v=Vector(3,5,6)
print(v)
v1=Vector(2,2,9)
print(v1)
print(v+v1)