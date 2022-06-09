import pygame as pg
from statistical_mentalics import *

pg.init()
screen = pg.display.set_mode((400, 800))
pg.display.update()

thinking = True
while thinking:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            thinking = False