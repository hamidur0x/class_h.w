def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"
number = int(input("Enter a number: "))
print(f"The number {number} is {even_or_odd(number)}.")