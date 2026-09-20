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
bonus_x=-20
bonus_y=-20
new_bonus=True

score=0
font=pygame.font.SysFont(None,30)

body_x=[]
body_y=[]
length=1

obstacle_x=[]
obstacle_y=[]
obstacles=10

while len(obstacle_x)< obstacles:
    new_x=random.randrange(0,800,20)
    new_y=random.randrange(0,600,20)
    ok=True
    if abs(new_x)+abs(new_y) <=100:
        ok=False
    if new_x==food_x and new_y==food_y:
        ok=False
    for j in range(len(obstacle_x)):
        if new_x==obstacle_x[j] and new_y==food_y:
            ok=False
    if ok ==True:
        obstacle_x.append(new_x)
        obstacle_y.append(new_y)

big_font=pygame.font.SysFont(None,80)
medium_font=pygame.font.SysFont(None,50)
window_closed=False

paused=False
delay_time=150
running=True
waiting=True

while waiting==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting=False
            running=False
            window_closed=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting=False
        if event.type == pygame.MOUSEBUTTONDOWN:
            waiting=False
    screen.fill((10,10,10))
    start_text=font.render("Press SPACE OR CLICK TO Start",True,(150,150,150))
    screen.blit(start_text,(250,280))
    pygame.display.flip()
    pygame.time.delay(150)

while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
            window_closed=True
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

    for i in range(len(body_x)):
        if x == body_x[i] and y == body_y[i]:
            running=False

    for j in range(len(obstacle_x)):
        if x==obstacle_x[j] and y==obstacle_y[j]:
            running=False

    if x==food_x and y==food_y:
        score +=1
        length=length+1
        food_x = random.randrange(0,800,20)
        food_y = random.randrange(0,600,20)

        food_ok=False
        while food_ok==False:
            food_ok=True
            for j in range(len(obstacle_x)):
                if food_x== obstacle_x[j] and food_y==obstacle_y[j:]:
                    food_ok=False
            if food_ok==False:
                food_x = random.randrange(0,800,20)
                food_y = random.randrange(0,600,20)
    

        if score %5 == 0:
            delay_time=delay_time-20
            if delay_time<50:
                delay_time=50

    body_x.append(x)
    body_y.append(y)
    if len(body_x)>length:
        del body_x[0]
        del body_y[0]
        
    screen.fill((0,0,0))

    for j in range(len(obstacle_x)):
        pygame.draw.rect(screen,(128,128,128),(obstacle_x[j],obstacle_y[j],20,20))

    pygame.draw.rect(screen,(245, 222, 179),(food_x,food_y,20,20))
    for b in range(len(body_x)):
        pygame.draw.rect(screen,(0,150,0),(body_x[b],body_y[b],19,19))

    text = font.render("Wheat Collected"+str(score),True,(255,255,255))
    screen.blit(text,(10,10))
    pygame.display.flip()
    pygame.time.delay(delay_time)

ending=True
if window_closed==True:
    ending=False
while ending==True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            ending=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                ending=False
        if event.type == pygame.MOUSEBUTTONDOWN:
                    ending=False

    screen.fill((0,0,0))
    over_text=big_font.render("GAME OVER",True,(255,0,0))
    score_text=medium_font.render("Wheat Collected:"+str(score),True,(255,255,255))
    close_text=font.render("Press SPACE or CLICK to Close",True,(150,150,150))

    screen.blit(over_text,over_text.get_rect(center=(400,220)))
    screen.blit(score_text,score_text.get_rect(center=(400,310)))
    screen.blit(close_text,close_text.get_rect(center=(400,400)))

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()