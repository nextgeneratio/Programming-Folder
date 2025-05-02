import random

def secret_code():
    # Generate a random 4-digit number with unique digits
    digits = set()
    while len(digits) < 4:
        digits.add(str(random.randint(1, 9)))
    
    # Convert the set of unique digits to a string
    sec_num = ''.join(digits)
    return sec_num

def get_guess():
    # Prompt the user for a 4-digit guess with unique digits
    while True:
        guess = input("Enter a 4-digit number with unique digits: ")
        if len(guess) == 4 and len(set(guess)) == 4 and guess.isdigit():
            return guess
        else:
            print("Invalid input. Please enter exactly 4 unique digits.")
    
def hint(guess, sec_num):
    """
    Provide hints based on the guess and secret number.
    Bulls: Correct digit in the correct position.
    Cows: Correct digit in the wrong position.
    """
    bulls = 0
    cows = 0

    # Check for Bulls (correct digit in the correct position)
    for i in range(4):
        if guess[i] == sec_num[i]:
            bulls += 1

    # Check for Cows (correct digit in the wrong position)
    for i in range(4):
        if guess[i] in sec_num and guess[i] != sec_num[i]:
            cows += 1

    return f"You got: {bulls} Bulls & {cows} Cows"


def display_result(player1, player2, num_)
