import turtle as a
from turtle import *
import time
s=Screen()
s.screensize(700,1000)
speed(190)
pen = a.Turtle()
a.bgcolor("yellow")
a.delay(8)
pen.color("red")
pen.begin_fill()
pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def Verma():
    pen.up()
    pen.setpos(-320,-200)
    pen.color('black')
    pen.write('I LOVE YOU BABES' , font=("Cosmics San MS", 16))
def Verma2():
    pen.up()
    pen.setpos(-5,-900)
    pen.color('black')
    pen.write('Made By Priyanshu Verma' , font=("serif", 6))
Verma()
Verma2() 
pen.end_fill()
time.sleep(100)
ht()