try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
