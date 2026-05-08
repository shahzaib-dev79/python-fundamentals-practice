#Print first 10 natural numbers using while loop
from prompt_toolkit.input import Input

i = 1
while i <= 10:
    print(i)
    i = i+1

# 2. Display numbers from -10 to -1 using for loop
for i in range (-10 , 0):
    print(i)

print("Done")
# Calculate the sum of all numbers from 1 to N
num = int(input("Enter a number : "))
result = 0
for i in range (num+1):
    result = i + result

print(result)
# Print multiplication table of a given number

num = int(input("Enter the number : "))
for i in range(1,11):
    print(f"{num} multiply by {i} = {num*i}")

# Calculate the cube of all numbers from 1 to a given number

num = int(input("Enter the Number : "))
for i in range (1 , num+1):
    print(f"Cube of {i} = {i**3}")



