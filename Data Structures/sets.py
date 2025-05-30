#creation of sets
set1= {1, 2, 3, 4}
print(set1)

#adding elements to the set
set2={"edwin","dhanush","harish","mayank"}
print(set2)
set2.add("virat")
print(set2)

#Joining two set
set3={"edwin","dhanush","harish","mayank"}
set4={10,20,30,40}
set5=set3.union(set4)
print(set5)

#update
set3.update(set4)
print(set3)