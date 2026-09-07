#Write a function greet(name) that returns "Hello, <name>!".

def greetings():
    print("Hello world")


greetings()

#Write a function is_even(n) that returns True if n is even, False otherwise.
def isEven(num):
    if num%2 == 0 or num == 0:
        return True
    else: 
        return False

print(isEven(3))
print(isEven(0))
print(isEven(20))

#Write a function add(a, b) that returns the sum of two numbers, then call it with different argument types (ints, floats).
def sum(num1, num2):
    return num1 + num2

print(sum(10, 12.0))

#Write a function power(base, exponent=2) that returns base raised to exponent. Call it once with one argument and once with both.
