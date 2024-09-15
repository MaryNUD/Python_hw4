# Задача 2. Палиндром
# Пользователь вводит строку. Необходимо написать программу, которая
# определяет, существует ли у этой строки перестановка, при которой она станет
# палиндромом. Затем она должна выводить соответствующее сообщение.
# Пример 1
# Введите строку: aab
# Можно сделать палиндромом
# Пример 2
# Введите строку: aabc
# Нельзя сделать палиндромом

line = input('Enter the line to check: ', )
line_dict = dict()
for elem in line:
    line_dict[elem] = line_dict.get(elem, 0) + 1  
    # считаем количество каждого элемента в строке
# print (line_dict)
odd_values = 0
for i_values in line_dict.values():
    if i_values % 2 != 0:
        odd_values += 1
# print (odd_values)
if odd_values != 1:
    print ('You cannot make polindrom from this line')
else:
    print ('Polindrom is available')
