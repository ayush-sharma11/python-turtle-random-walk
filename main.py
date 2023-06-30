import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
# 0 to 255 values

def random_color():
    """Generates random color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    random_color = (r, g, b)
    return random_color

turtle.pensize(5) # size/width of the pen
turtle.speed("fast") # speed at which the turtle moves

directions = [0, 90, 180, 270]

for _ in range(50):
    turtle.color(random_color())
    turtle.forward(30)
    turtle.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()