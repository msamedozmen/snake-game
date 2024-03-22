from turtle import Turtle,Screen
x_cor=[20,0,-20]


class Snake():

    def __init__(self):
        self.snakes_body =[]
        self.create_snake()
        
    def create_snake(self):
        
        for i in range(0,len(x_cor)):
            snake_body =Turtle()
            snake_body.shape("square")
            snake_body.color("white")
            snake_body.penup()
            snake_body.goto(x=x_cor[i],y=0)
            self.snakes_body.append(snake_body)
            
    def move(self):
        for snake in range(len(self.snakes_body)-1,0,-1):
            x= self.snakes_body[snake -1].xcor()
            y= self.snakes_body[snake -1].ycor()
            self.snakes_body[snake].goto(x,y)
        self.snakes_body[0].forward(20)
    
    def reset_snake(self):
        for snake in range(0,len(self.snakes_body)):
            self.snakes_body[snake].goto(1000,1000)
        self.snakes_body.clear()
        self.create_snake()
            
    def up(self):
        if self.snakes_body[0].heading()!=270:
            self.snakes_body[0].setheading(90)
        else:
            pass
    def down(self):
        if self.snakes_body[0].heading()!=90:
            self.snakes_body[0].setheading(270)
        else:
            pass
    def left(self):
        if self.snakes_body[0].heading()!=0:
            self.snakes_body[0].setheading(180)
        else:
            pass
    def right(self):
        if self.snakes_body[0].heading()!=180:
            self.snakes_body[0].setheading(0)
        else:
            pass
    def new_body(self):
        new_x = self.snakes_body[-1].xcor()
        new_y = self.snakes_body[-1].ycor()        
        snake_body = Turtle()
        snake_body.shape("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(new_x,new_y)
        self.snakes_body.append(snake_body)
        
    def hit_tail(self):
        head_x = self.snakes_body[0].xcor()
        head_y = self.snakes_body[0].ycor()
        for i in range(1,len(self.snakes_body)):
            if -10 <self.snakes_body[i].xcor()- head_x<10 and -10< self.snakes_body[i].ycor() - head_y <10:
                return 1