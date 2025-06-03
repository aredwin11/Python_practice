try:
    x = 0
    y = 10 / x
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Division successful:", y)
