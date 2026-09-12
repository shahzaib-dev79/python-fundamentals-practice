def is_valid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs.values():       
            stack.append(char)
        elif char in pairs:                
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack   


print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))