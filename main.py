import pygame as pg
import sys as s


display = pg.display.set_mode((800, 600))
pg.init()
pg.display.set_caption('Physic Project')


class Circle:
    def __init__(self, color, fill=False):
        self.color = color
        self.fill = fill
        self.radius = 1
        self.mass = 1
        self.speed = 1
        self.B = 1
        self.q = 1

    def draw(self):




"R = mU/(Bq)"


def start():
    show_menu = True
    while show_menu:
        event = pg.event.poll()
        if event.type == pg.QUIT:
            s.exit()
        display.fill((255, 255, 255))


        pg.display.update()

start()