# Homework 18 by Polskoi Yuri

import json

input_data = {
    100001: ('Nicolas', 25),
    100002: ('Natali', 19),
    100003: ('Jack', 30),
    100004: ('Elon', 23),
    100005: ('Maria', 44),
    100006: ('Mark', 18)
}

with open('hw_18.json', 'w') as f:
    json.dump(input_data, f)

