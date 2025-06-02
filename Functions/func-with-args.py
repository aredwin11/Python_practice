def func(name,ending):
    print(f"hello {name}" , "Greetings!")
    print(ending)

func("Edwin","thank you")


#return statement
def diff2(a,b):
    dif=b-a
    return dif

a = int(input("Enter a number"))
b = int(input("Enter a number"))

res=diff2(a,b)
print("the difference of ",a ,"and",b,"is : ",res)

#returning multiple values
def fun():
    name1= "Edwin"
    age1 = 22
    return name1, age1

name, age = fun()
print(name)
print(age)