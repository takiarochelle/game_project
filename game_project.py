from random import randint

# Buzzfeed style game where the user creates a coffee drink and the game will guess their birth month.
# One user game
# Define the values the user can input for each input

def size_drink():
	# If size is not a valid option return an error and exit the program
	# Return the user's value for use later
	size_list = ["small", "medium", "large"]
	size = raw_input("Choose a size (small, medium, large): ")
	if size not in size_list:
		print size + " is not an option. Try again!"
		size_drink()
	else:
		return size

def temp_drink():
	# If temp is not a valid option return an error and exit the program
	# Return the user's value for use later
	temp_list = ["iced", "hot"]
	temp = raw_input("Choose a temperature (iced or hot): ")
	if temp not in temp_list:
		print size + " is not an option. Try again!"
	else:
		return temp

def drink_type():
	# If drink is not a valid option return an error and exit the program
	# Return the user's value for use later
	drink_list = ["latte", "frapp", "black coffee"]
	drink = raw_input("Choose a drink (latte, frapp, black coffee): ")
	if drink not in drink_list:
		print drink + " is not an option. Try again!" 
	else:
		return drink

def milk_type():
	# If milk is not a valid option return an error and exit the program
	# Return the user's value for use later
	milk_list = ["2%", "whole", "soy", "none"]
	milk = raw_input("Choose a milk option (2%, whole, soy, none): ")
	if milk not in milk_list:
		print milk + " is not an option. Try again!"
	else:
		return milk

print "Create a Drink and we'll Guess Your Birth Month!\n"
print "Let's Play!!"

def buzzfeed_game():
	size = size_drink()
	temp = temp_drink()
	drink = drink_type()
	milk = milk_type()

	intro = "You were born in "

	if size == "small":
 		if temp == "hot":
 			print intro + "December!"
 		elif temp == "iced":
 			month = randint(1, 3)
 			if month == 1:
 				print intro + "January!"
 			else:
 				print intro + "February!"
	elif size == "medium":
		if temp == "hot":
			if drink == "latte" or drink == "frapp":
				print intro + "October!"
			else:
				print intro + "November!"
		elif temp == "iced":
			print intro + "September!"
	elif size == "large":
		if temp == "hot":
			if drink == "black coffee":
				spring_month = randint(3, 6)
				if spring_month == 3:
					print intro + "March!"
				else:
					print intro + "April!"
			else:
				print intro + "May!"
		elif temp == "iced":
			if drink == "latte" or drink == "frapp":
				if milk == "whole":
					print intro + "June!"
				elif milk == "2%" or milk == "none":
					print intro + "July!"
				else:
					print intro + "August!"


					