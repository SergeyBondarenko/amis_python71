def input_text(text):
    """
        This function is checking data(data can be any)

        Returns:
            text: string, will be used in function "del_after_el"

        Raises:
            None

        Examples:
            print(getnumber(''))
            "''"
    """
    return text


def del_after_el(text, ind):
    """
    This function is deletes the first 3 characters from the words starting with the element "a"

    Args:
        text: list, list of all items entered by user
        ind: integer, iterator, that points on element in list

    Returns:
        text: string

    Raises:
        None

    Examples:
        print(text(1 addd 3 4 0))
        "1 a 3 4 0"
    """

    text = text.split()
    if text.index[ind][0] == 'a':
        text[ind] = text[ind][:-3]
        return ' '.join(text)
    else:
        return del_after_el(text, ind + 1)


print(del_after_el(input_text(input("Enter text: ")), 0))
