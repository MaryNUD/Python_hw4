# Пользователь вводит текст(строка). Словом
# считается последовательность непробельных
# символов идущих подряд, слова разделены одним
# или большим числом пробелов. Определите, сколько
# различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

line = ('She sells sea shells on the sea shore The shells that she sells are sea shells I am sure. So if she sells sea shells on the sea shore I am sure that the shells are sea shore shells')
line = line.replace('.', ' ')
# print (line)
list = line.split()
# print (list)
set_list = set(list)
print (set_list)
print (len(set_list))