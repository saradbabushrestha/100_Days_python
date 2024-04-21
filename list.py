marks = [3,5,6, "sarad", True, 6,7,8,9]
print(marks)
print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])




# print(marks[-3])#negative index vayo
# print(marks[len(marks)-3])#convert to postive

if 7 in marks:
    print("yes")
else:
    print("no")
    
if "sarad" in marks:
    print("yes")
else:
    print("no")
    
    
    
if "arad" in "sarad":
    print("yes")
    
    
print(marks[1:7:2])