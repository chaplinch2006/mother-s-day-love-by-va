import turtle
import turtle as tur
from PIL import Image
pen=turtle.Turtle()
#write message
tur.title("mummatpoint")
tur.write("specially for you mumma.....!!!i am really sorry for today's mistake....happy mother's day mumma....!!!",align="center",font=("Comic Sans",10,"bold"))
#draw rose
tur.penup()
tur.left(90)
tur.fd(200)
tur.pendown()
tur.right(90)
tur.fillcolor ("red")
tur.begin_fill ()
tur.circle (10,180)
tur.circle (25,110)
tur.left (50)
tur.circle (60,45)
tur.circle (20,170)
tur.right (24)
tur.fd (30)
tur.left (10)
tur.circle (30,110)
tur.fd (20)
tur.left (40)
tur.circle (90,70)
tur.circle (30,150)
tur.right (30)
tur.fd (15)
tur.circle (80,90)
tur.left (15)
tur.fd (45)
tur.right (165)
tur.fd (20)
tur.left (155)
tur.circle (150,80)
tur.left (50)
tur.circle (150,90)
tur.end_fill ()
tur.left (150)
tur.circle (-90,70)
tur.left (20)
tur.circle (75,105)
tur.setheading (60)
tur.circle (80,98)
tur.circle (-90,40)
tur.left (180)
tur.circle (90,40)
tur.circle (-80,98)
tur.setheading (-83)
tur.fd (30)
tur.left (90)
tur.fd (25)
tur.left (45)
tur.fillcolor ("green")
tur.begin_fill ()
tur.circle (-80,90)
tur.right (90)
tur.circle (-80,90)
tur.end_fill ()
tur.right (135)
tur.fd (60)
tur.left (180)
tur.fd (85)
tur.left (90)
tur.fd (80)
tur.right (90)
tur.right (45)
tur.fillcolor ("green")
tur.begin_fill ()
tur.circle (80,90)
tur.left (90)
tur.circle (80,90)
tur.end_fill ()
tur.left (135)
tur.fd (60)
tur.left (180)
tur.fd (60)
tur.right (90)
tur.circle (200,60)
#draw heart
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
def heart():
    pen.fillcolor("pink")
    pen.begin_fill()
    pen.speed(20)
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color("green")
    pen.write("meripyarimumma",font=("Comic Sans",12,"bold"))
heart()
txt()
pen.ht()
myImage = Image.open("mom&me.jpg")
myImage.show()

    
    
    

