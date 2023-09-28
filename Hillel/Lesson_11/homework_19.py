# Homework 19 by Polskoi Yuri

import json
import csv
import random

with open('hw_18.json') as f:
    people_dict = json.load(f)

num_elements = int(len(people_dict) * 0.75)
all_indices = list(range(len(people_dict)))
selected_indices = sorted(random.sample(all_indices, num_elements))

operator_numbers = ['095', '066', '098', '096', '050', '097']

people_list = [[key] + value for key, value in people_dict.items()]

result_list = [['ID', 'Name', 'Age', 'Phone']] + [
    value + [random.choice(operator_numbers) + ''.join([str(random.randint(0, 9)) for _ in range(7)])]
    if index in selected_indices
    else value
    for index, value in enumerate(people_list)
]

with open('hw_19.csv', 'w', encoding='utf-8', newline='') as f:
    file_write = csv.writer(f, delimiter=',')
    for item in result_list:
        file_write.writerow(item)
