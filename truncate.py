with open('sample.txt','w')as f:
    f.write('Hello World')
    f.truncate(5) #mero file ma 5 char matra hoss file nai teti byte ko hos
    
with open('sample.txt','r') as f:
    print(f.read())