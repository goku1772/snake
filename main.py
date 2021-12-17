import turtle as t
import time
from snake_game import Snake
from food import Food
from scoreboard import Score

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect colison with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extened()

    #detect collison with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    #detect collison with it's own tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over
        
screen.exitonclick()
