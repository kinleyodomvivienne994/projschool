import random

def generate_random_code():
    # Generate a random string of 5 characters
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))
    
    return random_string

# Example usage: Get a random code
random_code = generate_random_code()
print("Generated Random Code:", random_code)
