import time
timestamp = time.strftime('%H:%M:%S')
print("The time right now is ",timestamp)
hour=int(time.strftime('%H'))
print(hour)
if(hour >=0 and hour <=12):
    print("Goodmorning Sir!!!!")
elif(hour >=12 and hour <=17):
    print("Goodafternoon Sir!!!")
elif(hour >=17 and hour <=20):
    print("Goodevening Sir!!!")
else:
    print("Goodnight Sir!!!")
   