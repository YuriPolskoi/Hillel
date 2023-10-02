# Homework 21 by Polskoi Yuri

import time


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


class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color="Unknown", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color="Unknown", weight=0):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


truck_1 = Truck(brand="DAF", age=5, mark="XF105", max_load=40000, color="White")
truck_2 = Truck(brand="Volvo", age=2, mark="FH16", max_load=25000)

car_1 = Car(brand="BMW", age=3, mark="G05", max_speed=250, color="Red")
car_2 = Car(brand="Honda", age=1, mark="Civic", max_speed=170)

print("Truck 1:")
print(f"Brand: {truck_1.brand}, Age: {truck_1.age}, Mark: {truck_1.mark}, Color: {truck_1.color}, Weight: {truck_1.weight}, Max Load: {truck_1.max_load}")
truck_1.move()
truck_1.load()

print("\nTruck 2:")
print(f"Brand: {truck_2.brand}, Age: {truck_2.age}, Mark: {truck_2.mark}, Color: {truck_2.color}, Weight: {truck_2.weight}, Max Load: {truck_2.max_load}")
truck_2.move()
truck_2.load()

print("\nCar 1:")
print(f"Brand: {car_1.brand}, Age: {car_1.age}, Mark: {car_1.mark}, Color: {car_1.color}, Weight: {car_1.weight}, Max Speed: {car_1.max_speed}")
car_1.move()

print("\nCar 2:")
print(f"Brand: {car_2.brand}, Age: {car_2.age}, Mark: {car_2.mark}, Color: {car_2.color}, Weight: {car_2.weight}, Max Speed: {car_2.max_speed}")
car_2.move()
