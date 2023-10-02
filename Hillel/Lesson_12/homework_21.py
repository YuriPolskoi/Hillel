# Homework 21 by Polskoi Yuri

class Auto:
    def __init__(self, brand, age, mark, color="Unknown", weight=0):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1
