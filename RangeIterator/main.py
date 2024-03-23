class RangeIterator:
    """
    An iterator class that iterates over a range of integers with specified start, end, and step.

    Args:
        start (int): The starting value of the range.
        end (int): The ending value of the range.
        step (int): The step size by which to increment or decrement the iterator.

    Raises:
        StopIteration: Raised when the iterator reaches or exceeds the end value.

    Returns:
        int: The next value in the range sequence.

    Example:
        for i in RangeIterator(1, 10, 2):
            print(i)
    """
    def __init__(self, start: int, end: int, step: int) -> None:
        """
        Initializes the RangeIterator object.

        Args:
            start (int): The starting value of the range.
            end (int): The ending value of the range.
            step (int): The step size by which to increment or decrement the iterator.
        """
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next value in the range sequence.

        Raises:
            StopIteration: Raised when the iterator reaches or exceeds the end value.

        Returns:
            int: The next value in the range sequence.
        """
        if self.value >= self.end:
            raise StopIteration
        result = self.value
        self.value += self.step
        return result


for i in RangeIterator(1, 10, 2):
    print(i)
