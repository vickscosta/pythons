import turtle
import random

wn = turtle.Screen()
wn.title("Costatech Pong")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

score_A=0
score_B=0

#A
PA=turtle.Turtle()
PA.speed(0)
PA.shape("square")
PA.color("violet")
PA.shapesize(stretch_wid=5,stretch_len=1)
PA.penup()
PA.goto(-350,0)

#B
PB=turtle.Turtle()
PB.speed(0)
PB.shape("square")
PB.color("violet")
PB.shapesize(stretch_wid=5,stretch_len=1)
PB.penup()
PB.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0,0)
ball.dx=0.05   #speed
ball.dy=0.05   #speed

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.clear()
pen.write("ELODIE : 0 - 0 : EVA", align="center", font=("Courrier",24,'bold'))

#obstacle
obs=turtle.Turtle()
obs.speed(0)
obs.shape("circle")
obs.color("white")

def PA_up():
    y=PA.ycor()
    if y>=250:
        y=250
    else:
        y+=20
    PA.sety(y)

def PA_down():
    y=PA.ycor()
    if y<=-250:
        y=-250
    else:
        y-=20
    PA.sety(y)

def PB_up():
    y=PB.ycor()
    if y>=250:
        y=250
    else:
        y+=20
    PB.sety(y)

def PB_down():
    y=PB.ycor()
    if y<=-250:
        y=-250
    else:
        y-=20
    PB.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(PB_up,"Up")
wn.onkeypress(PB_down,"Down")
wn.onkeypress(PA_up,"a")
wn.onkeypress(PA_down,"q")

frames=1
doit=True

#main loop
while True:
    wn.update()

    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if frames%6==0 and doit:
        ball.dx*=1.5
        doit=False

    #borders
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1

     #golos
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=-0.05
        ball.dy=0.05*random.randint(-2,2)   #y speed
        score_A+=1
        pen.clear()
        pen.write("ELODIE : {} - {} : EVA".format(score_A,score_B), align="center", font=("Courrier",24,'bold'))
        frames=0


    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=0.05
        ball.dy=0.05*random.randint(-2,2)   #y speed
        score_B+=1
        pen.clear()
        pen.write("ELODIE : {} - {} : EVA".format(score_A,score_B), align="center", font=("Courrier",24,'bold'))
        frames=0

    #palletes
    if (ball.xcor() > 340 and ball.xcor()< 350) and (ball.ycor()<PB.ycor()+40 and ball.ycor()>PB.ycor()-40 ):
        ball.setx(340)
        ball.dx*=-1 #random.randint(1,3)
        if ball.dy==0:
            ball.dy=random.randint(-2,2)*0.05
        else:
            ball.dy*=random.randint(-2,2)
        frames+=1
        doit=True

    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor()<PA.ycor()+40 and ball.ycor()>PA.ycor()-40 ):
        ball.setx(-340)
        ball.dx*=-1 #random.randint(1,3)
        ball.dy*=random.randint(-2,2)
        if ball.dy==0:
            ball.dy=random.randint(-2,2)*0.05
        else:
            ball.dy*=random.randint(-2,2)
        frames+=1
        doit=True

    




