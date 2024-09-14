# Даны три списка.
# array_1 = [1, 5, 10, 20, 40, 80, 100]
# array_2 = [6, 7, 20, 80, 100]
# array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# # Нужно выполнить две задачи:
# # 1. найти элементы, которые есть в каждом списке;
# # 2. найти элементы из первого списка, которых нет во втором и третьем
# # списках.

# new_array_set = set(array_1) & set(array_2) & set(array_3)
# print ('These numbers are in every list: ', new_array_set)

# new_array = set(array_1) & set(array_2)
# new_array_2 = set(array_1) & set(array_3)
# array_1 = set(array_1)- new_array - new_array_2
# print (array_1)

