from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.4, stretch_len=0.2)
        self.color("white")
        self.penup()
        self.hideturtle()

    def move_bullet(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)

    def move_enemy_bullet(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)

