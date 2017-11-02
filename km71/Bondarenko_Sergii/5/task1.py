line = input("Введите рост каждого ученика:").split()
for i in range(len(line)):
    line[i] = int(line[i])
Petya = int(input("Рост Пети:"))
line.append((Petya))
line.sort()
line = line[::-1]

same_h = line.count(Petya)
place = line.index(Petya)+same_h
print("Место Пети: ", place)
print(input("Нажмите \"Enter\" для выхода из програмы"))
