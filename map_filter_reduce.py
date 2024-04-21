#MAP
def cube(x):
    return x*x*x
print(cube(8))


l=[1,2,4,6,3]
newl=list(map(cube,l))#newl=list(map(lambda x:x*x*x,l))
print(newl)

#FILTER
def filter_function(a):
    return a>2
newnewl= list(filter(filter_function,l))
print(newnewl)


from functools import reduce
number=[1,2,4,6,3]
sum=reduce(lambda x,y:x + y,number)
print(sum)