from random import randint
from termcolor import colored

""" This function will print out the results of the user's birthday and favorite animal. """

def guess_bday_fav_animal(month, dict1):
	bday_intro = "You were born on "
	fav_animal_intro = " are your favorite animal!"
	day_year = " " + str(randint(1, 31)) + ", " + str(randint(1980, 2001)) + "!\n"
	feb_day_year = " " + str(randint(1, 29)) + ", " + str(randint(1980, 2001)) + "!\n"
	if month == "February":
		return colored(bday_intro + month + feb_day_year + dict1[month][0] + fav_animal_intro + dict1[month][1], "magenta", attrs=["bold"])
	else:
		return colored(bday_intro + month + day_year + dict1[month][0] + fav_animal_intro + dict1[month][1], "magenta", attrs=["bold"])


fav_animal = {
			"January": ("Unicorns", u"\U0001F984"),
			"February": ("Penguins", u"\U0001F427"),
			"March": ("Dolphins", u"\U0001F42C"),
			"April": ("Pigs", u"\U0001F437"),
			"May": ("Lions", u"\U0001F981"),
			"June": ("Dogs", u"\U0001F436"),
			"July": ("Monkeys", u"\U0001F435"),
			"August": ("Pandas", u"\U0001F43C"),
			"September": ("Frogs", u"\U0001F438"),
			"October": ("Elephants", u"\U0001F418"),
			"November": ("Cats", u"\U0001F431"),
			"December": ("Horses", u"\U0001F434")
			}
