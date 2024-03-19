def permutation_generator(numbers_list):
    """
    Generate all possible permutations of the elements in the given list.

    Args:
        lst (list): The list of elements.

    Yields:
        list: The next permutation.

    Example:
        >>> for i in permutation_generator([1, 2, 3]):
        ...     print(i)
        [1, 2, 3]
        [1, 3, 2]
        [2, 1, 3]
        [2, 3, 1]
        [3, 1, 2]
        [3, 2, 1]
    """
    stack = [(numbers_list, [])]
    while stack:
        items, perm = stack.pop()
        if not items:
            yield perm
        for i, item in enumerate(items):
            remaining = items[:i] + items[i + 1:]
            stack.append((remaining, perm + [item]))


for i in permutation_generator([1, 2, 3]):
    print(i)