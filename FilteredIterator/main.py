class FilterIterator:
    """
    An iterator that filters values based on a provided function.

    Args:
    iterable (iterable): The iterable sequence to iterate over.
    filter_func (function): The function used for filtering elements.
    """

    def __init__(self, iterable, filter_func):
        """
        Initializes the FilterIterator with the given iterable and filter function.

        Args:
        iterable (iterable): The iterable sequence to iterate over.
        filter_func (function): The function used for filtering elements.
        """
        self.values = iterable
        self.filter_func = filter_func
        self.index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next element in the iteration if it satisfies the filter function.

        Raises:
        StopIteration: If there are no more elements left in the iteration.

        Returns:
        Any: The next element in the iteration.
        """
        while self.index < len(self.values):
            element = self.values[self.index]
            self.index += 1
            if self.filter_func(element):
                return element
        raise StopIteration


f_iter = FilterIterator([1, 2, 3, 4], lambda x: x % 2 == 0)
while True:
    try:
        print(next(f_iter))
    except StopIteration:
        break
