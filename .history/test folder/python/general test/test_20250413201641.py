def get_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b

def add_numbers(x, y):
    return x + y

def display_result(result):
    print("The sum is:", result)

def main():
    num1, num2 = get_numbers()
    total = add_numbers(num1, num2)
    display_result(total)

main()
