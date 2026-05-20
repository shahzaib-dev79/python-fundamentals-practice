#5-1
#Condition test Check if you predicted true

car = "Mustang"
if car == "Alto":
    print("I predicted true")
else:
    print("I predicted false")
#5-2
#more comparisons

string  = "I am a Developer"
lowerString = string.lower()
if string ==lowerString:
    print('String is lower case')



number = 80
if number > 80:
    print("Number is greater then 80")
elif number <80 :
    print("Number is less then 80")
else:
    print("Number is equal to 80")



number = 100
number2 = 150

if number == 100 and number2  == 150:
    print("Alright Let's do the job")
if number <100 or number2 < 150:
    print("Ok fine!")



numbers = [13,12,11,10,8,5,1,15]
if 14 in numbers:
    print("14 is in the list")


if 15 not in numbers:
    print("15 is not in the list")


#5-3 , 5-4 , 5-5

color = "green"

if color == "green":
    print("You only got 5 points")
elif color == "yellow":
    print("You only got 10 points")
else:
    print("You only got 15 points")

#5-6
age = 18
if age < 2:
    print("Baby")
elif age <= 2 and age < 4:
    print("Toddler")
elif age <= 4 and age < 13:
    print("Kid")
elif age <= 13 and age < 20:
    print("Teenager")
elif age <= 20 and age < 65:
    print("Adult")
else:
    print("Elder")

#5-7 ---> 5-9
users=["admin","Maaz","Azhar","Ali"]
if len(users) != 0:
    for user in users:
        if user == "admin":
            print(f"Hello {user} would you like to see today's report")
        else:
            print(f"Hello {user} Welcome back")
else:(print("There is no user"))

#5-10
currentUser = ["ahmad", "ali", "john", "umair"]
username = "Ali"

if username.lower() in currentUser:
        print("use another username this name already exists")
else:
    print("Username is available")

#5-11
number = list(range(1,11))
for num in number:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    elif num == 4:
        print("4th")
    elif num == 5:
        print("5th")
    elif num == 6:
        print("6th")
    elif num == 7:
        print("7th")
    elif num == 8:
        print("8th")
    elif num == 9:
        print("9th")