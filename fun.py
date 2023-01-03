#!/usr/sh
print("USE LOWER CASE FOR INPUT PLEASE\n")

List = 1, 2, 3, 4, 5, 6, 7, 8
cus = 9
print("1 - python\n" + "2 - java\n" + "3 - c\n" + "4 - c#\n" + "5 - ruby\n" + "6 - perl\n" + "7 - c++\n" + "8 - php\n" + "9 - others")
i = int(input("What language do you use: \n"))
if i == List:
	print("that's Cool!")

elif i == cus:
        customList = int(input("Enter the language you use: "))
        print("Only geeks use " + customList)

#Check for Gender
gem = "boy"
gemp = "girl"
gen = input("You a boy or girl\? \n")

#Girl check first
if gen == gemp:
	print("Hey pretty lady\:) \n")
	dig = int(input("Enter your digit we should grab a drink sometime"))

#Check for male
elif gen == gem:
	print("yo what\'s Up Big man \n")
	ps5 = 1, 2, 3, 4, 5, 6
	print("1 - COD\n" + "2 - Fifa\n" + "3 - GTA V\n" + "4 - Battlefield\n" + "5 - Apex Legends\n" + "6 - Forza Horizon\n" + "7 - No\n")
	game = input("Which game you play? \n")

#Giveaway
if game == ps5:
	print("mail me for giveaway shell@proton.me")
else:
	print("tf? bro you f trans? \n")
