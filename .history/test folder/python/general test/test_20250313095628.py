def calculate_powers(base_number, limit):
    results = []
    for exponent in range(1, limit + 1):
        result = base_number ** exponent
        display = f"{base_number} to the power of {exponent} is {result:,}"
        print(display)
        results.append(display)
    return results

def write_to_file(file_name, content):
    with open(file_name, "w") as file:
        for line in content:
            file.write(line + "\n")

if __name__ == "__main__":
    while True:
        base = int(input("Enter the base number: "))
        range_limit = int(input("Enter the range limit: "))
        results = calculate_powers(base_number=base, limit=range_limit)
        file_name = f"base_{base}_powers.txt"
        write_to_file(file_name, results)
        print(f"Results have been written to {file_name}\n")
        continue_program = input("Do you want to continue? (y/n): ")
        if continue_program.lower() != "y":
            break