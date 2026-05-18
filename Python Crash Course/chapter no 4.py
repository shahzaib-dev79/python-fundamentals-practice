#4-1 Pizzas
pizzas = ["Malai Boti", "Tikka Pizza", "Fajita Pizza"]


for pizza in pizzas:
    print(f"I like {pizza}")

print("I love pizza")
print("I don't share pizza with anyone")
print("Malai Boti and Tikka combo is my favourite Pizza")



#4-2 Animals
animals= ["cat","dog","parrot"]
for animal in animals:
    print(f"{animal} would be a great pet")

print("These animals can understand you")
print("Your feelings")
print("and emotions")


#4-3 Counting to 20
for i in range(21):
    print(i)

#4-4
numbers = []
for i in range(1,1000001):
    numbers.append(i)
print(f"maximum number {max(numbers)}")
print(f"minimum number {min(numbers)}")
#4-5
print(f"minimum number {sum(numbers)}")


#4-6
evenNumbers = []
for i in range(1,21):
    if i%2!=0:
        evenNumbers.append(i)

print(evenNumbers)
#4-7
table = []
for i in range(1,11):
    table.append(i*3)
print(table)
#4-8
cubes = []
for i in range(1,11):
    cubes.append(i**3)
print(cubes)

#4-9
#cube comprehension
for i in range(10):
    print(f"the cube of {i+1} = {cubes[i]}")


#4-10
#Slicing
print(f"first three elements of the list are {cubes[:3]}")
print(f" three elements in middle of the list are {cubes[4:7]}")
print(f"last three elements of the list are {cubes[-3:]}")