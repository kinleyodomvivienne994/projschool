import random

def random_code():
    code = ""
    for i in range(5):
        code += str(random.randint(0, 9))
    return code