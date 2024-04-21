# import random

# print("s for snake")
# print("w for water")
# print("g for gun ")

# s=["D","W","L"]
# w=["L","D","W"]
# g=["W","L","D"]
# swg= [s,w,g]

# cc=random.choice(swg)

# try:
#     #for user input
#     ui=input(print("Enter your choice: " ))
#     if ui=="s":
#         ui=0
#     elif ui=="w":
#         ui=1
#     elif ui=="g":
#         ui=2
#     #to show result
#     result = cc.pop(ui)
#     if result=="L":
#         print("You Loose")
#     if result=="W":
#         print("You Win")
#     if result=="D":
#         print("Draw")
# except:
#     print("Invalid Input")
import random  

comp=random.randint(0,2)
def check(comp,user):
    
    if (comp == user):
        return 0
    
    if(comp == 0 and user == 1):
        return -1
    
    if (comp ==1 and user == 2):
        return -1
    
    if (comp ==2 and user == 1):
        return -1
    
    return 1
    

user =int(input("O for Snake, 1 for Water and 2 for Gun\n"))

score =check(comp,user)
print("You: ",user)
print("Comp: ",comp)
if (score==0):
    print("Its a draw")
elif(score==1):
    print("You won")
elif(score==-1):
    print("You loose")

