list = input("Enter your list:").split()
for i in range(len(list)):
    list[i] = int(list[i])
res = 0
for i in list:
    for j in list:
        if i == j:
            res +=1
    res -=1

print("The number of same pairs is", res//2)
print(input("Click on \"Enter\" to close program"))