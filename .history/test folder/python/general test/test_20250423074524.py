import random


def hint(Num, N):
    Num, N = str(Num), str(N)
    correct = ["X"] * len(Num)
    for i in range(0, len(N)):
        if Num[i] == N[i]:
            correct[i] = Num[i]
    return "You got " + " ".join(correct) + " correct!"

start = 1
stop = 100

num = random.randint(start, stop)


def Attempts():
    attempts = 0
    while True:
        n = input("Enter a number between 1 and 100: ")
        if n.isdigit():
            n = int(n)
        else:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        if n < start or n > stop:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        attempts += 1
        if n == num:
            print("You guessed it!")
        elif n != num:
            print(hint(num, n))
            print("Try again!")
    return attempts


def main():
    print("Welcome to the number guessing game!")
    num_players = input("Enter the number of players: ")
    while True:
        if num_players.isdigit():
            num_players = int(num_players)
            break
        else:
            print("Invalid input. Please enter a number.")
            continue
        if num_players < 1:
            print("Invalid input. Please enter a number greater than 0.")
            continue
        
    
