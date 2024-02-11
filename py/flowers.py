import turtle
from colorsys import hsv_to_rgb

# First flower style
turtle.bgcolor("black")
turtle.tracer(2)
turtle.pensize(2)
h = 0

for i in range(195):
    color = hsv_to_rgb(h, 0.9, 1)
    h += 0.006
    turtle.pencolor(color)
    turtle.lt(179)
    turtle.backward(i * 0.1)
    turtle.circle(i * 0.3, 120)
    turtle.rt(14)
    turtle.forward(i * 0.1)
    turtle.circle(i * 0.3, 120)


# Secod flower style
# turtle.bgcolor("black")
# turtle.speed(0)
# hue = 0

# for i in range(371):
#     col = hsv_to_rgb(hue, 1, 1)
#     hue += 0.005
#     turtle.color(col)
#     turtle.circle(-i * 0.68, 200)
#     turtle.right(80)

turtle.done()
