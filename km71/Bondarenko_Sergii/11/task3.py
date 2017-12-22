def getnumber():
    numb = input("Enter number of elements in list: ")
    """
    This function is checking data(data must be int)
        
    Returns:
        a: integer, will be used in function "calculating"
        
    Raises:
        OverflowError
        
    Examples:
        print(getnumber())
        "Data is correct"
        "100"
        print(getnumber())
        "Enter natural digit"
        "Data is correct"
        "101"
    """
    if numb.isdigit() is False:
        print("Enter natural digit")
        return getnumber()
    if len(numb) < 1:
        print("Enter natural digit")
        return getnumber()
    else:
        if int(numb) <= 0:
            print("Number of multiplying can't be < 0.")
            return getnumber()
        else:
            print("Data is correct")
    return int(numb)


Num = getnumber()
digits = []


def getlist(number):
    """
    This function is creating list

    Args:
        number: integer, number of repeating

    Returns:
        list: list, list of digits

    Raises:
        OverflowError

    Examples:
        print(getlist())
        "[1,2,3,4,5]"
    """
    global digits
    if len(digits) < number:
        a = int(input("Enter element: "))
        digits.append(a)
        getlist(number)
    else:
        return digits
    return digits


res = getlist(Num)
it = 0
min_el = res[it]


def min_f(inp_list, iterator):
    """
    This function is calculating minimal element

    Args:
        inp_list: list, where min is searching
        iterator: integer, iterator, that points on element in list

    Returns:
        min_el: integer

    Raises:
        OverflowError
        ValueError

    Examples:
        print(min_f([1,2,3,4],0))
        "1"
        print(min_f([1,2,"a",3],0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    global min_el
    if iterator < len(inp_list) - 1:
        if min_el > inp_list[iterator+1]:
            min_el = inp_list[iterator + 1]
            return min_f(inp_list, iterator + 1)
        else:
            return min_f(inp_list, iterator + 1)
    return min_el


print(min_f(res, it))
