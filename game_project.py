from random import randint
from termcolor import colored
from results_game_project import guess_bday_fav_animal, fav_animal

"""

A Buzzfeed style game where the user creates a coffee drink.
From the user's input the game will guess the user's birthday. 
This is a one user game.

"""

def choose_size_drink():
	# If user's input is not in size_list return an error and prompt the user for input again.
	# Return the user's value
	size_list = ["small", "medium", "large"]
	size = raw_input("Choose a size (small, medium, large):\n>>> ")
	if size not in size_list:
		print colored(size + " is not an option. Try again!", "red")
		return size_drink()
	else:
		return size

def choose_temp_drink():
	# If user's input is not in temp_list return an error and prompt the user for input again. 
	# Return the user's value
	temp_list = ["iced", "hot"]
	temp = raw_input("Choose a temperature (iced or hot):\n>>> ")
	if temp not in temp_list:
		print colored(temp + " is not an option. Try again!", "red")
		return temp_drink()
	else:
		return temp

def choose_drink_type():
	# If user's input is not in drink_list return an error and prompt the user for input again.
	# Return the user's value
	drink_list = ["latte", "frapp", "coffee"]
	drink = raw_input("Choose a delicious drink! (latte, frapp, coffee):\n>>> ")
	if drink not in drink_list:
		print colored(drink + " is not an option. Try again!", "red")
		return drink_type() 
	else:
		return drink

def choose_milk_type():
	# If user's input is not in milk_list return an error and propmt the user for input again.
	# Return the user's value
	milk_list = ["2%", "whole", "soy", "none"]
	milk = raw_input("Choose a milk option (2%, whole, soy, none):\n>>> ")
	if milk not in milk_list:
		print colored(milk + " is not an option. Try again!", "red")
		return milk_type()
	else:
		return milk


def play_buzzfeed_game():
	print colored("Build a drink and we'll guess your birthday and favorite animal!\nChoose from the options given.\nLet's Play!!!", "yellow", attrs=["bold"])

	size = choose_size_drink()
	temp = choose_temp_drink()
	drink = choose_drink_type()
	milk = choose_milk_type()

	if size == "small":
 		if temp == "hot":
 			print guess_bday_fav_animal("December", fav_animal)
 		elif temp == "iced":
 			winter_month = randint(1, 3)
 			if winter_month == 1:
 				print guess_bday_fav_animal("January", fav_animal)
 			else:
 				print guess_bday_fav_animal("February", fav_animal)
	elif size == "medium":
		if temp == "hot":
			if drink == "latte" or drink == "frapp":
				print guess_bday_fav_animal("October", fav_animal)
			else:
				print guess_bday_fav_animal("November", fav_animal)
		elif temp == "iced":
			print guess_bday_fav_animal("September", fav_animal)
	elif size == "large":
		if temp == "hot":
			if drink == "coffee":
				spring_month = randint(3, 6)
				if spring_month == 3:
					print guess_bday_fav_animal("March", fav_animal)
				else:
					print guess_bday_fav_animal("April", fav_animal)
			else:
				print guess_bday_fav_animal("May", fav_animal)
		elif temp == "iced":
			if drink == "latte" or drink == "frapp":
				if milk == "whole":
					print guess_bday_fav_animal("June", fav_animal)
				else:
					print guess_bday_fav_animal("July", fav_animal)
			else:
				print guess_bday_fav_animal("August", fav_animal)


def play_again():
	while True:
		repeat_game = raw_input("Would you like to play again? (Type y/n): ")
		if repeat_game == "y" or repeat_game == "yes":
			buzzfeed_game()
		elif repeat_game == "n" or repeat_game == "no":
			exit()
		else:
			print colored("Not a valid input. Type (y/n).", "red")
			play_again()

play_buzzfeed_game()
play_again()


