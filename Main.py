from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
# Setting up screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)    # Turns off animation on screen
# Make snake, food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()
# Move snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(scoreboard.endgame, "e")
while scoreboard.game_is_on:
    screen.update()    # Used with Screen tracer
    time.sleep(0.2)    # Adds a delay
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        for segment in snake.segments:
            while food.position == segment.position:
                food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()
    # Detect collision with body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
