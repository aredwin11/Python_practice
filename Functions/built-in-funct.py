#python has some built-in functions
# 1 . len() function --> to find the length
name=input("enter the name : ")
print(f"the length of the {name} is", len(name))

#sum and average
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Sum:", total)
print("Average:", average)

#Find max and min
numbers = [10, 20, 30, 40, 50]
print(max(numbers))
print(min(numbers))
