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


# Colors
white = pg.Color(255, 255, 255)
black = pg.Color(0, 0, 0)
red = pg.Color("red")
cool_grey = pg.Color(108, 117, 125)

# Game loop
while True:
    # Event checker
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((237, 242, 244))

    # Border Lines
    pg.draw.line(screen, black, (50, 50), (50, 550), 4)
    pg.draw.line(screen, black, (750, 50), (750, 550), 4)
    pg.draw.line(screen, black, (50, 50), (750, 50), 4)
    pg.draw.line(screen, black, (50, 550), (750, 550), 4)

    # Card slots lines

    vertical_line_adder = 150
    horizontal_line_adder = 150

    for _ in range(7):
        pg.draw.line(screen, cool_grey,
                     (vertical_line_adder, 50), (vertical_line_adder, 550), 4)
        vertical_line_adder += 100

    for _ in range(7):
        pg.draw.line(screen, cool_grey,
                     (50, horizontal_line_adder), (750, horizontal_line_adder),
                     4)
        horizontal_line_adder += 100

    # Upadte the full surface display
    pg.display.flip()
    # Framerate 60fps
    clock.tick(60)
