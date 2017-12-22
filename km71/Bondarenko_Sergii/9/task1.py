def get_data():  # A function that get data from customer
    b = True
    while b:  # cycle that allows customer to reenter the data
        a = input("Enter coordinate:")
        for i in a:  # cycle for checking entered data
            if "0123456789".find(a) == -1:  # condition for nondigits
                res = "You have entered not a digit. Enter a digit."
                continue
            else:  # condition for correct data
                b = False
                res = "Data is correct."
        print(res)
    return float(a)


x1 = get_data()  # here variables is defined by the use of "get_data"
y1 = get_data()
x2 = get_data()
y2 = get_data()


def distance(x1, y1, x2, y2):
    # A function, that calculate distance between points
    distance = ((x2) - (x1))**2 + ((y2) - (y1)**2)**0.5
    return distance


print(distance(x1, y1, x2, y2))  # here the function is called
