import pygame
import random

pygame.init()
screen=pygame.display.set_mode((800,600))

x=400
y=300
move_x=20
move_y=0

food_x=random.randrange(0,800,20)
food_y=random.randrange(0,600,20)

score=0
font=pygame.font.SysFont(None,30)

body_x=[]
body_y=[]
length=1

paused=False
running=True
waiting=True
while waiting==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting=False
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            waiting=False
    screen.fill((10,10,10))
    start_text=font.render("press space to start",True,(150,150,150))
    screen.blit(start_text,(290,280))
    pygame.display.flip()
    pygame.time.delay(150)
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_x=0
                move_y=-20
            if event.key == pygame.K_DOWN:
                move_x=0
                move_y=20
            if event.key == pygame.K_RIGHT:
                move_x=20
                move_y=0
            if event.key == pygame.K_LEFT:
                move_x=-20
                move_y=0
            if event.key == pygame.K_SPACE:
                if paused==False:
                    paused=True
                else:
                    paused=False
    if paused == True:
        if event.type==pygame.MOUSEBUTTONDOWN:
            paused=False
    if paused == True:
        pause_text=font.render("PAUSED",True,(150,150,150))
        screen.blit(pause_text,(360,290))
        pygame.display.flip()
        pygame.time.delay(150)
        continue
    x=x+move_x
    y=y+move_y

    if x>=800:
        x=0
    if x<0:
        x=780
    if y>=600:
        y=0
    if y<0:
        y=580

    if x==food_x and y==food_y:
        score +=1
        length=length+1
        food_x = random.randrange(0,800,20)
        food_y = random.randrange(0,600,20)
    body_x.append(x)
    body_y.append(y)
    if len(body_x)>length:
        del body_x[0]
        del body_y[0]
        
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(150,0,0),(food_x,food_y,20,20))
    pygame.draw.rect(screen,(0,150,0),(x,(y-1),20,20))
    for b in range(len(body_x)):
        pygame.draw.rect(screen,(0,150,0),(body_x[b],body_y[b],19,19))
    text = font.render("Score"+str(score),True,(255,255,255))
    screen.blit(text,(10,10))
    pygame.display.flip()

    pygame.time.delay(150)

pygame.quit()

