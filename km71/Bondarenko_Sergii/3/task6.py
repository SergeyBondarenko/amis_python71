first_c = int(input("Введите количество ученников в классе №1:"))
second_c = int(input("Введите количество ученников в классе №2:"))
third_c = int(input("Введите количество ученников в классе №3:"))
tables1 = first_c//2 + first_c%2
tables2 = second_c//2 + second_c%2
tables3 = third_c//2 + third_c%2
all_tables = tables1 + tables2 + tables3
print("Минимальное количество столов = " + str(all_tables))
print(input("Нажмите клавишу \"Enter\" для окончания работы программы"))
