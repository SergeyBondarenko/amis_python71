def get_data():  # A function that get data from customer
    a = input("Enter data:")
    return int(a)


a = get_data()  # here variables is defined by the use of "get_data"
n = get_data()


def power(a, n):  # A function that elevates number into pow
    if n == 0:  # condition for pow = 0
        a = 1
    elif n == 1:  # condition for pow = 1
        a = a
    else:  # condition for other values of pow
        a = a*power(a, n-1)
        # variable is mulplied by the returned value of function
    return(a)


print(power(a, n))
