from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time

def init():

    sc.setup(width=800, height=800)
    sc.bgcolor('black')
    sc.title("Snake Game")
    sc.tracer(0)


if __name__ == '__main__':

    sc = Screen()
    init()

    game_is_on = True
    snake = Snake()
    food = Food()
    score = Scoreboard()

    sc.listen()
    sc.onkey(snake.up,"Up")
    sc.onkey(snake.down,"Down")
    sc.onkey(snake.right,"Right")
    sc.onkey(snake.left,"Left")

    while game_is_on:
        sc.update()
        time.sleep(0.1)
        snake.move()
        if snake.ate(food):
            food.regenerate()
            score.update()
            snake.growtail()
        if snake.wallcollision() or snake.bit_itself():
            score.game_over()
            game_is_on = False


    sc.exitonclick()



