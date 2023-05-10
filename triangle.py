

from turtle import *
import turtle

tur = turtle.Turtle()
"this colors with user prompt"
side=int((input("Enter the length of triangle: ")))
col=input("enter the name of color")
tur.fillcolor(col)
tur.begin_fill()
for _ in range(3):
      tur.forward(side)
      tur.right(-120)
tur.end_fill()


""" this colors in blue
tur.fillcolor("blue")
tur.begin_fill()
for  _ in range(3):
      tur.forward(100)
      tur.left(120)
tur.end_fill()"""

