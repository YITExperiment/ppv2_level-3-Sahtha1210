import turtle

from itertools import cycle
colors = cycle(['blue', 'orange', 'purple', 'pink', 'glod', 'green'])

def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+5, angle+1,shift+1)

turtle.bgcolor('hot pink')
turtle.speed('fast')
turtle.pensize(40)
draw_circle(30,0,1)
