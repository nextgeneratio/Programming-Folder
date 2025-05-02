import random

def secret_code():
    # Generate a random 4-digit number and convert it to a list of characters
    sec_num = list(str(random.randint(1000, 9999)))
    
    # Ensure no two consecutive digits are the same
    for i in range(3):  # Loop only up to the third digit to avoid index out of range
        if sec_num[i] == sec_num[i + 1]:
            sec_num[i] = str(random.randint(0, 9))
    
    # Join the list back into a string
    sec_num = ''.join(sec_num)
    return sec_num

print(secret_code())

