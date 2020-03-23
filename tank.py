import turtle

wn = turtle.Screen()
wn.title('Tank')
wn.setup(width = 600, height = 600)
wn.tracer(0)
wn.bgcolor('white')
image="fighterjet.gif"

wn.register_shape(image)

tank = turtle.Turtle()
tank.speed(0)
tank.shapesize(2)
tank.shape(image)
tank.color("green")
tank.home()
tank.up()
tank.direction = 'up'

bullet = turtle.Turtle()
bullet.penup()
bullet.speed(1)
bullet.color('yellow')
bullet.shape('circle')
bullet.shapesize(.5, .5)
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
    wn.ontimer(bullet.forward(10), 10)
#    wn.ontimer(tank.forward(5), 10)
    wn.update()
