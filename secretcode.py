#normal english to secret code language

#coding:
#if letter has atleast 3 char remove first letter and append it at the end 
#append three random char at the starting  and the end
#simply reverse string

#decoding:
#if word contail less than 3 decode it
#else
#rmeove 3 random char from start and end .now rmeove last letter and append at begginning


#for encoding
a=input("Enter a string: ")
if len(a)<=2:
    a=a[::-1]
    print(a)
else :
    add1=input("Enter the 3 random letter at beggining: ")
    add2=input("Enter the 3 random letter at end:  ")
    modify= a[1:]+a[0]
    add=add1+modify+add2
    print(add)
#for decoding
b=input("Enter the code to decode: ")
if len(b)<=2:
    b=b[::-1]
    print(b)
else:
    modify1=b[3:-4]
    modify=modify1
    modify2=b[-4]
    modify=modify2+modify1
    print(modify)