from turtle import Turtle, Screen

_turtle= Turtle()
_turtle.pensize(3)
screen= Screen()

def move_forward():
    _turtle.forward(10)

def move_backward():
    _turtle.backward(10)

def turn_left():
    _turtle.left(10)

def turn_right():
    _turtle.right(10)
    
def clear_screen():
    _turtle.clear()
    _turtle.penup()
    _turtle.home()
    _turtle.pendown()
    
screen.listen()
screen.onkey(fun=move_forward, key="Up")
screen.onkey(fun=move_backward, key="Down")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=turn_right, key="Right")
screen.onkey(fun=clear_screen, key="c")

screen.exitonclick()
