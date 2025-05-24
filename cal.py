try:
    value = input("Enter the simple equation: ")
    result = eval(value)
    print(f"The result is {result}")
except ValueError:
    print(f"Invalid value")
