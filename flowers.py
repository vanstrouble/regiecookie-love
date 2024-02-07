from turtle import *
from colorsys import *

# bgcolor("black")
# tracer(2)
# pensize(2)
# h = 0

# for i in range(195):
#     color = colorsys.hsv_to_rgb(h, 0.9, 1)
#     h += 0.006
#     pencolor(color)
#     lt(179)
#     backward(i * 0.1)
#     circle(i * 0.3, 120)
#     rt(14)
#     forward(i * 0.1)
#     circle(i * 0.3, 120)

# done()


bgcolor("black")
speed(0)
h = 0

for i in range(371):
    c = hsv_to_rgb(h, 1, 1)
    h += 0.005
    color(c)
    circle(-i * 0.68, 200)
    right(80)

done()
