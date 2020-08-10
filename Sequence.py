import pygame as pg
import sys

# Initialize pg
pg.init()
# Create clock for framerate
clock = pg.time.Clock()


# Screen
screen_w = 800
screen_h = 600
screen = pg.display.set_mode((screen_w, screen_h))

# Game loop
while True:
    # Event checker
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Upadte the full surface display
    pg.display.flip()
    # Framerate 60fps
    clock.tick(60)
