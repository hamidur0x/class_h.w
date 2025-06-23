class Number:
    def __init__(self, value):
        self.value = value

    def is_even_or_odd(self):
        if self.value % 2 == 0:
            return "Even"
        else:
            return "Odd"
num = int(input("Enter a number: "))
number = Number(num)
print(number.is_even_or_odd())
