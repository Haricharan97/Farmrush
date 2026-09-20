import pygame
import random

pygame.init()

screen=pygame.display.set_mode((800,600))

x = 400
y = 300

move_x = 20
move_y = 0

food_x = random.randrange(0, 800, 20)
food_y = random.randrange(0, 600, 20)

bonus_x = -20
bonus_y = -20
new_bonus = True

bonus_active = False
bonus_start_time = 0

current_time = pygame.time.get_ticks()
bonus_spawn_time = current_time + 30000

score = 0
font = pygame.font.SysFont(None,30)

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
    
playing_game = not window_closed

while playing_game:

    x = 400
    y = 300

    move_x = 20
    move_y = 0

    score = 0
    length = 1

    body_x = []
    body_y = []

    delay_time = 150

    paused = False
    running = True

    food_x = random.randrange(0,800,20)
    food_y = random.randrange(0,600,20)

    bonus_x = -20
    bonus_y = -20
    bonus_active = False

    current_time = pygame.time.get_ticks()
    bonus_spawn_time = current_time + 30000

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                window_closed =True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if paused == False:
                        paused = True
                    else:
                        paused = False

                if event.key == pygame.K_UP:
                    if move_y != 20:
                        move_x = 0
                        move_y = -20

                if event.key == pygame.K_DOWN:
                    if move_y != -20:
                        move_x = 0
                        move_y = 20

                if event.key == pygame.K_RIGHT:
                    if move_x != -20:
                        move_x = 20
                        move_y = 0

                if event.key == pygame.K_LEFT:
                    if move_x != 20:
                        move_x = -20
                        move_y = 0

        if window_closed == True:
            break

        current_time = pygame.time.get_ticks()

        if paused == True:
            pause_text = font.render(
            "PAUSED",
            True,
            (150,150,150)
        )

            screen.blit(pause_text,(360, 290))
            pygame.display.flip()
            pygame.time.delay(150)
            continue

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

            food_ok = False

            food_x = random.randrange(0, 800, 20)
            food_y = random.randrange(0, 600, 20)


            while food_ok == False:
                food_ok = True

                for j in range(len(obstacle_x)):
                    if food_x == obstacle_x[j] and food_y == obstacle_y[j]:
                        food_ok = False

                for j in range(len(body_x)):
                    if food_x == body_x[j] and food_y == body_y[j]:
                        food_ok = False

                if food_ok == False:
                    food_x = random.randrange(0, 800, 20)
                    food_y = random.randrange(0, 600, 20)

            if score % 5 == 0:
                    delay_time = delay_time - 20

                    if delay_time < 50:
                        delay_time = 50

        current_time = pygame.time.get_ticks()

        if bonus_active == False:
            if current_time >= bonus_spawn_time:

                bonus_ok = False

                while bonus_ok == False:
                    bonus_x = random.randrange(0,800,20)
                    bonus_y = random.randrange(0,600,20)

                    bonus_ok = True

                    if bonus_x == food_x and bonus_y == food_y:
                        bonus_ok = False

                    for j in range(len(obstacle_x)):
                        if bonus_x == obstacle_x[j] and bonus_y == obstacle_y[j]:
                            bonus_ok = False

                    for j in range(len(body_x)):
                        if bonus_x == body_x[j] and bonus_y == body_y[j]:
                            bonus_ok = False

                bonus_active = True

        if bonus_active == True:
            snake_head = pygame.Rect(x,y,20,20)
            bonus_rect = pygame.Rect(bonus_x,bonus_y,20,20)

            if snake_head.colliderect(bonus_rect):
                score += 5

                bonus_active = False
                bonus_x = -20
                bonus_y = -20

                bonus_spawn_time = pygame.time.get_ticks() + 30000

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

        if bonus_active == True:
            pygame.draw.circle(
                screen,
                (255, 0, 255),
                (bonus_x + 10, bonus_y + 10),
                9
            )

            pygame.draw.circle( 
                screen,
                (255,255,255),
                (bonus_x + 10, bonus_y + 10),
                4
            )

        for b in range(len(body_x)):
            shade = 150 + b * 5

            if shade > 255:
                shade = 255

            pygame.draw.rect(
                screen,
                (0,shade,0),
                (body_x[b], body_y[b],19,19)
                )

        pygame.draw.rect(
            screen,
            (0,255,100),
            (x,y,20,20)
        )

        pygame.draw.rect(
            screen, 
            (0, 0, 0), 
            (x + 3, y + 3, 4, 4)
        )
        
        pygame.draw.rect(
            screen, 
            (0, 0, 0), 
            (x + 13, y + 3, 4, 4)
        )
        
        score_text = font.render(
            "Score: " + str(score), 
            True, 
            (255,255,255)
        )

        screen.blit(score_text, (10, 10))

        length_text = font.render(
            "Length: " + str(length),
            True,
            (255, 255, 255)
        )

        screen.blit(length_text, (120, 10))

        if bonus_active == True:
            bonus_text = font.render(
                "BONUS +5",
                True,
                (255,255,255)
            )
            screen.blit(bonus_text, (240, 10))

        else:
            seconds_left = (bonus_spawn_time - pygame.time.get_ticks()) // 1000 + 1
            if seconds_left < 0:
                seconds_left = 0

            bonus_timer_text = font.render(
                "Bonus in:" + str(seconds_left),
                True,
                (255,255,255)
            )

            screen.blit(bonus_timer_text, (240,10))

        pygame.display.flip()
        pygame.time.delay(delay_time)

    if window_closed == False:
        restart_waiting = True

        while restart_waiting:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    restart_waiting = False
                    playing_game = False
                    window_closed = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        restart_waiting = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        restart_waiting = False

            screen.fill((10,10,10))

            game_over_text = big_font.render(
                "GAME OVER",
                True,
                (255,255,255)
                )

            final_score_text = medium_font.render(
                "Score: " + str(score),
                True,
                (255,255,255)
                )

            final_length_text = font.render(
                "Length: " + str(length),
                True,
                (180,180,180)
                )

            restart_text = font.render(
                "Press SPACE To Restart",
                True,
                (150,150,150)
                )

            screen.blit(game_over_text, (220,160))
            screen.blit(final_score_text, (320,260))
            screen.blit(final_length_text, (350,320))
            screen.blit(restart_text, (270, 390))

            pygame.display.flip()
            pygame.time.delay(100)

pygame.quit()