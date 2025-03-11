# Python code here
import random

def get_random_number(max_value):
    return random.randint(1, max_value)

def get_random_string(length=10):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(length))
