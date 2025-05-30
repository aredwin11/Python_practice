# to print a number from 1 to 5 using for loop
for i in range(1,6):
    print(i)

#sum of first n number
total = 0
for i in range(1, 6):
    total += i
print("Sum:", total)

#Break Statement --> breaks the loop
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#Continue statement --> Skips the current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)