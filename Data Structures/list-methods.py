#Adding an element into the list
a=["Arun","Car","Bus",23]
print(a)

#append --> adds the element at the last index position
a.append("Apple")
print(a)

#extend --> adds multiple element at the end
a.extend([10,"Arun","Good"])
print(a)

#insert --> adds at the specific position
a.insert(0,"new")
print(a)


#Updating the list
str=[10,20,30,40,60]
print("str elements are",str)
a=len(str)-1
str[a]=50
print(str)

#Removing the elements from the list
#remove --> removes specific element in the list
str.remove(20)
print(str)

#pop -->Removes the element at the specific location
a = str.pop(2)
print("Removed Element " ,a)
print("After pop",str)

#Del statement --> deletes the first element
del str[0]
print("After del",str)


#to sort the elements in the list
man=[23,34,65,20,1,3,0,35,39,99,87]
man.sort()
print(man)