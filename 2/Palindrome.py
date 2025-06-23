class Palindrome:
    def __init__(self, word):
        self.word = word.lower().replace(" ", "")
    def is_palindrome(self):
        return self.word == self.word[::-1]
def main():
    text = input("Enter a string: ")
    palindrome = Palindrome(text)
    if palindrome.is_palindrome():
        print(f'"{text}" is a palindrome.')
    else:
        print(f'"{text}" is not a palindrome.')
if __name__ == "__main__":
    main()
