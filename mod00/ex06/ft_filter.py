def ft_filter(func, iterable):
    """
    ft_filter is an implementation of the built-in filter function.
    It constructs an iterator from those elements of iterable
    for which function returns true.
    if func is None, it returns the items that are true.

    :param func: a function that tests each element of the iterable
    to determine
    if it should be included in the result.
    :param iterable: an iterable collection of elements to be filtered.
    """
    if func is None:
        func = True
    return (item for item in iterable if func(item))


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6]

    y = list(filter(lambda n: n % 2 == 0, x))
    z = list(ft_filter(lambda n: n % 2 == 0, x))
    print("DocString original function", filter.__doc__)
    print("DocString own function", ft_filter.__doc__)
    print(y)
    print(z)
