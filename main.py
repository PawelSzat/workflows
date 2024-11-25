"""
Factourial counting
"""
def factorials(n):
    if n < 0:
        raise ValueError("Cannot be count")
    if not isinstance(n, int):
        raise TypeError("Must be intiger")

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial
