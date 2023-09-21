# Homework 12 by Polskoi Yuri

input_data = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

output_data = tuple(filter(lambda item: item.lower() == item.lower()[::-1], input_data))

print(output_data)
