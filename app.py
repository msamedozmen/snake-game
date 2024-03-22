from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
myscreen = Screen()
myscreen.setup(width=800, height=800)
myscreen.bgcolor("black")
myscreen.title("Snake Game")
myscreen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
myscreen.listen()
myscreen.onkey(key="Up", fun=snake.up)
myscreen.onkey(key="Down", fun=snake.down)
myscreen.onkey(key="Left", fun= snake.left)
myscreen.onkey(key="Right", fun=snake.right)


movement=1
score=0
while movement>0:
    
    myscreen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snakes_body[0].distance(food)<15:
        score +=1
        food.new_location()
        snake.new_body()
        score_board.new_score()
    if snake.snakes_body[0].xcor()>380 or snake.snakes_body[0].xcor()<-380 or snake.snakes_body[0].ycor()>380 or snake.snakes_body[0].ycor()<-380:
        score_board.reset_game()
        snake.reset_snake()
    if snake.hit_tail() ==1:
        score_board.reset_game()
        snake.reset_snake()



myscreen.exitonclick()