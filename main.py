def factorials(n):
    if n < 0:
        raise ValueError("Nie można obliczyć silni dla liczb ujemnych.")
    if not isinstance(n, int):
        raise TypeError("Wartość musi być liczbą całkowitą.")

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial
