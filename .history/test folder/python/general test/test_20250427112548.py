import random

def secret_code():
    sec_num = random.randint(1000, 9999)
    for i in range(4):
        if sec_num[i] == sec_num[i + 1]:
            sec_num = random.randint(1000, 9999)

