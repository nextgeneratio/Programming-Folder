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
    
def hint(guess, sec_num):
    # Provide hints based on the guess and secret number
    if guess == sec_num:
        return "Congratulations! You've guessed the correct number."
    
    hints = []
    for i in range(4):
        if guess[i] == sec_num[i]:
            hints.append("Fermi")
        elif guess[i] in sec_num:
            hints.append("Pico")
    
    if not hints:
        return "Bagels"
    
    return ' '.join(hints)

