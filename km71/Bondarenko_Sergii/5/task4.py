balls = int(input("Enter number of balls:"))
list = []
for i in range(balls):
    list.append(i+1)
list1 = []
throws = int(input("Enter number of throws:"))
for j in range(throws):
    list1 += list[int(input("Enter number of the left ball:"))-1:int(input("Enter number of the right ball:"))]

for liste1 in list1:
    for liste in list:
        if liste == liste1:
            a = list.index(liste)
            list.insert(a,".")
            list.remove(liste)
for liste in list:
    if liste != ".":
        b = list.index(liste)
        list.insert(b, "I")
        list.remove(liste)

print(" ".join(list))
print(input("Click on \"Enter\" to close program"))
