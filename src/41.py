import random
def random_sleep():
    # Generate a list of sleeping times between 0 and 59 seconds
    sleep_times = [random.randint(0, 59) for _ in range(random.randint(1, 6))]
    return min(sleep_times)

print(random_sleep())
