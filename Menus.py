import pygame
import tutor

BLACK = (0, 0, 0)

fondo = pygame.image.load('img/Mesa.png')  # fondo
jugar = pygame.image.load('img/jugar.png')
tuto = pygame.image.load('img/tutorial.png')
salid = pygame.image.load('img/salir.png')
pygame.mixer.init()
box = pygame.mixer.Sound('music/The_Music_Box.mp3')


def inicial(ventana, clock):
    sy = 48
    sx = 406

    ty = 256
    tx = 398

    ey = 480
    ex = 393

    done = False
    click = False
    box.play()
    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
            if event.type == pygame.MOUSEBUTTONUP:
                click = False

        maus_pos = pygame.mouse.get_pos()
        x_m = maus_pos[0]
        y_m = maus_pos[1]

        mouse = pygame.draw.rect(ventana, BLACK, (x_m, y_m, 1, 1))
        ventana.blit(fondo, (0, 0))
        pygame.draw.rect(ventana, BLACK, (406, 51, 477, 155))
        pygame.draw.rect(ventana, BLACK, (400, 258, 487, 157))
        pygame.draw.rect(ventana, BLACK, (394, 481, 496, 159))
        star = ventana.blit(jugar, (sx, sy))
        tutorial = ventana.blit(tuto, (tx, ty))
        exi = ventana.blit(salid, (ex, ey))

        if mouse.colliderect(star):
            sy = 43
            sx = 411
            touch_j = True
        else:
            sy = 48
            sx = 406
            touch_j = False

        if mouse.colliderect(tutorial):
            ty = 261
            tx = 403
            touch_t = True
        else:
            ty = 256
            tx = 398
            touch_t = False

        if mouse.colliderect(exi):
            ey = 472
            ex = 399
            touch_e = True
        else:
            ey = 480
            ex = 393
            touch_e = False

        if touch_j and click:
            done = True
            box.stop()
        elif touch_t and click:

            tutor.tutor(ventana, clock)
            click = False

        elif touch_e and click:
            pygame.quit()
            exit()

        pygame.display.update()
        clock.tick(10)
