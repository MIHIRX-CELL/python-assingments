def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Sample usage
number = 5
try:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
except ValueError as e:
    print(e)

