import pygame
pygame.init()
wn = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Flappy')
run = True
birdcor = [50, 300]
def draw_bird():
    pygame.draw.rect(wn, (255, 255, 0), (birdcor[0], birdcor[1], 50, 50))
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    birdcor[1]+=10
    if keys[pygame.K_SPACE]:
        birdcor[1] -= 35
    wn.fill((0))
    draw_bird()
    pygame.display.update()
pygame.quit()
                        
