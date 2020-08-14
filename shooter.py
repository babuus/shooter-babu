import turtle
import os
import math
import random
from tkinter import *
#import pysound
# import tkSnack

# root = Tk()
# tkSnack.initializeSnack(root)

# snd = tkSnack.Sound()

#screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("shoot")
wn.bgpic("Fr.png")

#register the shapes
turtle.register_shape("invaders.gif")
turtle.register_shape("spaceship 2.gif")
#turtle.register_shape("bullet.png")

#setting border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in  range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#///////////////////////////////////////////////////////////////////////
#set score
score = 0

#displaying the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scoresrg = "Points: %s" %score
score_pen.write(scoresrg, False, align = "left",font = ("Aial", 14, "normal"))
score_pen.hideturtle()

#///////////////////////////////////////////////////////////////////////
#player
player = turtle.Turtle()
player.color("blue")
player.shape("spaceship 2.gif")
player.shapesize(outline=2)
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)


playerspd = 15

#///////////////////////////////////////////////////////////////////////
#enemy
number_of_enemies = 5
enemies = []

#add enemies to listS
for i in range(number_of_enemies):
    #create enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    enemy.color("red")
    enemy.shape("invaders.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)
    #enemy.hideturtle()


enemyspd = 2

#////////////////////////////////////////////////////////////////////////
#players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet. setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspd = 30

#bullet state
bulletstate = "ready"

#///////////////////////////////////////////////////////////////////////
#move player left and right
def move_left():
    x = player.xcor()
    x -= playerspd
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x= player.xcor()
    x += playerspd
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()
        # snd.read('shooting_sound.wav')
        # snd.play(blocking=1)


def collsision(t1 ,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


#onkey liz

turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

#*****************************************************************************************************
#Main game loop...........

while True:

    for enemy in enemies:
    #move enemy
        x = enemy.xcor()
        x += enemyspd
        enemy.setx(x)

    #move enemy down and back
        if (enemy.xcor() > 280):
            #move all enemies down
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            enemyspd *= -1

        if (enemy.xcor() < -280):
            #move all enemies down
            for e in enemies:
                y = enemy.ycor()
                y -= 40
                enemy.sety(y)
            enemyspd *= -1

#coll of 
        if collsision(bullet, enemy):
        #reset the 
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
        #reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
        #update score
            score += 10
            scoresrg = "Point: %s" %score
            score_pen.clear()
            score_pen.write(scoresrg, False, align = "left",font = ("Aial", 14, "normal"))

        if collsision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print ("Game Over")
            break

#move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspd
        bullet.sety(y)

#check bullet is at 
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

#**************************************************************************************************************

delay = input("press ENTER to finish...")
