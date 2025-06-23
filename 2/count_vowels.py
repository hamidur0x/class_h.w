def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for number in s:
        if number in vowels:
            count += 1
    return count
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))