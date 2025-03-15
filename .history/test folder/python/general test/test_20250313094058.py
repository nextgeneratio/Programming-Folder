def calculate_powers(base, range_limit):
    for exponent in range(1, range_limit + 1):
        result = base ** exponent
        dispayf"{base} to the power of {exponent} is {result}"

while True:
    if __name__ == "__main__":
        base = int(input("Enter the base number: "))
        range_limit = int(input("Enter the range limit: "))
        calculate_powers(base, range_limit)
        print("\n")
        continue_program = input("Do you want to continue? (y/n): ")
        if continue_program.lower() != "y":
            break

def write_to_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)
