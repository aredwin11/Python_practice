# recursion is a function which calls itself again and again
#factorial of a number

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)

num=int(input("Enter a number"))
res=fact(num)
print(res)