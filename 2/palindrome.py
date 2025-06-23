def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
text = input("Enter a string: ")
if is_palindrome(text):
    print(f'"{text}" is a palindrome.')
else:
    print(f'"{text}" is not a palindrome.')
