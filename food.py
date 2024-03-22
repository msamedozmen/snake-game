from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super( ).__init__()
        self.speed("fastest")
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5 )
        self.goto(x=random.randint(-370,370),y=random.randint(-370,370))
        
    def new_location(self):
        self.goto(x=random.randint(-370,370),y=random.randint(-370,370))
