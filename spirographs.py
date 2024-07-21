import turtle
import random

snake = turtle.Turtle()
snake.speed(0)
colors = ["cornflower blue", "royal blue", "deep sky blue", "light blue", "blue", "medium blue"]
for i in range(40):
    snake.color(random.choice(colors))
    snake.penup()
    snake.forward(30)
    snake.pendown()
    snake.circle(5)
    snake.penup()
    snake.right(180)
    snake.forward(30)
    snake.right(180)
    snake.pendown()
    for j in range(10):
        snake.forward(2*j)
        snake.right(90)
    snake.forward(200)
    snake.right(70)
