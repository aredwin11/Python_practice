#functions is a block of statements which performs a specific TASK
# Syntax
def func1():   #this is called function definition
    print("this the example for functions")

func1()    # This is called function call


# Write a program to find diff of two numbers using functions
def diff2(a,b):
    if(b>a) :
        sub=b-a
        print(sub)
    elif(a>b):
        sub=a-b
        print(sub)
    else:
        print("equal")


a = int(input("Enter a number"))

b = int(input("Enter a number"))
diff2(a,b)