import turtle
a=turtle.Turtle()
a.getscreen().bgcolor("yellow")
a.penup()
a.goto(-200, 100)
a.pendown()
a.color("Red")
a.speed(25)
def star(turtle, size):
    if size<=10:
        return
    else:
        turtle.begin_fill()
        for i in range (5):
            turtle.pensize(2)
            turtle.forward(size)
            star(turtle, size/3)
            turtle.left(216)
            turtle.end_fill()
def verma():
    a.up()
    a.setpos(-5,-900)
    a.color('#000000')
    a.write("By Priyanshu verma" , font=("serif",6))
star(a, 360)
verma()
turtle.done()