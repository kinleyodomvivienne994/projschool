def sum_of_squares(n):
    """
    Calculate the sum of squares of first n natural numbers.
    
    Example:
    >>> sum_of_squares(10)
    385

    :param n: int - number of initial natural numbers to square and add up.
    :return: int - sum of squares of first n natural numbers.
    """
    return sum(x**2 for x in range(1, n+1))

# Test the function with a sample input
print(sum_of_squares(5))  # Expected output: 55
