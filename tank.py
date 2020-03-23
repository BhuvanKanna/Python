import turtle

wn = turtle.Screen()
#wn.title('Tank')
wn.setup(width = 600, height = 600)
wn.tracer(0)
wn.bgcolor('white')

s = turtle.Shape('compound')
poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
s.addcomponent(poly1, "red", "blue")
poly2 = ((0,0),(10,-5),(-10,-5))
s.addcomponent(poly2, "blue", "red")
wn.register_shape(s)
tank = turtle.Turtle()
tank.speed(0)
tank.turtlesize(2)
tank.shape(s)
tank.color("green")
tank.home()
tank.up()
tank.direction = 'up'

bullet = turtle.Turtle()
bullet.penup()
bullet.speed(1)
bullet.color('yellow')
bullet.shape('circle')
bullet.turtlesize(.5, .5)
bullet.hideturtle()

def goright():
    tank.right(5)
def goleft():
    tank.left(5)
def forward():
    tank.forward(5)
def shoot():
    bullet.setpos(tank.pos())
    bullet.setheading(tank.heading())
    bullet.showturtle()
wn.onkeypress(goright, 'Right')
wn.onkeypress(goleft, 'Left')
wn.onkeypress(shoot, 'space')
wn.onkeypress(forward, 'Up')
wn.listen()
while True:
    wn.update()
    wn.ontimer(tank.forward(5), 10)
    wn.ontimer(bullet.forward(10), 10)
