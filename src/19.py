def calculate_average(numbers):
    if len(numbers) == 0:
        return None
    total = sum(numbers)
    average = total / len(numbers)
    return round(average, 2)

numbers = [10, 20, 30, 40, 50]
print("The average is:", calculate_average(numbers))
