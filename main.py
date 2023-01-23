# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('text.txt', 'r', encoding='utf-8') as file:
    new_list = file.read()
    words = new_list.split(' ')
print(new_list)


dell_list = list(filter(lambda x: 'абв' not in x, words))
print(dell_list)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


rle_list = 'AAAABBBBCCCCDDDDD'
new_list = []
count = 0

for i in range(len(rle_list)-1, -1,-1):
    if rle_list[i] != rle_list[i-1]:
        count += 1
        a = str(count)+rle_list[i]
        new_list.append(a)
        count = 0
    elif i == len(rle_list):
        count += 1
        a = str(count)
        new_list.extend([a, rle_list[i]])
        count = 0

    else:
        count += 1
new_list.reverse()
print(new_list)
