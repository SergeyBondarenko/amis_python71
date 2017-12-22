res = input("Enter your list: ").split()
it = 0
a = []


def groups(search_list, iterator):
    """
    This function is counting elements

    Args:
        search_list: list, where elements in groups is counting
        iterator: integer, iterator, that points on element in list

    Returns:
        a: max count of elements in one group

    Raises:
        OverflowError
        ValueError

    Examples:
        print(groups([1, 1, 1, 2, 2, 3], 0))
        3
        print(groups([1, 1, "a", 2, 2, 3], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if iterator == len(search_list):
        return max(a)
    list_two = "".join(search_list)
    count_el = search_list.count(search_list[iterator])
    if (count_el - iterator)*str(search_list[iterator]) in list_two:
        a.append(count_el - iterator)
    return groups(search_list, iterator + 1)


print(groups(res, it))
