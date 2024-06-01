from turtle import*
shape("turtle")
width(5)
speed(1000)
bgcolor("skyblue")

penup()
goto(-600,-350)
pendown()
pencolor("green")
forward(325)
pencolor("dark gray")
forward(600)
pencolor("green")
forward(325)

pencolor("dark gray")
penup()
goto(-275,-350)
pendown()

begin_fill()
fillcolor("gray")

left(90)
forward(400)

# დიდი მარცხენა სახურავი

left(90)
forward(33)
right(90)
forward(45)
right(90)
forward(33)
right(90)
forward(18)
left(90)
forward(18)

left(90)
forward(18)
right(90)
forward(28)
right(90)
forward(18)


left(90)
forward(18)
left(90)
forward(18)
right(90)
forward(28)
right(90)
forward(18)

left(90)
forward(18)
left(90)
forward(18)
right(90)
forward(33)
right(90)
forward(45)
right(90)
forward(33)

left(90)
forward(400)

penup()
goto(325,-350)
pendown()
pencolor("dark gray")



right(180)


forward(400)
#meore saxuravi
right(90)
forward(33)
left(90)
forward(45)
left(90)
forward(33)
left(90)

forward(18)
right(90)
forward(18)

right(90)
forward(18)
left(90)
forward(28)
left(90)
forward(18)

right(90)
forward(18)
right(90)
forward(18)
left(90)
forward(28)
left(90)
forward(18)

right(90)
forward(18)
right(90)
forward(18)

left(90)
forward(33)
left(90)
forward(45)

left(90)
forward(33)
right(90)
forward(400)

#tani
right(180)
forward(340)


left(90)

forward(380)

left(90)
forward(340)
end_fill()

# drosebi
pencolor("black")
penup()
goto(-227,95)
pendown()

begin_fill()
fillcolor("white")

right(180)
forward(90)

right(90)
forward(100)

right(90)
forward(40)

right(90)
forward(100)
end_fill()
# drosis warwera

penup()
goto(-202,160)
pendown()

right(180)
forward(5)
right(90)
forward(5)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)


pencolor("white")
forward(10)
pencolor("black")
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)

pencolor("white")
forward(10)

pencolor("black")
left(60)
forward(23)
right(120)
forward(23)
left(60)
right(180)



# meore drosa
penup()
goto(279,95)
pendown()

begin_fill()
fillcolor("white")

right(90)
forward(90)

right(90)
forward(100)

right(90)
forward(40)

right(90)
forward(100)

end_fill()

# meore drosis warwera
penup()
goto(304,160)
pendown()

right(180)
forward(5)
right(90)
forward(5)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)

pencolor("white")
forward(10)
pencolor("black")
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
right(90)
forward(20)
left(90)

pencolor("white")
forward(10)

pencolor("black")
left(60)
forward(23)
right(120)
forward(23)

# yvavili
left(160)
penup()
goto(-370,-350)
pendown()
width(3)
pencolor("green")
forward(20)
left(30)
pencolor("pink")
begin_fill()
fillcolor("pink")

forward(8)
right(50)
forward(6)
right(260)
forward(6)
left(50)
forward(6)
right(260)
forward(6)
left(50)
forward(6)
right(260)
forward(6)
left(50)
forward(8)
end_fill()

# yvavili2
right(80)
penup()
goto(-420,-350)
pendown()

pencolor("green")
forward(30)
left(30)
pencolor("purple")
begin_fill()
fillcolor("purple")

forward(9)
right(50)
forward(8)
right(260)
forward(8)
left(50)
forward(8)
right(260)
forward(8)
left(50)
forward(8)
right(260)
forward(8)
left(50)
forward(9)
end_fill()

# mesame yvavili
right(65)
penup()
goto(-480,-350)
pendown()

pencolor("green")
forward(25)
right(30)
pencolor("red")
begin_fill()
fillcolor("red")

forward(8)
right(50)
forward(7)
right(260)
forward(7)
left(50)
forward(7)
right(260)
forward(7)
left(50)
forward(7)
right(260)
forward(7)
left(50)
forward(8)
end_fill()

# yvavili 4

right(20)
penup()
goto(-335,-350)
pendown()

pencolor("green")
forward(30)
right(30)
pencolor("white")
begin_fill()
fillcolor("white")

forward(9)
right(50)
forward(8)
right(260)
forward(8)
left(50)
forward(8)
right(260)
forward(8)
left(50)
forward(8)
right(260)
forward(8)
left(50)
forward(9)
end_fill()


# xe
penup()
goto(-550,-350)
pendown()

import turtle 
import time
t = turtle. Turtle() 
turtle. title("2D Tree")
t. shape("circle")
t.penup()
t.goto(-530,-170)
t.pendown()



t. pen (pencolor="green", fillcolor="green", pensize=4, speed=1)


def draw_tree(size):
    t.begin_fill()
    t.circle (size)
    size+=10
    t.end_fill()
    t.pencolor("brown")
    t.fillcolor ("brown")


    t.goto (-530,-170)

    t.begin_fill()

    t.right (90)
    t.forward(size*2)
    t.right (90)
    t.forward (20)
    t.right(90)
    t.forward(size*2)
    t.right (90)
    t.goto (-530,-170)

    t.end_fill()

draw_tree(80)

# mze

t.penup()
t.goto(520,220)
t.pendown()
t.pencolor("yellow")
t.fillcolor("yellow")


def draw_sun(size):
    t.begin_fill()
    t.circle (size)
    size+=10
    t.end_fill()

draw_sun(50)

# mepe
# pexi
pencolor("black")
penup()
goto(400,-350)
pendown()

right(5)

pencolor("black")
begin_fill()
fillcolor("blue")
forward(65)
right(90)
forward(20)
right(90)
forward(65)
right(90)
forward(20)
right(90)

end_fill()

begin_fill()
fillcolor("blue")
right(90)
forward(40)
left(90)
forward(65)
left(90)
forward(20)

end_fill()

left(90)
forward(65)
right(180)
forward(65)
left(90)

# tani
forward(20)
right(90)
begin_fill()
fillcolor("white")

forward(55)
right(90)
forward(16)
left(90)

# yeli

begin_fill()
fillcolor("pink")
forward(6)
right(90)
forward(8)
right(90)
forward(6)
right(90)
forward(8)

end_fill()

#

left(180)
forward(24)
begin_fill()
fillcolor("white")
right(90)
forward(55)

right(90)
forward(40)

right(90)
forward(55)
right(90)
forward(40)

end_fill()

# xeli

begin_fill()
fillcolor("white")
forward(6)
right(90)
forward(70)
right(90)
forward(6)
right(90)
forward(70)
end_fill()

left(90)
forward(46)

# meore xeli

begin_fill()
fillcolor("white")

left(90)
forward(70)
left(90)
forward(6)
left(90)
forward(70)
end_fill()

# tavi
right(90)
forward(16)
left(90)
forward(6)
right(90)
forward(4)

pencolor("pink")
begin_fill()
fillcolor("pink")

t.penup()
t.goto(420,-222)
t.pendown()
t.pencolor("pink")
t.fillcolor("pink")


def draw_sun(size):
    t.begin_fill()
    t.circle (size)
    size+=10
    t.end_fill()

draw_sun(20)

# gvirgvini
speed(1)
left(90)
forward(35)
pencolor("gold")
begin_fill()
fillcolor("gold")
left(90)
forward(20)
right(90)
forward(10)

right(20)
forward(10)
right(340)
forward(10)
left(70)
forward(10)

right(20)
forward(10)
right(70)
forward(10)
left(70)
forward(10)











