def calculate_powers(base_number, limit):
    power_results = []
    for exponent in range(1, limit + 1):
        result = base_number ** exponent
        display = f"{base_number} to the power of {exponent} is {result:,}"
        print(display)
        power_results.append(display)
    return power_results

def write_to_file(output_file_name, content):
    with open(output_file_name, "w", encoding="utf-8") as file:
        for line in content:
            file.write(line + "\n")

if __name__ == "__main__":
    while True:
        base = int(input("Enter the base number: "))
        range_limit = int(input("Enter the range limit: "))
        results = calculate_powers(base_number=base, limit=range_limit)
        file_name = f"base_{base}_powers.txt"
        write_to_file(output_file_name=file_name, content=results)
        print(f"Results have been written to {file_name}\n")
        continue_program = input("Do you want to continue? (y/n): ")
        if continue_program.lower() != "y":
            break
