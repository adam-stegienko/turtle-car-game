from turtle import Turtle

COLORS = ["red", "green", "orange", "yellow", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()