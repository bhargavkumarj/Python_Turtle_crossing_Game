from turtle import Turtle
import random
#from player import Player
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#RANDOM_y=[0,-75,-150,-225,-300,75,150,225,300]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        random_chance=random.randint(1, 6)
        if random_chance == 1:
            new_car=Turtle('square')
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            # new_car.setheading(180)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT









