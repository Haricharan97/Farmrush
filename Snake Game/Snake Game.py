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

running=True
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
        food_x = random.randrange(0,800,20)
        food_y = random.randrange(0,600,20)
        
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),(food_x,food_y,20,20))
    pygame.draw.rect(screen,(0,255,0),(x,(y-1),20,20))
    text = font.render("Score"+str(score),True,(255,255,255))
    screen.blit(text,(10,10))
    pygame.display.flip()

    pygame.time.delay(150)

pygame.quit()
