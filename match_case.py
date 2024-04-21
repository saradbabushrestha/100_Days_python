#match_case_statements
x=int(input("Enter the value of x: "))
#x is the variable to match
match x:
    #if x is 0
    case 0:
        print("x is zero")
    #case with if_condtion
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90.")
    case _ if x!=80:
        print(x,"is not 80.")
        
    case _:
        print(x)
#c/c++ ma chai break chainxa compulsary tara yesma chaidaina
