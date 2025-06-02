#Writing a file
# file.write() --> removes all the existing content and add this
file=open('names.txt','w')
file.write('Barath')
file.close()

f = open("names.txt", "r")
content = f.read()
print(content)
f.close()

#append --> along with existing content it adds this content also
file=open('names.txt','a')
file.write(' kumar')
file.close()

f = open("names.txt", "r")
content = f.read()
print(content)
f.close()