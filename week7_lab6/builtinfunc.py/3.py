def is_palindrome(s):
    return s == s[::-1]  

text = input("Enter a word:  ")

if is_palindrome(text):
    print("The word is a palindrome")
else:
    print("The word is not a palindrome.")
