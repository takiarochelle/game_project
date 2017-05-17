from random import randint
from termcolor import colored
from results_game_project import guess_bday_fav_animal, fav_animal
import emoji

"""

A Buzzfeed style game where the user creates a boba drink.
From the user's input the game will guess the user's birthday and favorite animal. 
This is a one user game.

"""

def choose_drink_size():
	# If user's input is not in size_list return an error and prompt the user for input again.
	# Return the user's value
	size_list = ["small", "medium", "large"]
	size = raw_input("Choose a size (small, medium, large)\n>>> ")
	if size not in size_list:
		print colored(size + " is not an option. Try again!", "red")
		return choose_drink_size()
	else:
		return size

def choose_pearls():
	# If user's input is not in pearls_list return an error and prompt the user for input again. 
	# Return the user's value
	pearls_list = ["yes", "no"]
	pearls = raw_input("Would you like pearls? (yes or no)\n>>> ")
	if pearls not in pearls_list:
		print colored(pearls + " is not an option. Try again!", "red")
		return choose_pearls()
	else:
		return pearls

def choose_sweetness_level():
	# If user's input is not in sweetness_list return an error and prompt the user for input again.
	# Return the user's value
	sweetness_list = ["0%", "50%", "100%"]
	sweetness = raw_input("Pick your sugar sweetness level: (0%, 50%, 100%)\n>>> ")
	if sweetness not in sweetness_list:
		print colored(sweetness + " is not an option. Try again!", "red")
		return choose_sweetness_level() 
	else:
		return sweetness

def choose_flavor():
	# If user's input is not in flavor_list return an error and propmt the user for input again.
	# Return the user's value
	flavor_list = ["taro", "milk tea", "oolong", "wintermelon"]
	flavor = raw_input("Choose a flavor (taro, milk tea, oolong, wintermelon)\n>>> ")
	if flavor not in flavor_list:
		print colored(flavor + " is not an option. Try again!", "red")
		return choose_flavor()
	else:
		return flavor


def play_buzzfeed_game():
	print colored("\nCreate a boba drink and we'll guess your birthday and favorite animal!\nChoose from options given.\nLet's Play!!!", "yellow", attrs=["bold"])

	size = choose_drink_size()
	pearls = choose_pearls()
	sweetness = choose_sweetness_level()
	flavor = choose_flavor()

	if size == "small":
 		if pearls == "yes":
 			print guess_bday_fav_animal("December", fav_animal) + u"\U0001F434"
 		elif pearls == "no":
 			winter_month = randint(1, 3)
 			if winter_month == 1:
 				print guess_bday_fav_animal("January", fav_animal) + u"\U0001F984"
 			else:
 				print guess_bday_fav_animal("February", fav_animal) + u"\U0001F427"
	elif size == "medium":
		if pearls == "yes":
			if sweetness == "0%" or sweetness == "100%":
				print guess_bday_fav_animal("October", fav_animal) + u"\U0001F418"
			else:
				print guess_bday_fav_animal("November", fav_animal) + u"\U0001F98A"
		elif pearls == "no":
			print guess_bday_fav_animal("September", fav_animal) + u"\U0001F438"
	elif size == "large":
		if pearls == "yes":
			if sweetness == "50%" or sweetness == "0%":
				if flavor == "taro" or flavor == "wintermelon":
					print guess_bday_fav_animal("March", fav_animal) + u"\U0001F42C"
				else:
					print guess_bday_fav_animal("April", fav_animal) + u"\U0001F437"
			else:
				print guess_bday_fav_animal("May", fav_animal) + u"\U0001F981"
		elif pearls == "no":
			if sweetness == "100%" or sweetness == "50%":
				if flavor == "milk tea" or flavor == "taro":
					print guess_bday_fav_animal("June", fav_animal) + u"\U0001F436"
				elif flavor == "oolong" or flavor == "wintermelon":
					print guess_bday_fav_animal("July", fav_animal) + u"\U0001F435"
			else:
				print guess_bday_fav_animal("August", fav_animal) + u"\U0001F43C"


def play_again():
	while True:
		repeat_game = raw_input("Would you like to play again? (Type y/n): ")
		if repeat_game == "y" or repeat_game == "yes":
			play_buzzfeed_game()
		elif repeat_game == "n" or repeat_game == "no":
			exit()
		else:
			print colored("Not a valid input. Type (y/n).", "red")
			play_again()

play_buzzfeed_game()
play_again()


