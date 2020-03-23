import turtle
from operator import mul
screen = turtle.Screen()
screen.bgcolor("light green")
tank = turtle.Turtle()
tank.penup()
tank.setpos(5,15)
tank.speed(100)
tank2 = turtle.Turtle()
tank2.penup()
tank2.setpos(5,15)
tank2.speed(100)
tank2.color("red")
if False:
	tank.fd(0.5*30)
	print(tank.pos())
	tank.rt(90)
	tank.fd(0.5*20)
	print(tank.pos())
	tank.rt(90)
	tank.fd(0.5*10)
	print(tank.pos())
	tank.lt(90)
	tank.fd(0.5*10)
	print(tank.pos())
	tank.rt(90)
	tank.fd(0.5*100)
	print(tank.pos())
	tank.rt(90)
	tank.fd(0.5*10)
	print(tank.pos())
	tank.lt(90)
	tank.fd(0.5*10)
	print(tank.pos())
	tank.rt(90)
	tank.fd(0.5*20)
	print(tank.pos())
	tank.rt(90)
	tank.fd(0.5*40)
	print(tank.pos())

	tank.lt(60)
	tank.fd(0.5*15)
	print(tank.pos())

	tank.lt(120)
	tank.fd(0.5*40)
	print(tank.pos())

	tank.lt(90)
	tank.fd(0.5*5)
	print(tank.pos())

	tank.rt(90)
	tank.fd(0.5*10)
	print(tank.pos())

	tank.rt(90)
	tank.fd(0.5*20)
	print(tank.pos())

	tank.rt(90)	
	tank.fd(0.5*10)
	print(tank.pos())

	tank.rt(90)
	tank.fd(0.5*5)
	print(tank.pos())

	tank.lt(90)
	tank.fd(0.5*45)
	print(tank.pos())

	tank.lt(90)
	tank.fd(0.5*3)
	print(tank.pos())

	tank.rt(90)
	tank.fd(0.5*22)
	print(tank.pos())

	tank.rt(60)
	tank.goto(5,15)
	print(tank.pos())


screen.register_shape("tankfd",((-20.0, 15.0),(-20.0, 5.0),(-15.0, 5.0),(-15.0, 0.0),(35.0, 0.0),(35.0, 5.0),(40.0, 5.0),(40.0, 15.0),(20.0, 15.0),(16.25, 21.4951905284),(36.25, 21.4951905284),(36.25, 18.9951905284),(41.25, 18.9951905284),(41.25, 28.9951905284),(36.25, 28.9951905284),(36.25, 26.4951905284),(13.75, 26.4951905284),(13.75, 27.9951905284),(2.75, 27.9951905284),(-5.0, 15.0)))
screen.register_shape("tankbd",((20.0, 15.0),(20.0, 5.0),(15.0, 5.0),(15.0, 0.0),(-35.0, 0.0),(-35.0, 5.0),(-40.0, 5.0),(-40.0, 15.0),(-20.0, 15.0),(-16.25, 21.4951905284),(-36.25, 21.4951905284),(-36.25, 18.9951905284),(-41.25, 18.9951905284),(-41.25, 28.9951905284),(-36.25, 28.9951905284),(-36.25, 26.4951905284),(-13.75, 26.4951905284),(-13.75, 27.9951905284),(-2.75, 27.9951905284),(5.0, 15.0)))
tank.shape("tankfd")
tank.seth(90)
tank.penup
tank2.shape("tankfd")
tank2.seth(90)
tank2.penup
def ford():
	tank.shape("tankfd")
	tank.setpos(tank.xcor() - 5,tank.ycor())
def back():
	tank.shape("tankbd")
	tank.setpos(tank.xcor() + 5,tank.ycor())
def down():
	tank.setpos(tank.xcor(),tank.ycor() - 5)
def up():
	tank.setpos(tank.xcor(),tank.ycor() + 5)
def ford2():
	tank2.shape("tankfd")
	tank2.setpos(tank2.xcor() - 5,tank2.ycor())
def back2():
	tank2.shape("tankbd")
	tank2.setpos(tank2.xcor() + 5,tank2.ycor())
def down2():
	tank2.setpos(tank2.xcor(),tank2.ycor() - 5)
def up2():
	tank2.setpos(tank2.xcor(),tank2.ycor() + 5)
screen.onkey(back,"Right")
screen.onkey(ford,"Left")
screen.onkey(up,"Up")
screen.onkey(down,"Down")
screen.onkey(back2,"d")
screen.onkey(ford2,"a")
screen.onkey(up2,"w")
screen.onkey(down2,"s")
screen.mainloop()
screen.listen()
