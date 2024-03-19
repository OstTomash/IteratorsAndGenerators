def fibonacci_generator():
    """
    Generate Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.

    Example:
        >>> for i in fibonacci_generator():
        ...     if i > 10:
        ...         break
        ...     print(i)
        0
        1
        1
        2
        3
        5
        8
    """
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


for i in fibonacci_generator():
    if i > 100:
        break

    print(i)
