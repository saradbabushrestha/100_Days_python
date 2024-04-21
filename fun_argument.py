# def average(a,b,c=9):
#     print("The average us ", (a+b)/2)

# # average(3,4)
# average(3,5)


def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+1
        print("average is : ",sum/len(numbers))
average(5,6)




def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+1
        # print("average is : ",sum/len(numbers))
        
        return sum/len(numbers)
    
c=average(5,6)
average(5,6)


