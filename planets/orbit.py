'''Program for simulating the orbits of planets'''

import random
import pygame
from planet_class import Planet
from config import WIDTH,HEIGHT
from config import WHITE,BLUE,RED,YELLOW,DARK_GREY,BLACK,ORANGE,PINK,GREEN,ROSE

COLORS=[WHITE,BLUE,RED,YELLOW,DARK_GREY,ORANGE,PINK,GREEN,ROSE]

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Planet simulation")

def main():
    'Main funtion'
    run = True
    clock = pygame.time.Clock()

    sun=Planet(0,0,30, YELLOW,1.98892e30,True)
    sun.sun=True

    earth=Planet(-1*Planet.AU,0,16, BLUE,5.9742e24,True)
    earth.y_vel=29.783*1000

    mars=Planet(-1.524*Planet.AU,0,12, RED,6.39e23,True)
    mars.y_vel=24.077*1000

    mercury=Planet(0.387*Planet.AU,0,8, DARK_GREY,3.30e23,True)
    mercury.y_vel=-47.4*1000

    venus=Planet(0.723*Planet.AU,0,14, WHITE,4.8685e24,True)
    venus.y_vel=-35.02*1000

    tax=Planet(3*Planet.AU,0,30, PINK,4.8685e27,True)
    tax.y_vel=-10.02*1000

    demos=Planet(-3*Planet.AU,0,30, ORANGE,4.8685e27,True)
    demos.y_vel=15.02*1000

    picos=Planet(1.5*Planet.AU,0.5*Planet.AU,50, BLUE,4.8685e27,True)
    picos.y_vel=-20.02*1000

    planis=[]
    for i in range(15):
        planis.append(0)
        planis[i]=Planet((0.5+0.25*i)*Planet.AU,
                         Planet.AU/2,
                         5,
                         random.choice(COLORS),
                         4.8685e27*random.random(),
                         True)
        planis[i].y_vel=-25*1000+i*1000*random.random()

    # moon=Planet(-1.1*Planet.AU,0,5, WHITE,7.342e22)
    # moon=Planet(-1.0025695*Planet.AU,0,5, WHITE,7.342e22)
    moon=Planet(-5*Planet.AU-380000000,0,20, BLUE,7.342e27,True)
    moon.y_vel=(20)*1000
    # moon.y_vel=(26.783+1.022)*1000

    # planets=[sun, earth, mars, mercury, venus, tax,demos, picos,
    planets=[sun, earth, mars, mercury, venus]+planis
    # planets=[sun, earth, moon]

    while run:
        clock.tick(60)
        WIN.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT    :
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)
            if abs(planet.x)>20*planet.AU or abs(planet.y)>20*planet.AU:
                planets.pop()
                print(len(planets))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
