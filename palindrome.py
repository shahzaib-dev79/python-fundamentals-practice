import re

def is_palindrome(s):
    # Keep only letters and digits, and lowercase everything
    cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
    return cleaned == cleaned[::-1]


print(is_palindrome("racecar"))                          # True
print(is_palindrome("hello"))                             # False
print(is_palindrome("A man, a plan, a canal: Panama"))    # True
print(is_palindrome("Was it a car or a cat I saw?"))       # True