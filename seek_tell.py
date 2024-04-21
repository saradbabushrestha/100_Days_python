with open ('file.txt','r') as f:
    print(type(f))
    #move to the 1-th byte in the file
    f.seek(10)
    #read the next 5 byte
    print(f.tell())
    data =f.read(5)
    print(data)