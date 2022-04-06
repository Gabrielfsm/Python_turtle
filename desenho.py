import turtle
from turtle import *

tela = turtle.Screen()
tela.bgcolor("black")

color("red", "yellow")
begin_fill()
while True:
    forward(500)
    left(101)
    if abs(pos()) < 1:
        break

end_fill()
done()
