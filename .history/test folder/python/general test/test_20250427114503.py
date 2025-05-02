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


def display_result(player1_guess_count, player2_guess_count):
    """
    Display the result of the game based on the number of guesses.
    """
    if player1_guess_count < player2_guess_count:
        print(f"Player 1 wins with {player1_guess_count} guesses!")
    elif player2_guess_count < player1_guess_count:
        print(f"Player 2 wins with {player2_guess_count} guesses!")
    else:
        print("It's a tie!")

def main():
    print("Welcome to the Bulls and Cows game!")
    print("Two players will try to guess a 4-digit secret number with unique digits.")
    print("The player with fewer guesses wins.")

    # Generate the secret number
    sec_num = secret_code()

    # Initialize guess counts for both players
    player1_guess_count = 0
    player2_guess_count = 0

    # Player 1's turn
    print("\nPlayer 1's turn:")
    while True:
        guess = get_guess()
        player1_guess_count += 1
        print(hint(guess, sec_num))
        if guess == sec_num:
            print(f"Player 1 guessed the secret number in {player1_guess_count} tries!")
            break

    # Player 2's turn
    print("\nPlayer 2's turn:")
    while True:
        guess = get_guess()
        player2_guess_count += 1
        print(hint(guess, sec_num))
        if guess == sec_num:
            print(f"Player 2 guessed the secret number in {player2_guess_count} tries!")
            break

    # Display the result of the game
    display_result(player1_guess_count, player2_guess_count)

if __name__ == "__main__":
