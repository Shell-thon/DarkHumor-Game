#!/usr/bin/env python

print("Use lower case for input please\n")

languages = ['python', 'java', 'c', 'c#', 'ruby', 'perl', 'c++', 'php']

print("Choose a programming language:")
for i, language in enumerate(languages, start=1):
	print(f"{i} - {language}")
print("9 - others")

i = int(input())
if i < 1 or i > 9:
	print("Invalid input")
elif i < 9:
	print(f"That's cool! {languages[i - 1]} is a great language!")
else:
	custom_language = input("Enter the language you use: ")
	print(f"Only geeks use {custom_language}")

# Check for gender
gender = input("You a boy or girl? \n")

# Check for girl
if gender == 'girl':
	print("Hey pretty lady :) \n")
	digits = int(input("Pass in your digit shawty we should grab a drink sometime: \n"))
	print("see ya later! \n")

 # Check for male
elif gender == 'boy':
	print("yo what's Up Big man \n")
	ps5 = ['cod', 'fifa', 'gta v', 'battlefield', 'apex legends', 'forza horizon']
	print("Choose a game:")
	for i, game in enumerate(ps5, start=1):
		print(f"{i} - {game}")
	print("7 - No")

	game = input()
	if game.lower() in ps5:
		print("mail me for giveaway shell@proton.me")
	else:
		print("tf? bro you f trans? \n")
