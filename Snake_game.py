import turtle
import time
import random

delay=0.1
score=0
high_score=0

win=turtle.Screen()
win.title("Snake Game")
win.setup(width=600,height=600)
win.bgcolor("black")
win.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.direction="stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()

body=[]

pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0   High score: 0",align="center",font=('Courier',24,'normal'))

def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_left():
    if head.direction!="right":
        head.direction="left"
def go_right():
    if head.direction!="left":
        head.direction="right"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
        
win.listen()
win.onkeypress(go_up, "Up")
win.onkeypress(go_down, "Down")
win.onkeypress(go_left, "Left")
win.onkeypress(go_right, "Right")

while True:
    win.update()

    if ((head.xcor()>290) or (head.xcor()<-290) or (head.ycor()>290) or (head.ycor()<-290)):
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        for i in body:
            i.goto(1000,1000)

        body.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write(("Score: {}   High score: {}".format(score,high_score)),align="center",font=('Courier',24,'normal'))
    
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        
        newbody=turtle.Turtle()
        newbody.speed(0)
        newbody.shape("square")
        newbody.color("green")
        newbody.penup()
        
        body.append(newbody)
        delay -=0.001

        score += 10
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write(("Score: {}   High score: {}".format(score,high_score)),align="center",font=('Courier',24,'normal'))
        
    for i in range(len(body)-1,0,-1):
        x=body[i-1].xcor()
        y=body[i-1].ycor()
        body[i].goto(x,y)

    if(len(body)>0):
        x=head.xcor()
        y=head.ycor()
        body[0].goto(x,y)
            
    move()
    for i in body:
        if i.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            for j in body:
                j.goto(1000,1000)
            body.clear()
            score=0
            delay=0.1
            pen.clear()
            pen.write(("Score: {}   High score: {}".format(score,high_score)),align="center",font=('Courier',24,'normal'))
            
    time.sleep(delay)
win.mainloop()
