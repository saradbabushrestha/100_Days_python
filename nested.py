num=int(input("Enter the value of num: "))
if(num <0):
    print("Number is -ve.")
elif(num >0):
    if(num <=10):
      print("Number is between 1-10.")
    elif(num >10 and num <=20):
      print("Number is between 11-20.")
    else:
       print("NUmber is greater than 20")
else:
    print("Number is Zero.")
