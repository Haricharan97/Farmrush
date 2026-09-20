import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

x = 400
y = 300

move_x = 20
move_y = 0

food_x = random.randrange(0, 800, 20)
food_y = random.randrange(0, 600, 20)

bonus_x = -20
bonus_y = -20
new_bonus = True

score = 0
font = pygame.font.SysFont(None, 30)

body_x = []
body_y = []
length = 1

crop_status = []

for grid_y in range(0, 600, 20):
    row = []

    for grid_x in range(0, 800, 20):
        row.append(random.randint(0, 2))

    crop_status.append(row)

surface = pygame.Surface((800, 600), pygame.SRCALPHA)
bag_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
first_bag_surface = pygame.Surface((20, 20), pygame.SRCALPHA)
farmer_surface = pygame.Surface((20, 20), pygame.SRCALPHA)

pygame.draw.rect(
    bag_surface,
    (115, 72, 35),
    (1, 1, 18, 18)
)

pygame.draw.line(
    bag_surface,
    (220, 185, 55),
    (3, 10),
    (16, 10),
    1
)

first_bag_surface.blit(bag_surface, (0, 0))

pygame.draw.line(
    first_bag_surface,
    (75, 45, 22),
    (6, 2),
    (12, 2),
    2
)

pygame.draw.rect(
    first_bag_surface,
    (90, 55, 25),
    (9, 1, 3, 3)
)

pygame.draw.rect(
    farmer_surface,
    (55, 100, 160),
    (3, 8, 14, 10)
)

pygame.draw.rect(
    farmer_surface,
    (35, 65, 115),
    (6, 8, 8, 10)
)

pygame.draw.rect(
    farmer_surface,
    (205, 155, 105),
    (1, 9, 4, 7)
)

pygame.draw.rect(
    farmer_surface,
    (205, 155, 105),
    (15, 9, 4, 7)
)

pygame.draw.rect(
    farmer_surface,
    (210, 165, 115),
    (3, 2, 14, 13)
)

pygame.draw.rect(
    farmer_surface,
    (195, 145, 100),
    (1, 6, 3, 5)
)

pygame.draw.rect(
    farmer_surface,
    (195, 145, 100),
    (16, 6, 3, 5)
)

pygame.draw.rect(
    farmer_surface,
    (105, 65, 30),
    (1, 3, 18, 4)
)

pygame.draw.rect(
    farmer_surface,
    (125, 78, 35),
    (1, 3, 18, 4) 
)

pygame.draw.rect(
    farmer_surface,
    (125, 78, 35),
    (5, 0, 10, 6)
)

pygame.draw.rect(
    farmer_surface,
    (75, 45, 22),
    (5, 5, 10, 2)
)

pygame.draw.rect(
    farmer_surface,
    (30, 25, 20),
    (5, 8, 3, 3)
)

pygame.draw.rect(
    farmer_surface,
    (30, 25, 20),
    (12, 8, 3, 3)
)

pygame.draw.rect(
    farmer_surface,
    (180, 125, 85),
    (9, 10, 2, 2)
)

pygame.draw.line(
    farmer_surface,
    (100, 55, 45),
    (8, 13),
    (12, 13),
    1
)

obstacle_x = []
obstacle_y = []

obstacles = 10

while len(obstacle_x) < obstacles:

    new_x = random.randrange(0,800, 20)
    new_y = random.randrange(0, 600, 20)

    ok = True

    if abs(new_x - x) + abs(new_y - y) <= 100:
        ok = False

    if new_x == food_x and new_y == food_y:
        ok = False

    for j in range(len(obstacle_x)):
        if new_x == obstacle_x[j] and new_y == obstacle_y[j]:
            ok = False

    if ok == True:
        obstacle_x.append(new_x)
        obstacle_y.append(new_y)

big_font = pygame.font.SysFont(None, 80)
medium_font = pygame.font.SysFont(None, 50)
window_closed = False
paused = False
delay_time = 150
running = True
waiting = True

