import random


def hint(Num, n):
    num, n = str(num), str(n)
    correct = ["X"] * len(num)
    for i in range(min(len(num), len(n))):
        if num[i] == n[i]:
            correct[i] = num[i]
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
