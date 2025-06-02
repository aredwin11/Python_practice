#reading the contents from names.txt
#Opening a file
with open('names.txt','r')as file:
    content=file.read()
    print(content)
    file.close()

#read() --> Reads Entire file as a string
f = open("names.txt", "r")
content = f.read()
print(content)
f.close()

#readLine --> Reads the content of one line
f = open("names.txt", "r")
content = f.readline()
print(content)
f.close()

#readlines -->Reads all line and returns them as a string
f = open("names.txt", "r")
content = f.readlines()
print(content)
f.close()