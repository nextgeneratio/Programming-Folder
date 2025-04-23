import random


num = random.randint(1, 100)

n = input("Enter a number between 1 and 100: ")
if n.isdigit():
    n = int(n)
else:
    print("Invalid input. Please enter a number between 1 and 100.")
    exit()
    
