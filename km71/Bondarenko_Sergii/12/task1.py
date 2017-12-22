res = input("Enter your list: ").split()
it = 0


def convert_list(ress, iterator):
    """
    This function is converting all elements of list into float type

    Args:
        ress: list, that is converting
        iterator: integer, iterator, that points on element in list

    Returns:
        ress: converted list

    Raises:
        OverflowError
        ValueError

    Examples:
        print(convert_list(["1", "2", "3"], 0))
        [1, 2, 3]
        print(convert_list(["a", "2", "3"], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if iterator < len(ress):
        ress[iterator] = float(ress[iterator])
        return convert_list(ress, iterator + 1)
    return ress


res1 = convert_list(res, it)
max_el = res1[it]


def max_f(inp_list, iterator):
    """
    This function is calculating max element

    Args:
        inp_list: list, where max is searching
        iterator: integer, iterator, that points on element in list

    Returns:
        max_el: integer

    Raises:
        OverflowError
        ValueError

    Examples:
        print(max_f([1,2,3,4],0))
        "4"
        print(max_f([1,2,"a",3],0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    global max_el
    if iterator < len(inp_list)-1:
        if max_el < inp_list[iterator+1]:
            max_el = inp_list[iterator + 1]
            return max_f(inp_list, iterator + 1)
        else:
            return max_f(inp_list, iterator + 1)
    return max_el


max_elem = max_f(res1, it)
test = []


def del_max_el(resa, max_element, iterator):
    """
    This function is deleting all elements, which values are equal to the value of max element

    Args:
        resa: list, where second max is searching
        iterator: integer, iterator, that points on element in list
        max_element: first max_element

    Returns:
        test: list, list without first max element

    Raises:
        OverflowError
        ValueError

    Examples:
        print(del_max_el([1, 2, 3, 4], 4, 0))
        [1, 2, 3]
        print(del_max_el([1, "a", 3, 4], 4, 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    global test
    if iterator < len(resa) - 1:
        if resa[iterator] != max_element:
            test.append(resa[iterator])
            return del_max_el(resa, max_element, iterator + 1)
        else:
            return del_max_el(resa, max_element, iterator + 1)
    elif iterator == len(resa)-1:
        if resa[iterator] != max_element:
            test.append(resa[iterator])
    return test


del_max_el(res1, max_elem, it)
it = 0




def sec_max_f(inp_list, iterator):
    """
    This function is calculating second max element element

    Args:
        inp_list: list, where second max is searching
        iterator: integer, iterator, that points on element in list

    Returns:
        sec_max_el: integer

    Raises:
        OverflowError
        ValueError

    Examples:
        print(sec_max_f([1, 2, 3], 0))
        "3"
        print(sec_max_f([1, 2, "b"], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    global sec_max_el
    if iterator < len(inp_list) - 1:
        if sec_max_el < inp_list[iterator+1]:
            sec_max_el = inp_list[iterator + 1]
            return sec_max_f(inp_list, iterator + 1)
        else:
            return sec_max_f(inp_list, iterator + 1)
    return sec_max_el

if len(test) > 0:
    sec_max_el = test[it]
    print("Second max element is:", sec_max_f(test, it))
else:
    print("The list does not have second max element.")

