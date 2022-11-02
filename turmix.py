import turtle
import random

tur = turtle.Turtle()
turin = turtle.Turtle()


turtle.bgcolor('black')

tur.color('yellow')
tur.shape('turtle')

turin.color('orange')
turin.shape('turtle')

# reptilians symbolic

tur.speed(0)
turin.speed(0)

tur.pendown()
tur.goto(350,350)

turin.pendown()
turin.goto(-450,350)



for x in range(10,450):
    
    tur.color(random.choice(['green','yellow','blue','red','pink','orange']))
    tur.forward(100)
    tur.right(143)
    
    turin.color(random.choice(['green','yellow','blue','red','pink','orange']))
    turin.forward(100)
    turin.right(143)


turtle.exitonclick()