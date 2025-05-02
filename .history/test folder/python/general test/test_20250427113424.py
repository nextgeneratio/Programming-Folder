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
    # Prompt the user for a 4-digit guess
    while True:
        guess = input("Enter the guessing number: ")
        if len(guess) == 4 and len(set(guess)) == 4 and guess.isdigit():
            return guess
        else:
            print("Invalid input. Please try again.")
    
    

