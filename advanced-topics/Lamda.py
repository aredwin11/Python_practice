#finding square of a number without using lamda functions
def square(num):
    return num*num
res=square(5)
print(res)


#finding square of a number using lamda functions
square = lambda x: x * x
print(square(4))
