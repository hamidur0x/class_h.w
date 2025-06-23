class VowelCounter:
    def __init__(self, text):
        self.text = text

    def count(self):
        vowels = "aeiouAEIOU"
        count = 0
        for char in self.text:
            if char in vowels:
                count += 1
        return count

text = input("Enter a string: ")
vc = VowelCounter(text)
print("Number of vowels:", vc.count())
