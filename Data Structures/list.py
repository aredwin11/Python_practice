#lists are like containers to store a set of values of any datatypes
name=["Edwin",11,'male',True] #Creating a list
solution=name[3] #Accessing the items in the list
print(solution)

# printing the items in the list
print(name)


#checking the type in the list
t=type(name[3])
print(t)

#Items in the list can be changed
name[2]="Studying python"
print(name)