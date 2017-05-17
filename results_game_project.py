from random import randint
from termcolor import colored

""" This function will print out the results of the user's birthday and favorite animal. """

def guess_bday_fav_animal(month, dict1):
	bday_intro = "You were born on "
	fav_animal_intro = "Your favorite animals are "
	day_year = " " + str(randint(1, 31)) + ", " + str(randint(1980, 2001)) + "!\n"
	feb_day_year = " " + str(randint(1, 29)) + ", " + str(randint(1980, 2001)) + "!\n"
	if month == "February":
		return colored(bday_intro + month + feb_day_year + fav_animal_intro + dict1[month], "magenta", attrs=["bold"])
	else:
		return colored(bday_intro + month + day_year + fav_animal_intro + dict1[month], "magenta", attrs=["bold"])


fav_animal = {
			"January": "unicorns",
			"February": "penguins!",
			"March": "dolphins!",
			"April": "pigs!",
			"May": "lions!",
			"June": "dogs!",
			"July": "monkeys!",
			"August": "pandas!",
			"September": "frogs!",
			"October": "elephants!",
			"November": "cats!",
			"December": "horses!"
			}
