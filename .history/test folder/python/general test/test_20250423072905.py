import random


def hint(Num, N):
    Num, N = str(Num), str(N)
    correct = ["X"] * len(Num)
    for i in range(min(len(Num), len(N))):
        if Num[i] == N[i]:
            correct[i] = Num[i]
    return "".join(correct)

start = 

num = random.randint(1, 100)
attempts = 0
print("Welcome to the number guessing game!")

while True:
    n = input("Enter a number between 1 and 100: ")
    if n.isdigit():
        n = int(n)
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    if n < 1 or n > 100:
        print("Invalid input. Please enter a number between 1 and 100.")
        continue
    attempts += 1
    if n == num:
        print("You guessed it!")
    elif n != num:
        pass



