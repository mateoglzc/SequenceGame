from cool_pgColors import cools
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
cool_grey = pg.Color(108, 117, 125)
cool_blue = pg.Color(152, 193, 217)


# Game loop
while True:
    # Event checker
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((237, 242, 244))

    # Border Lines
    pg.draw.line(screen, cools["black"], (50, 50), (50, 550), 4)
    pg.draw.line(screen, cools["black"], (750, 50), (750, 550), 4)
    pg.draw.line(screen, cools["black"], (50, 50), (750, 50), 4)
    pg.draw.line(screen, cools["black"], (50, 550), (750, 550), 4)

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

    # IDK how to make this more efficient

    # # Free Spaces
    # pg.draw.circle(screen, cool_blue, (100, 100), 35, 10)
    # pg.draw.circle(screen, cool_blue, (100, 500), 35, 10)
    # pg.draw.circle(screen, cool_blue, (700, 100), 35, 10)
    # pg.draw.circle(screen, cool_blue, (700, 500), 35, 10)

    # # Tiger
    # pg.draw.circle(screen, cools["tiger"], (600, 500), 35)
    # pg.draw.circle(screen, cools["tiger"], (200, 100), 35)
    # # Kangaroo
    # pg.draw.circle(screen, cools["kangaroo"], (500, 500), 35)
    # pg.draw.circle(screen, cools["kangaroo"], (500, 200), 35)
    # # Giraffe
    # pg.draw.circle(screen, cools["giraffe"], (400, 500), 35)
    # pg.draw.circle(screen, cools["giraffe"], (500, 300), 35)
    # # Wolf
    # pg.draw.circle(screen, cools["wolf"], (300, 500), 35)
    # pg.draw.circle(screen, cools["wolf"], (300, 300), 35)
    # # Turtle
    # pg.draw.circle(screen, cools["turtle"], (200, 500), 35)
    # pg.draw.circle(screen, cools["turtle"], (200, 200), 35)
    # # Fox
    # pg.draw.circle(screen, cools["fox"], (200, 400), 35)
    # pg.draw.circle(screen, cools["fox"], (300, 300), 35)
    # # Rendeer
    # pg.draw.circle(screen, cools["rendeer"], (500, 100), 35)
    # pg.draw.circle(screen, cools["rendeer"], (700, 300), 35)
    # # Lion
    # pg.draw.circle(screen, cools["lion"], (500, 300), 35)
    # pg.draw.circle(screen, cools["lion"], (600, 100), 35)
    # # Crocodile
    # pg.draw.circle(screen, cools["crocodile"], (400, 500), 35)
    # pg.draw.circle(screen, cools["crocodile"], (600, 300), 35)
    # # Zebra
    # pg.draw.circle(screen, cools["zebra"], (200, 400), 35)
    # pg.draw.circle(screen, cools["zebra"], (300, 300), 35)
    # # Monkey
    # pg.draw.circle(screen, cools["monkey"], (200, 400), 35)
    # pg.draw.circle(screen, cools["monkey"], (300, 300), 35)
    # # Hippo
    # pg.draw.circle(screen, cools["hippo"], (200, 400), 35)
    # pg.draw.circle(screen, cools["hippo"], (300, 300), 35)
    # # Panda
    # pg.draw.circle(screen, cools["panda"], (200, 400), 35)
    # pg.draw.circle(screen, cools["panda"], (300, 300), 35)
    # # Shark
    # pg.draw.circle(screen, cools["shark"], (200, 400), 35)
    # pg.draw.circle(screen, cools["shark"], (300, 300), 35)
    # # Camel
    # pg.draw.circle(screen, cools["camel"], (200, 400), 35)
    # pg.draw.circle(screen, cools["camel"], (300, 300), 35)
    # # Orca
    # pg.draw.circle(screen, cools["orca"], (200, 400), 35)
    # pg.draw.circle(screen, cools["orca"], (300, 300), 35)
    # # Elephant
    # pg.draw.circle(screen, cools["elephant"], (200, 400), 35)
    # pg.draw.circle(screen, cools["elephant"], (300, 300), 35)
    # # Penguin
    # pg.draw.circle(screen, cools["penguin"], (200, 400), 35)
    # pg.draw.circle(screen, cools["penguin"], (300, 300), 35)

    # Upadte the full surface display
    pg.display.flip()
    # Framerate 60fps
    clock.tick(60)
