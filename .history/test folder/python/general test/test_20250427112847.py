import random

def secret_code():
    sec_num = list(random.randint(1000, 9999))
    for i in range(4):
        if str(sec_num[i]) == str(sec_num[i + 1]):
            
        
    return sec_num

print(secret_code())

