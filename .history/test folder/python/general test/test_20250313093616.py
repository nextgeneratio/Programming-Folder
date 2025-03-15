def calculate_powers(base, range_limit):
    for exponent in range(1, range_limit + 1):
        result = base ** exponent
        print(f"{base} to the power of {exponent} is {result}")


    if __name__ == "__main__":
        base = int(input("Enter the base number: "))
        range_limit = int(input("Enter the range limit: "))
        calculate_powers(base, range_limit)