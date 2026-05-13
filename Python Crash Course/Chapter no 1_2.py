print("hello python Crash Course")
#------------------------------------
#chapter no 2


message = ("Hello Welcome to python Crash Course")
print(message)
message = ("Hello Welcome to python World")
print(message.title())

print(message.lower())
print(message.upper())


firstName = "Shahzaib"
lastName = "Fayyaz"
#combining two strings
intro = f"My name is {firstName} {lastName} "
print(f"Hello {intro}")
#adding whitespace
print(f"Hello \t{intro}")

#adding new lines
print("Languages \nJavaScript \nPython \nC++")



fvrt_language = "Python "
#print with extra spaces
print(fvrt_language)

withOutSpaces = fvrt_language.rstrip()
print(withOutSpaces)


#Exercise no 1
name = "Ash"
print(f"Hello {name}, welcome to my Python Crash Course repository")

#2.2
print(name.upper()) #upper case
print(name.lower()) #lower case
print(name.title()) #title case

#2.3
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

#2.4
name =" Ash "
print(f"\t{name}") #space added equal to tab
print(f"\n{name}") #starts from new line
print(f"{name.strip()}") #remove extra whitespaces from string
print(f"{name.rstrip()}") #remove whitespaces from right
print(f"{name.lstrip()}") #remove whitespaces from left



#2.5
file_name  = "pre.suff"
print(file_name.removeprefix("pre"))
print(file_name.removesuffix("suff"))

#-------------------------------Integers-------------------------------------
#2.6
print(2+2+4)
print(6-2+4)
print(2*4)
print(32/4)

#2.7
fvrtNumber = 7
print(f"My favourite Number is {fvrtNumber}")