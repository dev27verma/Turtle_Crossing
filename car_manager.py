import random
from turtle import Turtle


COLOUR = ["red","green","blue","black","yellow"]
CAR_MOVE = 7
CAR_SPEED = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_MOVE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLOUR))
            car_y = random.randint(-250,250)
            new_car.goto(300,car_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def car_s(self):
        self.car_speed += CAR_SPEED


        