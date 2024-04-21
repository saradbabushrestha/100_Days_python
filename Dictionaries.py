dic={
    "Sarad":"Human Being",
    "Spoon":"Object",
    69:"sadikshya",
    70:"Ram",
    71:"Sarda",
    "name":"Honey"
    
}
print(dic["Sarad"])
print(dic[71])
print(dic)
print(dic.get('Sarad'))
print(dic.keys())


print(dic.items())
for key, value in dic.items():
    print(f"THe value of corresponding to the key {key} is {value}")
    