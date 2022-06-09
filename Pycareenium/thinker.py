import pygame as pg
from statistical_mentalics import *

background_color = "black"

pg.init()
screen = pg.display.set_mode((400, 800))
pg.display.update()

thinking = True

test_simm = Simm(5, 100, 200, 0, 5)

while thinking:
    for event in pg.event.get():

        if event.type == pg.QUIT:
            thinking = False