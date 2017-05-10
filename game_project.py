from random import randint
from termcolor import colored

"""

A Buzzfeed style game where the user creates a coffee drink.
From the user's input the game will guess the user's birthday. 
This is a one user game.

"""

def size_drink():
	# If size is not a valid option return an error and exit the program
	# Return the user's value for use later
	size_list = ["small", "medium", "large"]
	size = raw_input("Choose a size (small, medium, large):\n>>> ")
	if size not in size_list:
		print colored(size + " is not an option. Try again!", "red")
		return size_drink()
	else:
		return size

def temp_drink():
	# If temp is not a valid option return an error and exit the program
	# Return the user's value for use later
	temp_list = ["iced", "hot"]
	temp = raw_input("Choose a temperature (iced or hot):\n>>> ")
	if temp not in temp_list:
		print colored(temp + " is not an option. Try again!", "red")
		return temp_drink()
	else:
		return temp

def drink_type():
	# If drink is not a valid option return an error and exit the program
	# Return the user's value for use later
	drink_list = ["latte", "frapp", "coffee"]
	drink = raw_input("Choose a drink (latte, frapp, coffee):\n>>> ")
	if drink not in drink_list:
		print colored(drink + " is not an option. Try again!", "red")
		return drink_type() 
	else:
		return drink

def milk_type():
	# If milk is not a valid option return an error and exit the program
	# Return the user's value for use later
	milk_list = ["2%", "whole", "soy", "none"]
	milk = raw_input("Choose a milk option (2%, whole, soy, none):\n>>> ")
	if milk not in milk_list:
		print colored(milk + " is not an option. Try again!", "red")
		return milk_type()
	else:
		return milk

bday_description = {
			"Jan": "You are a born leader with an obsession for tacos!", 
			"Feb": "You are a rebel with a love of dolphins!",
			"March": "You like skipping in fields of daisies while listening to the Sound of Music!",
			"April": "You enjoy traveling and fighting crime in your spare time!",
			"March": "You enjoy watching the sunset while doing cartwheels on the beach"
			}

""" Generating random birthdays and years """

year = randint(1970, 2001)
day = randint(1, 31)
feb_day = randint(1, 29)
day_year = str(day) + ", " + str(year) + "! "
feb_day_year = str(feb_day) + ", " + str(year) + "! "

print colored("Build a drink and we'll guess your birthday!\n", "yellow", attrs=["bold"])
print colored("Let's Play!!\n", "yellow", attrs=["bold"])
print colored("Enter your answer after the >>>\n", "blue", attrs=["bold"])


def buzzfeed_game():
	size = size_drink()
	temp = temp_drink()
	drink = drink_type()
	milk = milk_type()

	intro = "You were born on "

	if size == "small":
 		if temp == "hot":
 			print colored(intro + "December " + day_year, "magenta", attrs=["bold"])
 		elif temp == "iced":
 			winter_month = randint(1, 3)
 			if winter_month == 1:
 				print intro + "January " + day_year + bday_description["Jan"]
 			else:
 				print intro + "February " + feb_day_year
	elif size == "medium":
		if temp == "hot":
			if drink == "latte" or drink == "frapp":
				print intro + "October " + day_year
			else:
				print intro + "November " + day_year
		elif temp == "iced":
			print intro + "September " + day_year
	elif size == "large":
		if temp == "hot":
			if drink == "coffee":
				spring_month = randint(3, 6)
				if spring_month == 3:
					print intro + "March " + day_year
				else:
					print intro + "April " + day_year
			else:
				print intro + "May " + day_year
		elif temp == "iced":
			if drink == "latte" or drink == "frapp":
				if milk == "whole" or milk == "none":
					print intro + "June " + day_year
				else:
					print intro + "July " + day_year
			else:
				print intro + "August " + day_year


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

buzzfeed_game()
play_again()


