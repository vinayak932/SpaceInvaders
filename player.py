from turtle import Turtle

class Player(Turtle):
      def __init__(self, position):

          super().__init__()
          self.shape ("triangle")
          self.color("white")
          self.setheading(90)
          self.penup()
          self.goto(position)

      def move_left(self):
          x_cor = self.xcor() - 30
          self.goto(x_cor, self.ycor())

      def move_right(self):
          x_cor = self.xcor() + 30
          self.goto(x_cor, self.ycor())
