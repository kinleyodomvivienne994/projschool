import math

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    print(f"The greatest common divisor (GCD) of {num1} and {num2} is {calculate_gcd(num1, num2)}")

if __name__ == "__main__":
    main()
