import turtle

def moving():
    turtle.forward(50)
    turtle.stamp()

def move_w():
    turtle.setheading(90)
    moving()

def move_s():
    turtle.setheading(270)
    moving()

def move_d():
    turtle.setheading(0)
    moving()

def move_a():
    turtle.setheading(180)
    moving()

def reset():
    turtle.reset()
    
turtle.shape('turtle')

turtle.onkey(move_a,'a')
turtle.onkey(move_d,'d')
turtle.onkey(move_w,'w')
turtle.onkey(move_s,'s')
turtle.onkey(reset,'Escape')
turtle.listen()
