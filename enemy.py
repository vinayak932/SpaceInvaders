from turtle import Turtle

class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.color("white")
        self.setheading(-90)
        self.penup()