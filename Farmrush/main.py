import pygame
import random
import asyncio

async def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    x = 400
    y = 300

    move_x = 20
    move_y = 0

    last_x = 20
    last_y = 0

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
    font = pygame.font.Font(None, 30)

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
        (150, 100, 55),
        (1, 1, 18, 18)
    )

    pygame.draw.rect(
        bag_surface,
        (75, 45, 22),
        (5, 5, 10, 10)
    )

    for dot_x, dot_y in [(6, 6), (11, 12), (8, 9)]:
       pygame.draw.rect(
           bag_surface,
           (230, 195, 60),
           (dot_x, dot_y, 1, 1)
       ) 

    for dot_x, dot_y in [(6, 12), (11, 6)]:
       pygame.draw.rect(
           bag_surface,
           (230, 195, 60),
           (dot_x, dot_y, 2, 2)
       ) 

    first_bag_surface.blit(bag_surface, (0, 0))

    pygame.draw.line(
        first_bag_surface,
        (235, 200, 110),
        (5, 17),
        (15, 17),
        3
    )

    pygame.draw.rect(
        first_bag_surface,
        (255, 235, 160),
        (8, 15, 4, 4)
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
        (225, 190, 80),
        (1, 3, 18, 4)
    )

    pygame.draw.rect(
        farmer_surface,
        (225, 190, 80),
        (5, 0, 10, 6)
    )

    pygame.draw.rect(
        farmer_surface,
        (170, 120, 45),
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

    big_font = pygame.font.Font(None, 80)
    medium_font = pygame.font.Font(None, 50)
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

        screen.blit(surface, (0,0))

        start_text = font.render(
            "Press SPACE OR CLICK TO Start",
            True,
            (150,150,150)
        )

        screen.blit(start_text, (250, 280))

        pygame.display.flip()
        await asyncio.sleep(0.15)
    
    playing_game = not window_closed

    while playing_game:

        x = 400
        y = 300

        move_x = 20
        move_y = 0

        last_x = 20
        last_y = 0

        score = 0
        length = 1

        body_x = []
        body_y = []

        delay_time = 150

        paused = False
        running = True

        food_x = random.randrange(0, 800, 20)
        food_y = random.randrange(0, 600, 20)

        bonus_x = -20
        bonus_y = -20
        bonus_active = False

        current_time = pygame.time.get_ticks()
        bonus_spawn_time = current_time + 30000

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    playing_game = False
                    window_closed = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:

                        if paused:
                            paused = False
                        else: 
                            paused = True

                    if paused == False: 

                        if event.key == pygame.K_UP:
                            if last_y != 20:
                                move_x = 0
                                move_y = -20

                        if event.key == pygame.K_DOWN:
                            if last_y != -20:
                                move_x = 0
                                move_y = 20

                        if event.key == pygame.K_RIGHT:
                            if last_x != -20:    
                                move_x = 20
                                move_y = 0

                        if event.key == pygame.K_LEFT:
                            if last_x != 20:
                                move_x = -20
                                move_y = 0

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if paused:
                        paused = False

            if window_closed == True:
                break

            if paused == True:
                pause_text = font.render(
                    "PAUSED",
                    True,
                    (150, 150, 150)
                )

                pause_rect = pause_text.get_rect(center = (400, 300))
                screen.blit(pause_text, pause_rect)

                pygame.display.flip()
                await asyncio.sleep(0.15)
            
                continue

            x = x + move_x
            y = y + move_y

            last_x = move_x
            last_y = move_y

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
                    bonus_start_time = current_time






            if bonus_active == True:
                if current_time - bonus_start_time >= 8000:
                    bonus_active = False
                    bonus_x = -20
                    bonus_y = -20

                    bonus_spawn_time = current_time + 30000

            if bonus_active == True:
                snake_head = pygame.Rect(x, y, 20, 20)
                bonus_rect = pygame.Rect(bonus_x, bonus_y, 20, 20)

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

                bonus_age = pygame.time.get_ticks() - bonus_start_time

                if bonus_age < 5000 or (bonus_age // 150) % 2 == 0:

                    pygame.draw.rect(
                        screen,
                        (140, 100, 30),
                        (bonus_x + 1, bonus_y + 4, 18, 14)
                    )

                    pygame.draw.rect(
                        screen,
                        (225, 185, 65),
                        (bonus_x + 2, bonus_y + 5, 16, 11)
                    )

                    pygame.draw.rect(
                        screen,
                        (245, 215, 110),
                        (bonus_x + 2, bonus_y + 5, 16, 2)
                    )

                    pygame.draw.rect(
                        screen,
                        (190, 150, 45),
                        (bonus_x + 2, bonus_y + 14, 16, 2)
                    )

                    for dash_x, dash_y in [(3, 8), (9, 9), (15, 8), (4, 11), (10, 12), (14, 11)]:
                        pygame.draw.line(
                            screen,
                            (175, 135, 40),
                            (bonus_x + dash_x, bonus_y + dash_y),
                            (bonus_x + dash_x + 2, bonus_y + dash_y),
                            1
                        )

                    pygame.draw.rect(
                        screen,
                        (165, 80, 45),
                        (bonus_x + 6, bonus_y + 4, 2, 14),
                    )

                    pygame.draw.rect(
                        screen,
                        (165, 80, 45),
                        (bonus_x + 12, bonus_y + 4, 2, 14)
                    )

                    for wisp_x, wisp_y in [(3, 4), (9, 4), (16, 4)]:
                        pygame.draw.line(
                            screen,
                            (245, 215, 110),
                            (bonus_x + wisp_x, bonus_y + wisp_y),
                            (bonus_x + wisp_x - 1, bonus_y + wisp_y - 2),
                            1
                        )










            screen.blit(surface, (0, 0))
            for j in range(len(obstacle_x)):

                ox = obstacle_x[j]
                oy = obstacle_y[j]

                pygame.draw.polygon(
                    screen,
                    [45, 30, 20],
                    [
                        (ox + 1, oy + 7),
                        (ox + 4, oy + 3),
                        (ox + 10, oy + 1),
                        (ox + 16, oy + 1),
                        (ox + 19, oy + 9),
                        (ox + 18, oy + 15),
                        (ox + 14, oy + 19),
                        (ox + 7, oy + 18),
                        (ox + 2, oy + 15),
                        (ox + 1, oy + 7)
                    ]
                )

                pygame.draw.polygon(
                    screen,
                    (25, 75, 105),
                    [
                        (ox + 3, oy + 8),
                        (ox + 7, oy + 4),
                        (ox + 13, oy + 4),
                        (ox + 17, oy + 8),
                        (ox + 16, oy + 14),
                        (ox + 6, oy + 16),
                        (ox + 3, oy + 13)
                    ]
                )

                pygame.draw.line(
                    screen,
                    (25, 75, 105),
                    (ox + 5, oy + 12),
                    (ox + 14, oy + 14)
                )

                pygame.draw.line(
                    screen,
                    (80, 160, 185),
                    (ox + 6, oy + 7),
                    (ox + 11, oy + 6),
                    1
                )

                pygame.draw.line(
                    screen,
                    (95, 175, 195),
                    (ox + 12, oy + 9),
                    (ox + 15, oy + 9),
                    1
                )

                pygame.draw.rect(
                    screen,
                    (105, 65, 35),
                    (ox + 2, oy + 16, 3, 2)
                )

                pygame.draw.rect(
                    screen,
                    (105, 65, 35),
                    (ox + 15, oy + 3, 3, 2)
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

            if bonus_active == True:
                bonus_text = font.render(
                    "BONUS +5",
                    True,
                    (255, 255, 255)
                )

                screen.blit(bonus_text, (240, 10))

            else:
                seconds_left = (bonus_spawn_time - pygame.time.get_ticks()) // 1000 + 1

                if seconds_left < 0:
                    seconds_left = 0

                bonus_timer_text = font.render(
                    "Bonus in:" + str(seconds_left),
                    True,
                    (255, 255, 255)
                )

                screen.blit(bonus_timer_text, (240, 10))

            pygame.display.flip()
            await asyncio.sleep(delay_time / 1000)

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

                            screen.blit(surface, (0,0))
            

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
                await asyncio.sleep(0.1)

    pygame.quit()

asyncio.run(main())