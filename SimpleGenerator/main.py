def count_down_generator(num):
    """
        Generate a countdown from a given number to 0.

        Args:
            n (int): The number to start the countdown from.

        Yields:
            int: The next number in the countdown sequence, starting from 'n' down to 0.

        Example:
            >>> for i in count_down_generator(3):
            ...     print(i)
            3
            2
            1
            0
        """
    while num >= 0:
        yield num
        num -= 1


custom_input = int(input('Enter a number: '))

for i in count_down_generator(custom_input):
    print(i)
