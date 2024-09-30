from turtle import Turtle
import random
X_LIM = 380
Y_LIM  = 380

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('yellow')
        self.speed("fastest")
        self.goto(random.randint(-X_LIM,X_LIM), random.randint(-Y_LIM,Y_LIM))

    def regenerate(self):
        self.goto(random.randint(-X_LIM, X_LIM), random.randint(-Y_LIM, Y_LIM))