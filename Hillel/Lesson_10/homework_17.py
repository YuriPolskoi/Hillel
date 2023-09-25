# Homework 17 by Polskoi Yuri

line_1 = input('Введіть перший рядок: ')

line_2 = input('Введіть другий рядок: ')

line_3 = input('Введіть третій рядок: ')

line_4 = input('Введіть четвертий рядок: ')

with open('file.txt', 'w') as f:
    f.write(line_1 + '\n' + line_2)

with open('file.txt', 'a') as f:
    f.write('\n' + line_3 + '\n' + line_4)
