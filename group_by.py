def group_by(func, iterable):
    """
    Create a dictionary, when the key is the results of the function on the iterable, and the value is list of the items
        that given this result.
    :param func:
    :param iterable:
    :return:dictionary of keys and list of  iterable objects.
    """
    return {func(i): list(filter(lambda word: func(word) == func(i), iterable)) for i in iterable}


if __name__ == "__main__":
    print(group_by(len, ["hi", "bye", "yo", "try"]))
