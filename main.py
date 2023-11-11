import pygame as pg
import sys

pg.init()
s_h = 500
s_w = 500
sc = pg.display.set_mode((s_w, s_h))
border_position_h = 300
vel = 5

pl_x = 30
pl_y = 268
pl_size = 30
pl_jump_steps = 10
pl_is_jump = False


while True:
    pg.time.delay(40)
    sc.fill((0, 0, 0))
    pg.draw.line(sc, (255, 0, 0), (0, border_position_h), (s_w, border_position_h), 5)
    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        pl_x -= vel
    if keys[pg.K_RIGHT]:
        pl_x += vel

    if not(pl_is_jump):
        if keys[pg.K_SPACE]:
            pl_is_jump = True
    else:
        if pl_jump_steps >= -10:
            pl_y -= (pl_jump_steps * abs(pl_jump_steps)) * 0.5
            pl_jump_steps -= 1
        else:
            pl_jump_steps = 10
            pl_is_jump = False

    pg.draw.rect(sc, (255, 255, 255), (pl_x, pl_y, pl_size, pl_size))

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()