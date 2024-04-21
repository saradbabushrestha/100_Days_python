x = 4
print(x)
def hello():
    global x
    x=5
    print(x)
    print("Hello sarad")
    print(f"THe global x is {x}")
    
hello()
print(f"THe global x is {x}")