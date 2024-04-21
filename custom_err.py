# # a = int(input("ENter any value between 5 and 9:"))
# # try:
# #  if( a<5 or a>9):
# #     raise ValueError("Value error should be between 5 and 9")
# # except:
# #     if(a!="quit"):
# #      raise ValueError("Invalid word")
# #     elif(a=="quit"):
# #      print("Executed")
 
# a=input("Enter value:")
# if (a!="quit"):
#      raise ValueError("Invalid error!!!")
# elif(a=="quit"):
#      print("executed")

a = input("ENter any value between 5 and 9:")
try:
 if( a<5 or a>9):
    raise ValueError("Value error should be between 5 and 9")
 elif(a!="quit"):
     raise ValueError("Invalid word")
except:
    
    if(a=="quit"):
     print("Executed")
    elif(a>5 or a<9):
     print("Executed")
