import turtle
import time
import random
delay= .1
score = 0
segments = []
wn = turtle.Screen()
wn.title('Snake Game')
wn.setup(width = 600, height = 600)
wn.tracer(0)
wn.bgcolor('black')
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.home()
head.up()
head.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.up()
food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
def go_up():
    if head.direction != 'down':
        head.direction = 'up'
def go_down():
    if head.direction != 'up':
        head.direction = 'down'
def go_right():
    if head.direction != 'left':
        head.direction = 'right'
def go_left():
    if head.direction != 'right':
        head.direction = 'left'
def move():
    if head.direction == "up":
        head.sety(head.ycor()+20)
    if head.direction == "down":
        head.sety(head.ycor()-20)
    if head.direction == "right":
        head.setx(head.xcor()+20)
    if head.direction == "left":
        head.setx(head.xcor()-20)
wn.listen()
wn.onkeypress(go_up,'Up')
wn.onkeypress(go_down,'Down')
wn.onkeypress(go_right,'Right')
wn.onkeypress(go_left,'Left')
while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.home()
        head.direction = 'stop'
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('light green')
        new_segment.penup()
        segments.append(new_segment)
        score+=1
        print("Score:"+str(score))
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.home()
            head.direction = 'stop'
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
    time.sleep(delay)
wn.mainloop()