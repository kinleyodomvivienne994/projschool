def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("除数不能为零")
    return x / y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def power(x, n):
    return x ** n
