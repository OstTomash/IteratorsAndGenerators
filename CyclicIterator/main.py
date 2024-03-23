class CyclicIterator:
    """
    An iterator that cyclically iterates over a given collection indefinitely.

    Args:
    collection (iterable): The iterable collection to iterate over cyclically.
    """

    def __init__(self, collection):
        """
        Initializes the CyclicIterator with the given collection.

        Args:
        collection (iterable): The iterable collection to iterate over cyclically.
        """
        self.values = collection
        self.index = 0

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next element in the cyclic iteration.
        """
        if self.index >= len(self.values):
            self.index = 0
        result = self.values[self.index]
        self.index += 1
        return result


for i in CyclicIterator([1, 2, 3]):
    print(i)
