x_coord = []
y_coord = []
x_coord.append(int(input("Enter x1 coordinate:")))
y_coord.append(int(input("Enter y1 coordinate:")))
x_coord.append(int(input("Enter x2 coordinate:")))
y_coord.append(int(input("Enter y2 coordinate:")))
x_coord.append(int(input("Enter x3 coordinate:")))
y_coord.append(int(input("Enter y3 coordinate:")))
x_coord.append(int(input("Enter x4 coordinate:")))
y_coord.append(int(input("Enter y4 coordinate:")))
x_coord.append(int(input("Enter x5 coordinate:")))
y_coord.append(int(input("Enter y5 coordinate:")))
x_coord.append(int(input("Enter x6 coordinate:")))
y_coord.append(int(input("Enter y6 coordinate:")))
x_coord.append(int(input("Enter x7 coordinate:")))
y_coord.append(int(input("Enter y7 coordinate:")))
x_coord.append(int(input("Enter x8 coordinate:")))
y_coord.append(int(input("Enter y8 coordinate:")))
n = 8
res = " "
for elemx in x_coord:
    if x_coord.count(elemx)>1:
        res = "Yes"

for elemy in y_coord:
    if y_coord.count(elemy)>1:
        res = "Yes"

for i in range(n):
    for j in range(i+1,n):
        if (abs(x_coord[i] - x_coord[j]) == abs(y_coord[j] - y_coord[i])) :
            res = "Yes"
if res != "Yes":
    res = "No"
print(res)
print(input("Click on \"Enter\" to close program"))