from snake import Snake
import time
from scoreboard import ScoreBoard
from food import Food
from turtle import Screen

s = Screen()
s.tracer(0)
s.bgcolor('pink')
s.title('My snake game')
s.setup(width=600, height=600)
food = Food()
snake = Snake()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
score = ScoreBoard()
game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.addscore()
        snake.extend()
        print(len(snake.segment))

    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 \
            or snake.head.ycor() <= -290 or snake.head.ycor() >= 290:
        game_is_on = False
        score.game_over()

    for segment_ in snake.segment[1:]:
        if snake.head.distance(segment_) < 10:
            game_is_on = False
            score.game_over()



s.exitonclick()
