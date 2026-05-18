#3-1
#Store the names in a list
team = ["Shumaila", "Azhar", "Ansa"]

#3-2
#print greetings to each member of your team
print(f"Hello {team[0]}! how are you")
print(f"Hello {team[1]}! how are you")
print(f"Hello {team[2]}! how are you")

#3-3
#create own vehicle list and write about it

vehicles= ["Buggati Cheron", "Suzuki 150" , "Ninja H2R" ]
print (f"I want to Buy a {vehicles[1]} in next two years")
print (f"{vehicles[0]} is my favourite car")
print (f"{vehicles[2]} is my favourite Sports bike")

#3-4 , 3-5
#Dinner invitation to the Guests
#replacing a guest with new guest
guests = ["Ahmad", "Uzair", "Rehman", "Maroof"]

print(f"{guests} \nI want you to join me on the Dinner next Sunday ")

print(f"{guests[3]} can't join me on Sunday")

guests[3] = "Shahram"
print(f"{guests} are comming to the dinner")

#3-6
#adding more guest

guests.insert(0, "Zark")#inserting at the beginning
guests.insert(3, "Adeel") #Inserting at the middle of the list
guests.append("Azan") # adding at the end of the list

print(f"Guys I have Booked a bigger table for {len(guests)}")
print(f"Now the List of Guests is \n{guests}")


#removing some guests
print(f"The booking of the new table is canceled so i can only invite two people")

guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(f"{guests[0]} you are still invited to the dinner")
print(f"{guests[1]} you are still invited to the dinner")

del guests[0]
del guests[0]

print(guests)# leaving an Empty string because dinner is cancelled

#=================================================================
#3-8
#places i want to visit

places = ["Dubai", "Gilgit", "Swat" , "Quetta","Hunza"]
print(places)

print(f"Original Order :\n",places)
print(f"Sorted Order :\n",sorted(places))



print(f"\n\nChecking the order of the List \n{places}")
places.reverse()
print(f"\nReversed list \n{places}")
places.reverse()
print(f"\nOriginal list order \n{places}")

places.sort()
print(f"Sorted in ascending order {places}")
places.sort(reverse=True)
print(f"Sorted in descending order {places}")



