def getnumber():
    num = input("Enter number of elements in list: ")
    """
    This function is checking data(data must be int)
        
    Returns:
        a: integer, will be used in function "calculating"
        
    Raises:
        OverflowError
        
    Examples:
        print(getnumber())
        (if we enter 100)
        Data is correct
        100
        print(getnumber())
        (if we enter abc)
        Enter natural digit
        (if we enter 101)
        Data is correct
        101
    """
    if num.isdigit() is False:
        print("Enter natural digit")
        return getnumber()
    if len(num) < 1:
        print("Enter natural digit")
        return getnumber()
    else:
        if int(num) <= 0:
            print("Number of multiplying can't be < 0.")
            return getnumber()
        else:
            print("Data is correct")
    return int(num)


Num = getnumber()
digits = []


def getlist(num):
    """
    This function is creating list

    Args:
        num: integer, number of repeating

    Returns:
        list: list, list of digits

    Raises:
        OverflowError

    Examples:
        print(getlist())
        "[1,2,3,4,5]"
    """
    global digits
    if len(digits) < num:
        a = int(input("Enter element: "))
        digits.append(a)
        getlist(num)
    else:
        return digits
    return digits


inp_list = getlist(Num)
res = []
it = 1


def convert_list(input_list, iterator):
    """
    This function is reversing list

    Args:
        input_list: list, which is reversing
        iterator: integer, iterator, that points on element in list

    Returns:
        res: reversed list

    Raises:
        OverflowError
        ValueError

    Examples:
        print(min_f([1,2,3,4],0))
        "[4,3,2,1]"
        print(min_f([1,2,"a",3],0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    global res
    if len(input_list) == iterator-1:
        return res
    res.append(input_list[-iterator])
    return convert_list(input_list, iterator + 1)


print(convert_list(inp_list, it))
