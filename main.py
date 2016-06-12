# fenv/bin/python

import turtle

TRIANGE_ANGLE = 60
TRIANGLE_ANGLES_SUM = 180
MAX_ANGLE = 360
START_X = -200
START_Y = -200
SIDE_LEN = 400
REQUIRED_DEPTH = 4

def draw_fractal_triangle(x, y, len, depth, a):
        depth -= 1
        if depth == 0:
            return
        a.penup()
        a.goto(x,y)
        a.seth(TRIANGE_ANGLE)
        a.fd(len)
        a.pendown()
        a.seth(MAX_ANGLE)
        x1 = a.xcor()
        y1 = a.ycor()
        a.fd(len)
        a.rt(TRIANGLE_ANGLES_SUM - TRIANGE_ANGLE)
        a.fd(len)
        a.rt(TRIANGLE_ANGLES_SUM - TRIANGE_ANGLE)
        a.fd(len)
        draw_fractal_triangle(x,       y,       len/2, depth, a)
        draw_fractal_triangle(x+len,   y,       len/2, depth, a)
        draw_fractal_triangle(x1,      y1,      len/2, depth, a)

def draw_main_triange(x, y, len, depth, a):
    a.penup()
    a.goto(x,y)
    a.pendown()
    a.lt(TRIANGE_ANGLE)
    a.fd(len)
    a.rt(TRIANGLE_ANGLES_SUM - TRIANGE_ANGLE)
    a.fd(len)
    a.rt(TRIANGLE_ANGLES_SUM - TRIANGE_ANGLE)
    a.fd(len)
    a.seth(MAX_ANGLE)
    draw_fractal_triangle(x,y,len/2,depth, a)

def init():
    wn = turtle.Screen()
    Turtle = turtle.Turtle()
    draw_main_triange(START_X, START_Y, SIDE_LEN, REQUIRED_DEPTH, Turtle)

if __name__ == "__main__":
    init()
    input()
