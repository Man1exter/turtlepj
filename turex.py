import turtle  

t = turtle.Turtle()
t.shape('turtle')

# square
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)

t.circle(100) # pi

t.goto(150,200)
t.goto(-150,200) # move 

t.home() # back to home 0,0

t.clear() # clear the space

t.color('white') # turtle color line

turtle.bgcolor('black') # background color

t.pensize(5) # increase the color line


t.penup()
t.goto(300,300) # move turtle to choice space / up (x,y)

t.pendown()
t.goto(-300,300) # move turtle to choice space / down (x,y)

t.write('HEJECZKA',font=('Roboto',30,"bold")) # write-space with font roboto size 30px and bold letters

# t.hideturtle() hide 
# t.showturtle() show

turtle.exitonclick() # exit with click from the window

t.begin_fill() # before shape the figures
t.end_fill() # after shape the figures