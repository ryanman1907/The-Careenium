from thinker import screen, background_color
import pygame as pg

class Simm:

    def __init__(self, radius, x, y, v_x, v_y, mass, color):
        self.radius = radius
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.mass = mass
        self.color = color
    
    def show(self, color):
        global screen
        pg.draw.circle(screen, color, (self.x, self.y), self.radius)

    def think(self):
        self.show(pg.color(background_color))

        self.x += self.v_x
        self.y += self.v_y

        self.show(pg.color(self.color))


