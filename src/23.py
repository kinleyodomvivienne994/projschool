def calculate_gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

print(calculate_gcd(8, 12))
