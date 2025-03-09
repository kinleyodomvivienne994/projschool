import random

def get_random_number(n):
    """
    Generate a random number between 1 and n (inclusive)
    """
    return random.randint(1, n)

def get_random_letter(s):
    """
    Generate a random letter from the string s
    """
    return random.choice(s)

def get_random_string(n, alphabet):
    """
    Generate a random string of length n using the characters in alphabet
    """
    return ''.join(random.choices(alphabet, k=n))
