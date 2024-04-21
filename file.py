# #readint a file
# f= open('myfile.txt','r')

# # print(f)
# text=f.read()
# print(text)
# f.close
f=open('myfile.txt','w')
f.write("Hello,world")
f.close()

f=open('myfile.txt','a')
f.write("Hello,world")
f.close()


with open ('myfile.txt','a') as f:
    f.write(" Hey i am inside with") 