ep1={122:45 ,123:89 ,567:69 ,670:69}
ep2={222:67 ,556:90}


ep1.update(ep2)
print(ep1)
# ep1.clear()
# print(ep1)
# empt={}
# print(empt)
# ep1.pop(122)
ep1.popitem()
del ep1[122]
print(ep1)



