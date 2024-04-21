#factorial (7)= 7*6*5*4*3*2*1
#factorial (6)= 6*5*4*3*2*1
#factorial (5)= 5*4*3*2*1
#factorial (0)= 1

#factorial (n)=n * factorial(n-1)

def factor(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* factor(n-1)
    
print(factor(3))
print(factor(4))
print(factor(5))
#eg:
# 5 *factor(4)
# 5*4*factor(3)
# 5*4*3*factor(2)
# 5*4*3*2*factor(1)
# 5*4*3*2*1


# generate fibonnaci 
# f(0)=0
# f(1)=1
# f(2)=f(1)+f(0)
# fn=f(n-1) +f(n-2)
def fibonnaci(n):
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return (fibonnaci(n-1)+fibonnaci(n-2))
for i in range(10):
    print(fibonnaci(i))
