# Homework 13 by Polskoi Yuri

import random
from datetime import datetime


def time_decorator(func):
    def wrapper(*args):
        now = datetime.now()
        res = func(*args)
        print('Час виконання функції:', datetime.now() - now)
        return res
    return wrapper


@time_decorator
def gen_rand_list(amount):
    list_numbers = [int(random.random() * 10) + 1 for i in range(amount)]
    print('Було згенеровано список із випадкових чисело від 1 до 10 у кількості:', amount)
    return list_numbers


@time_decorator
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print('Було обчислено факторіал від', n)
    return result


gen_rand_list(1000000)

factorial(50000)
