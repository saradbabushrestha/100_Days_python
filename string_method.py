#string are immutable
#string lai change gardaina naya string banaunaxa change garera
a="!!! !Sarad!!!!! !Sarad!" 
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Sarad","Sathi"))
print(a.split(" "))
blogheading="introduction tO py"
print(blogheading.capitalize())#first lai upper garesi paxadi sab lai lower
str="Welcome to the console!!"
print(len(str))
print(len(str.center(50)))
print(a.count("Sarad"))
print(str.endswith("!"))
print(str.endswith("to",4,10))

str1="He's name is dan.he is an honest man."
print(str1.find("is"))
# print(str1.index("ishh"))


print(str1.isalnum())
print(str1.islower())
print(str1.istitle())
print(str.swapcase())
print(str.title())
