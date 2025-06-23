class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
def main():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    student = Student(name, age)
    student.display()
if __name__ == "__main__":
    main()
