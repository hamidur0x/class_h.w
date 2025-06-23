class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)

w = int(input("Enter width: "))
h = int(input("Enter height: "))

r = Rectangle(w, h)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
