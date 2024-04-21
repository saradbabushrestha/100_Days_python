#this is my first exercise of making simple calculator using python
print("Enter the value of first number")
a=int(input())
print("Enter the value of second number")
b=int(input())
print("Enter the operator for calculation")
c=str(input())
if (c=="+"):
 print("Addition = ",a+b)
elif (c=="-"):
 print("Subtraction = ",a-b)
elif (c=="*"):
 print("Multiplication = ",a*b)
elif (c=="/"):
 print("Division = ",a/b)
else:
 print("INVALID INTEGER")


