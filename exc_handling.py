a= input("ENter the number: ")

print(f"MUltiplication table of {a} is :")
try:
 for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalild error")