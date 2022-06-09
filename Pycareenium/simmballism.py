from driver import screen
import pygame as pg

class Simm:
    def __init__(self, size, x, y, v_x, v_y, mass):
        self.size = size
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.mass = mass
    
    def show(self):
        global screen
        pg.draw.circle(screen, "pink", self.x, self.y)