while waiting:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            waiting = False
            running = False
            window_closed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting = False
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            waiting = False

    screen.fill((10, 10, 10))

    start_text = font.render(
        "Press SPACE OR CLICK TO Start",
        True,
        (150,150,150)
    )

    screen.blit(start_text, (250, 280))

    pygame.display.flip()
    pygame.time.delay(150)
    
started = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            window_closed = True
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                if paused:
                    paused = False
                else: 
                    paused = True

            if paused == False: 

                if event.key == pygame.K_UP:
                    move_x = 0
                    move_y = -20

                if event.key == pygame.K_DOWN:
                    move_x = 0
                    move_y = 20

                if event.key == pygame.K_RIGHT:
                    move_x = 20
                    move_y = 0

                if event.key == pygame.K_LEFT:
                    move_x = -20
                    move_y = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            if paused:
                paused = False

    if paused:

        screen.fill((10, 10, 10))
        
        pause_text = font.render(
            "PAUSED",
            True,
            (150, 150, 150)
        )

        pause_rect = pause_text.get_rect(center = (400, 300))
        screen.blit(pause_text, pause_rect)

        pygame.display.flip()
        pygame.time.delay(100)

        continue

    if started == True:
        x = x + move_x
        y = y + move_y

    if x >= 800:
        x = 0
        
    if x < 0:
        x = 780

    if y >= 600:
        y = 0

    if y < 0:
        y = 580

    for i in range(len(body_x) - 1):
        if x == body_x[i] and y == body_y[i]:
            running = False

    for j in range(len(obstacle_x)):
        if x == obstacle_x[j] and y == obstacle_y[j]:
            running = False

    if x == food_x and y == food_y:

        score +=1
        length += 1

        food_x = random.randrange(0, 800, 20)
        food_y = random.randrange(0, 600, 20)

        food_ok = False

        while food_ok == False:
            food_ok = True

            for j in range(len(obstacle_x)):
                if food_x == obstacle_x[j] and food_y == obstacle_y[j]:
                    food_ok = False

            if food_ok == False:
                food_x = random.randrange(0, 800, 20)
                food_y = random.randrange(0, 600, 20)

        if score % 5 == 0:
            delay_time = delay_time - 20

            if delay_time < 50:
                delay_time = 50

    body_x.append(x)
    body_y.append(y)

    if len(body_x) > length:
        del body_x[0]
        del body_y[0]
        
    screen.fill((92, 62, 38))
    surface.fill((0, 0, 0, 0))

    for lane_y in range(0, 600, 40):
        pygame.draw.rect(
            screen, 
            (82, 52, 31), 
            (0, lane_y, 800, 40)
            )

        for soil_x in range(0, 800, 20):
            pygame.draw.line(
                screen,
                (105, 72, 43),
                (soil_x + 3, lane_y + 10),
                (soil_x + 15, lane_y + 10),
                2
            )

            pygame.draw.line(
                screen,
                (65, 40, 24),
                (soil_x + 7, lane_y + 27),
                (soil_x + 18, lane_y + 27),
                2
            )

        pygame.draw.line(
            screen,
            (55, 35, 22),
            (0, lane_y + 39),
            (800, lane_y + 39),
            2
        )

    for grid_y in range(0, 600, 20):
        for grid_x in range(0, 800, 20):
                status = crop_status[grid_y // 20][grid_x // 20]

                if status == 0:
                    pygame.draw.line(
                        surface,
                        (60, 130, 40, 90),
                        (grid_x + 10, grid_y + 18),
                        (grid_x + 10, grid_y + 9),
                        2
                    )

                    pygame.draw.line(
                        surface,
                        (70, 145, 45, 90),
                        (grid_x + 10, grid_y + 14),
                        (grid_x + 6, grid_y + 11),
                        2
                    )
                    
                elif status == 1:
                    pygame.draw.line(
                        surface,
                        (50, 115, 35, 90),
                        (grid_x + 10, grid_y + 19),
                        (grid_x + 10, grid_y + 5),
                        4
                    )

                    pygame.draw.line(
                        surface, 
                        (65, 140, 40, 90),
                        (grid_x + 10, grid_y + 14),
                        (grid_x + 4, grid_y +10),
                        3
                    )

                    pygame.draw.line(
                        surface,
                        (65, 140, 40, 90),
                        (grid_x + 10, grid_y + 12),
                        (grid_x + 16, grid_y + 8),
                        3
                    )

                    pygame.draw.line(
                        surface,
                        (220, 185, 55, 90),
                        (grid_x + 10, grid_y + 6),
                        (grid_x + 16, grid_y + 8),
                        3
                    )

                elif status == 2:
                    pass

    screen.blit(surface, (0, 0))
    for j in range(len(obstacle_x)):

        ox = obstacle_x[j]
        oy = obstacle_y[j]

        pygame.draw.polygon(
            screen,
            [45, 30, 20],
            [
                (ox + 1, oy + 7),
                (ox + 4, oy + 3)
            ]
        )

        pygame.draw.rect(
            screen,
            (128, 128, 128),
            (
                obstacle_x[j],
                obstacle_y[j],
                20,
                20
            )
        )

    pygame.draw.polygon(
        screen,
        (205, 170, 45),
        [
            (food_x + 1, food_y + 3),
            (food_x + 4, food_y + 1),
            (food_x + 8, food_y + 2),
            (food_x + 12, food_y + 1),
            (food_x + 16, food_y + 3),
            (food_x + 19, food_y + 2),
            (food_x + 18, food_y + 6),
            (food_x + 19, food_y + 10),
            (food_x + 17, food_y + 14),
            (food_x + 19, food_y + 17),
            (food_x + 15, food_y + 19),
            (food_x + 11, food_y + 18),
            (food_x + 7, food_y + 19),
            (food_x + 3, food_y + 17),
            (food_x + 1, food_y + 14),
            (food_x + 2, food_y + 10),
            (food_x + 1, food_y + 6)
        ]
    )

    pygame.draw.line(
        screen,
        (240, 205, 70),
        (food_x + 3, food_y + 16),
        (food_x + 8, food_y + 4),
        2
    )

    pygame.draw.line(
        screen,
        (175, 140, 30),
        (food_x + 7, food_y + 17),
        (food_x + 12, food_y + 3),
        2
    )

    pygame.draw.line(
        screen,
        (240, 205, 70),
        (food_x + 11, food_y + 16),
        (food_x + 16, food_y + 5),
        2
    )

    pygame.draw.line(
        screen,
        (160, 125, 25),
        (food_x + 3, food_y + 7),
        (food_x + 16, food_y + 12),
        1
    )

    pygame.draw.line(
        screen,
        (250, 220, 90),
        (food_x + 4, food_y + 4),
        (food_x + 15, food_y + 15)
    )

    if move_y == 20:
        angle = 180

    elif move_x == -20:
        angle = 90

    elif move_y == -20:
        angle = 0

    elif move_x == 20:
        angle = 270

    for b in range(len(body_x)):
        
        if b == 0:
            bag = first_bag_surface
        else:
            bag = bag_surface

        rotated_bag = pygame.transform.rotate(
            bag, 
            angle
        )

        bag_rect = rotated_bag.get_rect(
            center = (
                body_x[b] + 10,
                body_y[b] + 10
            )
        )

        screen.blit(
            rotated_bag,
            bag_rect
        )

    rotated_farmer = pygame.transform.rotate(
        farmer_surface,
        angle
    )

    farmer_rect = rotated_farmer.get_rect(
        center = (
            x + 10, 
            y + 10
        )
    )

    screen.blit(
        rotated_farmer,
        farmer_rect
    )

    score_text = font.render(
        "Score: " + str(score), 
        True, 
        (255, 255, 255)
    )

    screen.blit(score_text, (10, 10))

    length_text = font.render(
        "Length: " + str(length),
        True,
        (255, 255, 255)
    )

    screen.blit(length_text, (120, 10))

    pygame.display.flip()
    pygame.time.delay(delay_time)

ending = True

if window_closed == True:
    ending = False

while ending:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ending = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ending = False

        if event.type == pygame.MOUSEBUTTONDOWN:
                    ending = False

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()