import turtle
from turtle import*
from random import randint

tela = turtle.Screen()

t1 = turtle.Turtle()
t1.shape('turtle')
t1.up()
t1.goto(randint(-10, 400), randint(10, 400))



tela.mainloop()