from cool_pgColors import cools
from Player import Player
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
red = pg.Color("red")

# Chips


class Chip():

    def __init__(self, color):
        self.color = color

    def PlaceChip(self, pos: tuple, screen):
        return pg.draw.circle(screen, self.color, pos, 10)


player1_chips = []
player2_chips = []
chips_placed = [player1_chips, player2_chips]

# Player
player1 = Player("Matt", False)
player1.chips = Chip((237, 31, 35))
player2 = Player("Emi", False)
player2.chips = Chip((73, 159, 104))

turn = 1


def turn_decider(turn_num, pos):
    global turn
    if player2.turn:
        player2_chips.append(pos)
        turn += 1
    if player1.turn:
        player1_chips.append(pos)
        turn += 1


# Game loop
while True:

    if turn % 2 == 0:
        player2.turn = True
        player1.turn = False
    else:
        player1.turn = True
        player2.turn = False

    # Event checker
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            turn_decider(turn, pos)
    screen.fill((237, 242, 244))

    # Border Lines
    pg.draw.line(screen, cools["black"], (50, 50), (50, 550), 4)
    pg.draw.line(screen, cools["black"], (750, 50), (750, 550), 4)
    pg.draw.line(screen, cools["black"], (50, 50), (750, 50), 4)
    pg.draw.line(screen, cools["black"], (50, 550), (750, 550), 4)

    # Card slots lines

    vertical_line_adder = 150
    horizontal_line_adder = 133

    for _ in range(6):
        pg.draw.line(screen, cool_grey,
                     (vertical_line_adder, 50), (vertical_line_adder, 550), 4)
        vertical_line_adder += 100

    for _ in range(5):
        pg.draw.line(screen, cool_grey,
                     (50, horizontal_line_adder), (750, horizontal_line_adder),
                     4)
        horizontal_line_adder += 84

    # IDK how to make this more efficient

    # Free Spaces
    pg.draw.circle(screen, cool_blue, (100, 94), 25, 7)
    pg.draw.circle(screen, cool_blue, (100, 512), 25, 7)
    pg.draw.circle(screen, cool_blue, (700, 94), 25, 7)
    pg.draw.circle(screen, cool_blue, (700, 512), 25, 7)

    # Tiger
    pg.draw.circle(screen, cools["tiger"], (600, 512), 25)
    pg.draw.circle(screen, cools["tiger"], (200, 94), 25)
    # Kangaroo
    pg.draw.circle(screen, cools["kangaroo"], (500, 512), 25)
    pg.draw.circle(screen, cools["kangaroo"], (500, 176), 25)
    # Giraffe
    pg.draw.circle(screen, cools["giraffe"], (400, 512), 25)
    pg.draw.circle(screen, cools["giraffe"], (500, 260), 25)
    # Wolf
    pg.draw.circle(screen, cools["wolf"], (300, 512), 25)
    pg.draw.circle(screen, cools["wolf"], (300, 260), 25)
    # Turtle
    pg.draw.circle(screen, cools["turtle"], (200, 512), 25)
    pg.draw.circle(screen, cools["turtle"], (200, 176), 25)
    # Fox
    pg.draw.circle(screen, cools["fox"], (200, 428), 25)
    pg.draw.circle(screen, cools["fox"], (300, 176), 25)
    # Rendeer
    pg.draw.circle(screen, cools["rendeer"], (100, 428), 25)
    pg.draw.circle(screen, cools["rendeer"], (700, 260), 25)
    # Lion
    pg.draw.circle(screen, cools["lion"], (300, 428), 25)
    pg.draw.circle(screen, cools["lion"], (600, 94), 25)
    # Crocodile
    pg.draw.circle(screen, cools["crocodile"], (400, 428), 25)
    pg.draw.circle(screen, cools["crocodile"], (600, 260), 25)
    # Zebra
    pg.draw.circle(screen, cools["zebra"], (500, 428), 25)
    pg.draw.circle(screen, cools["zebra"], (600, 176), 25)
    # Monkey
    pg.draw.circle(screen, cools["monkey"], (600, 428), 25)
    pg.draw.circle(screen, cools["monkey"], (100, 260), 25)
    # Hippo
    pg.draw.circle(screen, cools["hippo"], (700, 428), 25)
    pg.draw.circle(screen, cools["hippo"], (400, 260), 25)
    # Panda
    pg.draw.circle(screen, cools["panda"], (700, 344), 25)
    pg.draw.circle(screen, cools["panda"], (100, 176), 25)
    # Shark
    pg.draw.circle(screen, cools["shark"], (600, 344), 25)
    pg.draw.circle(screen, cools["shark"], (400, 176), 25)
    # Camel
    pg.draw.circle(screen, cools["camel"], (500, 344), 25)
    pg.draw.circle(screen, cools["camel"], (200, 260), 25)
    # Orca
    pg.draw.circle(screen, cools["orca"], (300, 344), 25)
    pg.draw.circle(screen, cools["orca"], (400, 94), 25)
    # Elephant
    pg.draw.circle(screen, cools["elephant"], (200, 344), 25)
    pg.draw.circle(screen, cools["elephant"], (500, 94), 25)
    # Penguin
    pg.draw.circle(screen, cools["penguin"], (100, 344), 25)
    pg.draw.circle(screen, cools["penguin"], (700, 176), 25)
    # Ostrich
    pg.draw.circle(screen, cools["ostrich"], (400, 344), 25)
    pg.draw.circle(screen, cools["ostrich"], (300, 94), 25)

    # Place Chips
    for i in player1_chips:
        pg.draw.circle(screen, player1.chips.color, i, 10)
    for i in player2_chips:
        pg.draw.circle(screen, player2.chips.color, i, 10)

    # Upadte the full surface display
    pg.display.flip()
    # Framerate 60fps
    clock.tick(60)
