countries =("spain","italy","nepal","england","india")
temp=list(countries)
temp.append("russia")#add item
temp.pop(3)          #remove item 
temp[2]="finland"     #change item
countries=tuple(temp) 
print(countries)
res= countries.count("italy")
print(res)
