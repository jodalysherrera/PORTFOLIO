from turtle import *
import math


j = Turtle()
j.speed(3)

shape=input('shape:')
setup(500,300)
x_pos = 0
y_pos = 0

#function where the body is an equation that can make shapes
#def shape(sides):
	#j.forward(180*(sides-2))
	#j.right(180*(sides-2))
#if sides== "n>2"


def square():
	j.penup()
	j.setposition(x_pos,y_pos)
	j.pendown()
	j.begin_fill()
	j.color("purple","purple")
	range(0,100)
	j.forward(125)
	j.left(90)
	j.forward(125)
	j.left(90)
	j.forward(125)
	j.left(90)
	j.forward(125)
	j.left(90)
	j.penup()
if shape=="square":
	square()

def triangle():
	j.penup()
	j.setposition(x_pos,y_pos)
	j.pendown()
	j.begin_fill()
	j.color("purple","purple")
	j.forward(100)
	j.left(120)
	j.forward(100)
	j.left(120)
	j.forward(100)
	j.left(120)
	j.penup()
if shape=="triangle":
	triangle()

exitonclick()
