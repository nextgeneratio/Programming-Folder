import random


def hint(Num, N):
    Num, N = str(Num), str(N)
    correct = ["X"] * len(Num)
    for i in range(min(len(Num), len(N))):
        if Num[i] == N[i]:
            correct[i] = Num[i]
    return "".join(correct)


num = random.randint(1, 100)

n = input("Enter a number between 1 and 100: ")
if n.isdigit():
    n = int(n)
else:
    print("Invalid input. Please enter a number between 1 and 100.")
    exit()
if n < 1 or n > 100:
    print("Invalid input. Please enter a number between 1 and 100.")
    exit()
if n == num:
    print("You guessed it!")
elif n != num:
    pass



