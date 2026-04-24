# Task
# Given an integer, perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range 2 of 5 to , print Not Weird
# If  is even and in the inclusive range of 6 to 20 , print Weird
# If  is even and greater than 20, print Not Weird

n = int(input("Enter a number : "))
if n%2 == 0:
    if n<=5:
        print("Not Weired")
    elif 6 <= n <= 20:
        print("Weired")
    elif n>20:
        print("not Weired")
else:
    print("Weired")

