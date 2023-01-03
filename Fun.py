#!/usr/bin/env python

import random
import colorama

colorama.init()

def rainbow(s):
    colors = [
        colorama.Fore.RED,
        colorama.Fore.YELLOW,
        colorama.Fore.GREEN,
        colorama.Fore.CYAN,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA
    ]
    output = ""
    for i, c in enumerate(s):
        output += random.choice(colors) + c
    return output

def greeting():
    images = [
        "   /\_/\  ",
        "  ( o.o ) ",
        "  >^<   ",
        "  '' '' ",
        "  ( - )( - )  "
    ]
    image = random.choice(images)
    name = "DARK HUMOR GAME"
    decorated_name = rainbow(name)

    print(decorated_name)
    print(image)

greeting()

languages = ['python', 'java', 'c', 'c#', 'ruby', 'perl', 'c++', 'php']

print("\n I use python to code")
for i, language in enumerate(languages, start=1):
	print(f"{i} - {language}")
print("9 - others \n")
print("Pick your language: \n")

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
