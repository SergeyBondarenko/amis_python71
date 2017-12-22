def get_data():  # A function that get data from customer
    b = True
    while b:
        a = input("Enter data:")
        if int(a) < 0:
            print("Enter digit > 0")
            continue
        else:
            b = False
            print("Data is correct")
    return int(a)


a = get_data()  # here variables is defined by the use of "get_data"
n = get_data()


def power(a, n):
    c = a
    if n == 0:
        a = 1
    elif n == 1:
        a = a
    else:
        for mult in range(n-1):
            a = a*c
    return a


print(power(a, n))
