res = input("Enter your list: ").split()
it = 0
max_el = int(res[it])


def convert_list(result, iterator):
    """
    This function is converting all elements of list into float type

    Args:
        result: list, that is converting
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
    if iterator < len(result):
        result[iterator] = float(result[iterator])
        return convert_list(result, iterator + 1)
    return result


res1 = convert_list(res, it)


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


max_elem = max_f(res, it)
s = 0


def count_max(result1, iterator):
    """
     This function is counting number ofmax element

     Args:
         result1: list, where max is counting
         iterator: integer, iterator, that points on element in list

     Returns:
         s: integer, number of max elements

     Raises:
         OverflowError
         ValueError

     Examples:
         print(max_f([1,2,3,4],0))
         "1"
         print(max_f([1,2,"a",3],0))
         Traceback (most recent call last):
             ...
         ValueError
     """
    global s
    global max_elem
    if iterator < len(result1) - 1:
        if result1[iterator] == max_elem:
            s += 1
            return count_max(result1, iterator + 1)
        else:
            return count_max(result1, iterator + 1)
    elif iterator == len(result1) - 1:
        if result1[iterator] == max_elem:
            s += 1
            return count_max(result1, iterator + 1)
        else:
            return count_max(result1, iterator + 1)
    return s


print("The number of max elements is:", count_max(res1, it))
