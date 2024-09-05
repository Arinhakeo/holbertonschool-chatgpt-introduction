#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a non-negative integer n using recursion.

    Args:
        n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.

    Example:
        factorial(4) returns 24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check that the script is being run with one argument
if len(sys.argv) != 2:
    print("Usage: ./factorial_recursive.py <non-negative integer>")
    sys.exit(1)

# Get the input integer from command line argument
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
