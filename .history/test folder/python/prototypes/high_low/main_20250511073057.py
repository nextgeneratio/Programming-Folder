# since we want to randomly select an 
# option from the data, we need random 
# module
import random

# import the game data
from game_data import data

# import the ASCII art to display.
from art import logo
from art import vs

# IDEs like Replit have their own "clear" 
# functions to clear the output console:
from replit import clear

# If you are using some other IDE, this import 
# will not work.
# You will have to use clear of that IDE
# For example, in Google Colab Notebook we have:
from googl.colab import output

def assign():
	return random.choice(data)

def compare(p1, p2, user_input):
	pass

def play_higher_lower():
	pass


want_to_play = input("Do you want to play Higher Lower? (y/n)\n").lower()
if want_to_play == 'y':
	clear()
	play_higher_lower()
elif want_to_play == 'n':
	print("Program Exit Successful.")
else:
	print("Invalid Input, Program Exited.")

