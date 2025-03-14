text = input("Enter string: ")

def is_palindrome(s):
    return s == s[::-1]

print(f"Is the string a palindrome? {is_palindrome(text)}")
