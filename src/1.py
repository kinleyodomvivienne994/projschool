import random

def get_random_name():
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return random.choice(names)

def main():
    name = get_random_name()
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
