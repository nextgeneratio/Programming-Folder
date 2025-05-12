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
	    # store the follower count of
    # account1 in a variable
    sum1 = p1['follower_count']
     
    # store the follower count of 
    # account2 in a variable
    sum2 = p2['follower_count']
     
    # make an empty variable max, where
    # we will store the name of account
    # with highest followers, then compare
    # it with user input name.
    max = ""
     
    # if account1 has greater follower count
    if sum1 > sum2:
           
        # max is name of account1 
        max = p1['name']
    elif sum1 < sum2:
           
        # otherwise, if account2 has higher
        # follower count, 
        # max is name of account two.
        max = p2['name']
     
    # now compare the name of account with greater
    #follower count against the user input name,
    # if user is correct, return True
    if max == user_input:
        return True
    else:
          # otherwise return False
        return False

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

