import pygame
import random

pygame.init()
screen=pygame.display.set_mode((800,600))

x=400
y=300
move_x=20
move_y=0

bg_colors = [
    (0, 0, 0),
    (10, 10, 30),
    (20, 10, 10),
    (10, 25, 10),
    (25, 20, 5)
]

food_x=random.randrange(0,800,20)
food_y=random.randrange(0,600,20)

score=0
font=pygame.font.SysFont(None,30)

body_x=[]
body_y=[]
length=1

started = False
running=True
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                started = True
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

    if started == True:         
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
        
    background = bg_colors[(score//5)%len(bg_colors)]
    screen.fill(background)

    

    for grid_x in range(0, 800, 20):
        pygame.draw.line(screen, (35, 35, 35), (grid_x, 0), (grid_x, 600), 1)

    for grid_y in range(0, 800, 20):
        pygame.draw.line(screen, (35, 35, 35), (0, grid_y), (800, grid_y), 1)

    pygame.draw.rect(screen,(150,0,0),(food_x,food_y,20,20))
    pygame.draw.rect(screen,(0,255,100),(x,(y-1),20,20))
    for b in range(len(body_x)):
        pygame.draw.rect(screen,(0,150,0),(body_x[b],body_y[b],19,19))
    score_text = font.render("Score: "+str(score), True, (255,255,255))
    screen.blit(score_text,(10,10))
    length_text = font.render("Length: " + str(score), True, (255, 255, 255))
    screen.blit(length_text, (120, 10))

    if not started:
        start_text = font.render(
            "PRESS SPACE TO START",
            True,
            (255, 255, 255)
        )

        start_rect = start_text.get_rect(center = (400, 300))

        screen.blit(start_text, start_rect)

    pygame.display.flip()

    pygame.time.delay(150)

pygame.quit()