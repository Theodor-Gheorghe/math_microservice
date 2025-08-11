def calculate_factorial(n):
    """
    Calculates the factorial of n.
    Ex: factorial(5) = 5 * 4 * 3 * 2 * 1 = 120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def calculate_factorial(n):
    # Calculates the factorial of an integer n.
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_pow(base, exponent):
    # Calculates power: base^exponent
    return base ** exponent


def calculate_fibonacci(n):
    # Calculates the n-th Fibonacci number
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b