# dictionary is a collection of key value pairs
d={ }  #empty dictionary
print (type(d))

#syntax of a dictionary
marks={ #"key" : "values"
    "kiran" : 100,
    "Arun" : 45,
    "kamal" : 67,
    "prakash" : 89
}

print(marks) #prints the entire dictionary

#Methos in the dictionary
print(marks.items()) #prints the entire dictionary

print(marks.keys()) #prints only the keys ie is the left hand side values

print(marks.values())  #prints only the values i.e is the right hand side values

marks.update({"edwin":100 , "kiran":99}) # we can update our dictionary
print(marks)

print(marks.get("kamal"))  #prints the specified key value

#diffrence between marks.get("kamal") and marks["kamal"]
print(marks.get("Krishna"))  #prints none if the value does not exist
print(marks["Krishna"])  #returns type error if the key does not exist