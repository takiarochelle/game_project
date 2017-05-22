from random import randint
from termcolor import colored
from results_game_project import guess_bday_fav_animal, fav_animal

"""

A Buzzfeed style game where the user creates a boba drink.
From the user's input the game will guess the user's birthday and favorite animal. 
This is a one user game.

"""


def choose_drink_size():
	# If user's input is not in size_list return an error and prompt the user for input again.
	# Return the user's value
	size_list = ["a", "b", "c"]
	size = raw_input("What size do you normally get?\na. small\nb. medium\nc. large\n>>> ")
	size = size.lower()
	if size not in size_list:
		print colored(size + " is not an option. Try again!", "red")
		return choose_drink_size()
	else:
		return size


def choose_pearls():
	# If user's input is not in pearls_list return an error and prompt the user for input again. 
	# Return the user's value
	pearls_list = ["yes", "no", "y", "n"]
	pearls = raw_input("Would you like to add pearls? (y/n)\n>>> ")
	pearls = pearls.lower()
	if pearls not in pearls_list:
		print colored(low_pearls + " is not an option. Try again!", "red")
		return choose_pearls()
	else:
		return pearls


def choose_sweetness_level():
	# If user's input is not in sweetness_list return an error and prompt the user for input again.
	# Return the user's value
	sweetness_list = ["a", "b", "c"]
	sweetness = raw_input("What range of sweetness do you prefer?\na. 0-50%\nb. 50-75%\nc. 75-100%\n>>> ")
	sweetness = sweetness.lower()
	if sweetness not in sweetness_list:
		print colored(sweetness + " is not an option. Try again!", "red")
		return choose_sweetness_level() 
	else:
		return sweetness


def choose_flavor():
	# If user's input is not in flavor_list return an error and propmt the user for input again.
	# Return the user's value
	flavor_list = ["a", "b", "c", "d"]
	flavor = raw_input("Lastly, choose a flavor!\na. taro\nb. green milk tea\nc. oolong\nd. Thai milk tea\n>>> ")
	flavor = flavor.lower()
	if flavor not in flavor_list:
		print colored(flavor + " is not an option. Try again!", "red")
		return choose_flavor()
	else:
		return flavor


def play_buzzfeed_game():
	print colored("\nCreate a boba drink and we'll guess your birthday and favorite animal!\nEnter answer after the >>>.\nLet's Play!!!", "yellow", attrs=["bold"])

	size = choose_drink_size()
	pearls = choose_pearls()
	sweetness = choose_sweetness_level()
	flavor = choose_flavor()

	if size == "a":
 		if pearls == "yes" or pearls == "y":
 			print guess_bday_fav_animal("December", fav_animal) 
 		elif pearls == "no" or pearls == "n":
 			winter_month = randint(1, 3)
 			if winter_month == 1:
 				print guess_bday_fav_animal("January", fav_animal) 
 			else:
 				print guess_bday_fav_animal("February", fav_animal) 
	elif size == "b":
		if pearls == "yes" or pearls == "y":
			if sweetness == "a" or sweetness == "c":
				print guess_bday_fav_animal("October", fav_animal) 
			else:
				print guess_bday_fav_animal("November", fav_animal) 
		elif pearls == "no" or pearls == "n":
			print guess_bday_fav_animal("September", fav_animal) 
	elif size == "c":
		if pearls == "yes" or pearls == "y":
			if sweetness == "b" or sweetness == "a":
				if flavor == "a" or flavor == "d":
					print guess_bday_fav_animal("March", fav_animal) 
				else:
					print guess_bday_fav_animal("April", fav_animal) 
			else:
				print guess_bday_fav_animal("May", fav_animal) 
		elif pearls == "no" or pearls == "n":
			if sweetness == "c" or sweetness == "b":
				if flavor == "b" or flavor == "a":
					print guess_bday_fav_animal("June", fav_animal) 
				elif flavor == "c" or flavor == "d":
					print guess_bday_fav_animal("July", fav_animal) 
			else:
				print guess_bday_fav_animal("August", fav_animal) 


def play_again():
	while True:
		repeat_game = raw_input("Would you like to play again? (Type y/n): ")
		repeat_game = repeat_game.lower()
		if repeat_game == "y" or repeat_game == "yes":
			play_buzzfeed_game()
		elif repeat_game == "n" or repeat_game == "no":
			exit()
		else:
			print colored("Not a valid input. Type (y/n).", "red")
			play_again()

play_buzzfeed_game()
play_again()


