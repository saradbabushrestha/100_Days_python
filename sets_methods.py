s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}
cities3=cities.union(cities2)# aUb
print(cities3)
cities3=cities.intersection(cities2)#a intersect b
print(cities3)
cities3=cities.symmetric_difference(cities2)#bar a intersect b
print(cities3)
cities3=cities.difference(cities2)#a-b
print(cities3)
cities3=cities.isdisjoint(cities2)
print(cities3)
cities3=cities.issuperset(cities2)
print(cities3)
cities3=cities.issubset(cities2)
print(cities3)
cities.add("Kathmandu")
print(cities)
cities.remove("Kathmandu")
print(cities)
item=cities.pop()
print(cities)
print(item)
# # del cities
# # print(cities)
# cities.clear()
# print(cities)