'''Class for planets'''

import math
import pygame
from config import WIDTH,HEIGHT
from config import WHITE

# pygame.init()
# FONT = pygame.font.SysFont("comicsans", 16)

class Planet:
    '''Planets class'''
    AU=149.6e6*1000
    G=6.67428e-11
    SCALE=150/AU
    # SCALE=200/AU
    TIMESTEP=3600*24
    DRAW_LIM=2000

    def __init__(self, x:int, y:int, radius:int, color:tuple(), mass:int, trail:bool)->None:
        '''initialisation'''
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.mass=mass

        self.orbit=[]
        self.sun=False
        self.distance_to_sun=0
        self.trail=trail

        self.x_vel=0
        self.y_vel=0

    def draw(self, win):
        'draws stuff'
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2 and self.trail:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))

            if len(updated_points)<self.DRAW_LIM:
                pygame.draw.lines(win, self.color, False, updated_points, 2)
            else:
                updated_points=updated_points[-self.DRAW_LIM:]
                pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        # if not self.sun:
        #     distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)}km", 1, WHITE)
        #     win.blit(distance_text,
        #              (x - distance_text.get_width()/2, y - distance_text.get_height()/2)
        #              )

    def attraction(self, other):
        '''calculates attraction force'''
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        '''calculates the current position'''
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))
        if len(self.orbit)>self.DRAW_LIM:
            self.orbit=self.orbit[-self.DRAW_LIM:]
