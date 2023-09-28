# Homework 19 by Polskoi Yuri

import json
import csv
import random

with open('hw_18.json') as f:
    people_dict = json.load(f)

print(len(people_dict))

operator_numbers = ['095', '066', '098', '096', '050', '097']

result_list = [['ID', 'Name', 'Age', 'Phone']] + [
    [key] + value + [random.choice(operator_numbers) + ''.join([str(random.randint(0, 9)) for i in range(7)])]
    if random.random() < 0.75
    else [key] + value
    for key, value in people_dict.items()
]

with open('hw_19.csv', 'w', encoding='utf-8', newline='') as f:
    file_write = csv.writer(f, delimiter=',')
    for item in result_list:
        file_write.writerow(item)
