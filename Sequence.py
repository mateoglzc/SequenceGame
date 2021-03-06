from cool_pgColors import cools
from Player import Player
import pygame as pg
import sys
import random
import math

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

# Cards
deck = ["tiger", "kangaroo", "giraffe", "wolf", "turtle",
        "fox", "rendeer", "lion", "crocodile", "zebra",
        "monkey", "hippo", "panda", "shark", "camel",
        "orca", "elephant", "penguin", "ostrich", "tiger",
        "kangaroo", "giraffe", "wolf", "turtle", "fox",
        "rendeer", "lion", "crocodile", "zebra", "monkey",
        "hippo", "panda", "shark", "camel", "orca",
        "elephant", "penguin", "ostrich"]

cards_taken = []

player1_cards = []
player2_cards = []

a = random.randint(0, (len(deck)-1))
cards_taken.append(a)
b = random.randint(0, (len(deck)-1))
while b in cards_taken:
    b = random.randint(0, (len(deck)-1))
cards_taken.append(b)
c = random.randint(0, (len(deck)-1))
while c in cards_taken:
    c = random.randint(0, (len(deck)-1))
cards_taken.append(c)

player1_cards.append(a)
player1_cards.append(b)
player1_cards.append(c)

a = random.randint(0, (len(deck)-1))
cards_taken.append(a)
b = random.randint(0, (len(deck)-1))
while b in cards_taken:
    b = random.randint(0, (len(deck)-1))
cards_taken.append(b)
c = random.randint(0, (len(deck)-1))
while c in cards_taken:
    c = random.randint(0, (len(deck)-1))
cards_taken.append(c)

player2_cards.append(a)
player2_cards.append(b)
player2_cards.append(c)


def round_up_x(num):
    num += 50
    return int(math.floor(num / 100)) * 100


def round_up_y(num):
    if num < 134:
        return 100
    if num < 218:
        return 200
    if num < 302:
        return 300
    if num < 386:
        return 400
    if num < 470:
        return 500
    if num < 554:
        return 600


def card_picker(x, y):
    if x == 100:
        if y == 100:
            return None
        if y == 200:
            return 31
        if y == 300:
            return 29
        if y == 400:
            return 18
        if y == 500:
            return 6
        if y == 600:
            return None
    if x == 200:
        if y == 100:
            return 19
        if y == 200:
            return 23
        if y == 300:
            return 33
        if y == 400:
            return 17
        if y == 500:
            return 5
        if y == 600:
            return 4
    if x == 300:
        if y == 100:
            return 37
        if y == 200:
            return 24
        if y == 300:
            return 22
        if y == 400:
            return 16
        if y == 500:
            return 7
        if y == 600:
            return 3
    if x == 400:
        if y == 100:
            return 34
        if y == 200:
            return 32
        if y == 300:
            return 30
        if y == 400:
            return 15
        if y == 500:
            return 8
        if y == 600:
            return 2
    if x == 500:
        if y == 100:
            return 35
        if y == 200:
            return 20
        if y == 300:
            return 21
        if y == 400:
            return 14
        if y == 500:
            return 9
        if y == 600:
            return 1
    if x == 600:
        if y == 100:
            return 26
        if y == 200:
            return 28
        if y == 300:
            return 27
        if y == 400:
            return 13
        if y == 500:
            return 10
        if y == 600:
            return 0
    if x == 700:
        if y == 100:
            return None
        if y == 200:
            return 36
        if y == 300:
            return 25
        if y == 400:
            return 12
        if y == 500:
            return 11
        if y == 600:
            return None
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
        card_used = card_picker(round_up_x(pos[0]), round_up_y(pos[1]))
        x = random.randint(0, (len(deck)-1))
        while x in cards_taken:
            x = random.randint(0, (len(deck)-1))
        cards_taken.append(x)
        if card_used in player2_cards:
            card_used_index = player2_cards.index(card_used)
            player2_cards[card_used_index] = x
        turn += 1
    if player1.turn:
        player1_chips.append(pos)
        card_used = card_picker(round_up_x(pos[0]), round_up_y(pos[1]))
        x = random.randint(0, (len(deck)-1))
        while x in cards_taken:
            x = random.randint(0, (len(deck)-1))
        cards_taken.append(x)
        if card_used in player1_cards:
            card_used_index = player1_cards.index(card_used)
            player1_cards[card_used_index] = x
        turn += 1


# Game loop
while True:

    if len(cards_taken) == len(deck):
        pg.quit()
        sys.exit()

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
            # print(round_up_x(pos[0]))

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

    pg.draw.circle(screen, cools[deck[player1_cards[0]]], (400, 575), 15)
    pg.draw.circle(screen, cools[deck[player1_cards[1]]], (370, 575), 15)
    pg.draw.circle(screen, cools[deck[player1_cards[2]]], (430, 575), 15)

    pg.draw.circle(screen, cools[deck[player2_cards[0]]], (30, 300), 15)
    pg.draw.circle(screen, cools[deck[player2_cards[1]]], (30, 270), 15)
    pg.draw.circle(screen, cools[deck[player2_cards[2]]], (30, 330), 15)

    # Upadte the full surface display
    pg.display.flip()
    # Framerate 60fps
    clock.tick(60)
