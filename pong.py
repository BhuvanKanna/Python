from time import sleep
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
pygame.init()
wn = pygame.display.set_mode((700, 500))
pygame.display.set_caption('Pong')
score = 0
vel = 15
delay = 80
ballposition = [100, 225]
ballvelocity = [15, 15]
left_bat = [5,200]
right_bat = [680,200]
width = 15
height = 75
run  = True
def drawball():
    global score, ballposition, left_bat, right_bat, ballvelocity, delay
    pygame.draw.rect(wn, (255, 255, 255), (ballposition[0], ballposition[1], 10, 10))
    if ballposition[1] <= 15 or ballposition[1] >= 480:
        ballvelocity[1] = -ballvelocity[1]
    if ballposition[0] >= 672.5 and ballposition[1] in range(right_bat[1]-10, right_bat[1]+75):
        ballvelocity[0] = -ballvelocity[0]
    elif ballposition[0] >= 673 and ballposition[1] not in range(right_bat[1]-10, right_bat[1]+75):
        score+=1
        print(score)
        ballposition[0] = 250
        ballposition[1] = 250
        ballvelocity = [15, 15]
        left_bat[1] = 200
        right_bat[1] = 200
        delay = 80
    if ballposition[0] <= 25 and ballposition[1] in range(left_bat[1]-10, left_bat[1]+75):
        ballvelocity[0] = -ballvelocity[0]
        if delay != 25:
            delay-=5
    elif ballposition[0] <= 20 and ballposition[1] not in range(left_bat[1]-10, left_bat[1]+75) :
        score+=1
        print(score)
        ballposition[0] = 250
        ballposition[1] = 250
        ballvelocity = [15, -15]
        left_bat[1] = 200
        right_bat[1] = 200
        delay = 80
    ballposition[0] += ballvelocity[0]
    ballposition[1] += ballvelocity[1]
while run:
    pygame.time.delay(delay)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        right_bat[1] -= vel
    if keys[pygame.K_w]:
        left_bat[1] -= vel
    if keys[pygame.K_DOWN]:
        right_bat[1] += vel
    if keys[pygame.K_s]:
        left_bat[1] += vel
    wn.fill((0))
    pygame.draw.rect(wn, (255, 255, 255), (left_bat[0], left_bat[1], width, height))
    pygame.draw.rect(wn, (255, 255, 255), (right_bat[0], right_bat[1], width, height))
    drawball()
    pygame.display.update()
pygame.quit()
