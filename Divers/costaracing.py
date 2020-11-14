#for finding if there are intersections
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

def ccw(A,B,C):
	return (C.y-A.y)*(B.x-A.x) > (B.y-A.y)*(C.x-A.x)

def intersect(A,B,C,D):
	return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

#for determining the intersections
def intersectLines( pt1, pt2, ptA, ptB ): 
    """ this returns the intersection of Line(pt1,pt2) and Line(ptA,ptB)
        
        returns a tuple: (xi, yi, valid, r, s), where
        (xi, yi) is the intersection
        r is the scalar multiple such that (xi,yi) = pt1 + r*(pt2-pt1)
        s is the scalar multiple such that (xi,yi) = pt1 + s*(ptB-ptA)
            valid == 0 if there are 0 or inf. intersections (invalid)
            valid == 1 if it has a unique intersection ON the segment    """

    DET_TOLERANCE = 0.00000001

    x1, y1 = pt1;   x2, y2 = pt2
    dx1 = x2 - x1;  dy1 = y2 - y1
    x, y = ptA;   xB, yB = ptB
    dx = xB - x;  dy = yB - y
    DET = (-dx1 * dy + dy1 * dx)

    if math.fabs(DET) < DET_TOLERANCE: return (0,0,0,0,0)
    DETinv = 1.0/DET
    r = DETinv * (-dy  * (x-x1) +  dx * (y-y1))
    s = DETinv * (-dy1 * (x-x1) + dx1 * (y-y1))
    xi = (x1 + r*dx1 + x + s*dx)/2.0
    yi = (y1 + r*dy1 + y + s*dy)/2.0
    return ( xi, yi, 1, r, s )


class Sprite():
    def Load(self):
        font = pygame.font.Font(None,24)
        self.xc = 150;self.yc = 450
        self.xf = int(self.xc); self.yf = int(self.yc)
        self.speed = 0
        self.lap = []
        self.laptime = []
        self.dt = 1.0
        self.angle=0
        self.speedo = []
        self.x_front=self.xc; self.y_front=self.yc-20
        self.x_front_i=int(self.x_front); self.y_front_i=int(self.y_front)
        self.sonar_0_distance=0; self.sonar_0_x=0; self.sonar_0_y=0
        self.sonar_30_distance=0; self.sonar_30_x=0; self.sonar_30_y=0
        self.sonar_60_distance=0; self.sonar_60_x=0; self.sonar_60_y=0
        self.sonar_90_distance=0; self.sonar_90_x=0; self.sonar_90_y=0
        self.sonar_180_distance=0; self.sonar_180_x=0; self.sonar_180_y=0
        self.sonar_270_distance=0; self.sonar_270_x=0; self.sonar_270_y=0
        self.sonar_300_distance=0; self.sonar_300_x=0; self.sonar_300_y=0
        self.sonar_330_distance=0; self.sonar_330_x=0; self.sonar_330_y=0
        for i in range(101):
            self.speedo += [font.render("SPEED "+str(i),1,ORANGE)]
        for i in range(1,5):
            self.lap += [font.render("LAP "+str(i),1,ORANGE)]
        for i in range(1201):
            self.laptime += [font.render("Lap time "+str(i//10)+"."+str(i%10),1,ORANGE)]

    def Draw(self,x,y,screen,acar,alap,alaptime):
        angle = self.angle
        if angle < 0 :
            angle = angle + 360
        angle = angle%360
        car=car_original.copy()
        car.set_colorkey(WHITE)
        car=pygame.transform.rotate(acar, -angle)
        rect=car.get_rect()
        rect.center=(self.xc,self.yc)
        screen.blit(car,rect)
        screen.blit(self.speedo[int(10*self.speed)],(500,650))
        screen.blit(self.lap[alap-1],(500,670))
        for i in range(1,alap):
            screen.blit(self.laptime[int((alaptime[i-1]*10))],(600,650+(i-1)*20))
        if alap>3:
            screen.blit(self.laptime[int((sum(alaptime)*10))],(600,650+4*20))
        pygame.draw.circle(screen, BLUE, (self.sonar_0_x,self.sonar_0_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_30_x,self.sonar_30_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_60_x,self.sonar_60_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_90_x,self.sonar_90_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_180_x,self.sonar_180_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_270_x,self.sonar_270_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_300_x,self.sonar_300_y), 5)
        pygame.draw.circle(screen, RED, (self.sonar_330_x,self.sonar_330_y), 5)
            
    def Update(self,onboard):
        if not onboard:
            self.speed=0
            self.sonar_0_x=self.x_front_i;self.sonar_0_y=self.y_front_i;self.sonar_0_distance=0
            self.sonar_30_x=self.x_front_i;self.sonar_30_y=self.y_front_i;self.sonar_30_distance=0
            self.sonar_60_x=self.x_front_i;self.sonar_60_y=self.y_front_i;self.sonar_60_distance=0
            self.sonar_90_x=self.x_front_i;self.sonar_90_y=self.y_front_i;self.sonar_90_distance=0
            self.sonar_180_x=self.x_front_i;self.sonar_180_y=self.y_front_i;self.sonar_180_distance=0
            self.sonar_270_x=self.x_front_i;self.sonar_270_y=self.y_front_i;self.sonar_270_distance=0
            self.sonar_300_x=self.x_front_i;self.sonar_300_y=self.y_front_i;self.sonar_300_distance=0
            self.sonar_330_x=self.x_front_i;self.sonar_330_y=self.y_front_i;self.sonar_330_distance=0

        else:
            self.sonar_0_x,self.sonar_0_y, self.sonar_0_distance = self.calculate_sonar(0)
            self.sonar_30_x,self.sonar_30_y, self.sonar_30_distance = self.calculate_sonar(30)
            self.sonar_60_x,self.sonar_60_y, self.sonar_60_distance = self.calculate_sonar(60)
            self.sonar_90_x,self.sonar_90_y, self.sonar_90_distance = self.calculate_sonar(90)
            self.sonar_180_x,self.sonar_180_y, self.sonar_180_distance = self.calculate_sonar(180)
            self.sonar_270_x,self.sonar_270_y, self.sonar_270_distance = self.calculate_sonar(270)
            self.sonar_300_x,self.sonar_300_y, self.sonar_300_distance = self.calculate_sonar(300)
            self.sonar_330_x,self.sonar_330_y, self.sonar_330_distance = self.calculate_sonar(330)

        langle = self.angle/57.296  #passage en radians
        vx = self.speed*math.sin(langle)
        vy = -self.speed*math.cos(langle)
        self.xf = self.xf + vx*self.dt
        self.yf = self.yf + vy*self.dt
        self.xc = int(self.xf)
        self.yc = int(self.yf)
        self.x_front = self.xf+20*math.sin(langle)
        self.y_front = self.yf-20*math.cos(langle)
        self.x_front_i = int(self.x_front)
        self.y_front_i = int(self.y_front)
        
        #print(self.sonar_0_distance)

    def brake(self):
        self.speed = 0.95*self.speed - 0.2
        if self.speed<0:
            self.speed=0
        #print(int(10.0*self.speed),'\t')

    def acelerate(self):
        self.speed = .95*self.speed + 0.05*10
        if self.speed>10:
            self.speed=10
        #print(int(10.0*self.speed),'\t')

    def calculate_sonar(self,sonar_angle):
        candidates=self.calculate_track_intersections_candidates(outside_line,sonar_angle)
        candidates+=self.calculate_track_intersections_candidates(inside_line,sonar_angle)

        sonar_x=0
        sonar_y=0
        sonar_distance=1000
        angletotal = (self.angle+sonar_angle)/57.296  #passage en radians
        
        for i in range(int(len(candidates)/2)):
            (sonar_temp_x, sonar_temp_y,_,_,_) = intersectLines(candidates[2*i+1], candidates[2*i], (self.x_front+1000*math.sin(angletotal),self.y_front-1000*math.cos(angletotal)), (self.x_front,self.y_front))
            sonar_distance_temp=math.sqrt(math.pow(sonar_temp_x-self.x_front,2)+math.pow(sonar_temp_y-self.y_front,2))
            if sonar_distance_temp<sonar_distance:
                sonar_distance=sonar_distance_temp
                sonar_x=int(sonar_temp_x)
                sonar_y=int(sonar_temp_y)

        return sonar_x,sonar_y,sonar_distance

    def calculate_track_intersections_candidates(self,atrack,sonar_angle):

        candidates=[]
        angletotal = (self.angle+sonar_angle)/57.296  #passage en radians
        
        P1=Point(self.x_front,self.y_front)
        P2=Point(self.x_front+1000*math.sin(angletotal),self.y_front-1000*math.cos(angletotal))
        old_pt=atrack[0]
        for idx,pt in enumerate(atrack):
            if idx!=0:
                P3=Point(old_pt[0],old_pt[1])
                P4=Point(pt[0],pt[1])
                if intersect(P1,P2,P3,P4):
                    candidates+=[old_pt,pt]
                old_pt=pt
        
        P3=Point(old_pt[0],old_pt[1])
        P4=Point(atrack[0][0],atrack[0][1])
        if intersect(P1,P2,P3,P4):
            candidates+=[old_pt,pt]

        return candidates

class Agent():
    def Load(self):
        pass

#Main
x = 800
y = 30

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" %(x,y)
import pygame
pygame.init()
from pygame.locals import *
from pygame.transform import *
import math
import pdb

running=True
clock = pygame.time.Clock()

CAR_WIDTH=20
CAR_LENGHT=40
ORANGE=(255,160,16)
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

screen_size = (1024,768)
screen = pygame.display.set_mode(screen_size)
screen.fill(WHITE)

outside_line=[(100,500),(100,400),(135,350),(50,250),(150,100),(400,90),
                (375,200),(600,150),(700,50),(900,50),(920,60),(950,100),(950,650),
                (925,675),(900,690),(875,690),(500,500),(300,630),(150,600)]

inside_line=[(200,500),(200,400),(220,350),(120,250),(220,150),(300,155),
                (320,275),(700,170),(750,120),(850,120),(870,140),(875,200),
                (875,600),(860,620),(500,400),(250,560),(220,550)]

def draw_board(self,ol,il):
    
    pygame.draw.lines(self,BLACK,True,ol,5)
    pygame.draw.lines(self,BLACK,True,il,5)
    pygame.draw.lines(self,RED,False,[(103,470),(197,470)],3)

def calculate_perimeter(liste):

    liste+=[liste[0]]

    perimeter=[(liste[0][0],liste[0][1])]
    
    for idx,pt in enumerate(liste):
        if idx!=0:
            dx=pt[0]-liste[idx-1][0]
            dy=pt[1]-liste[idx-1][1]
            if dx==0:
                count=abs(dy)
                if dy>0:
                    perimeter+=[(liste[idx-1][0],liste[idx-1][1]+i) for i in range(1,count)]
                elif dy<0:
                    perimeter+=[(liste[idx-1][0],liste[idx-1][1]-i) for i in range(1,count)]
            else:
                derivate=dy/dx
                origine=pt[1]-derivate*pt[0]
                count=abs(dx)
                if dx>0:
                    perimeter+=[(liste[idx-1][0]+i,int(derivate*(liste[idx-1][0]+i)+origine)) for i in range(1,count)]
                if dx<0:
                    perimeter+=[(liste[idx-1][0]-i,int(derivate*(liste[idx-1][0]-i)+origine)) for i in range(1,count)]
            perimeter+=[pt]

    return perimeter

def calculate_area_pixels(perimetre):

    track_pixels=[]
    track_pixels+=perimetre

    for ix in range(0,1000):
        x_list=[]
        for idx,ip in enumerate(perimetre):
            if ix==ip[0]:
                x_list+=[(ip[1],idx)]
        x_list.sort()
        x_list_len=len(x_list)
        
        if x_list_len%2 ==0:
            for idx_pair in range(int(x_list_len/2)):
                track_pixels+=[(ix,x_list[2*idx_pair][0]+i) for i in range(1,x_list[2*idx_pair+1][0]-x_list[2*idx_pair][0])]
        elif x_list_len%2 ==1 and x_list_len>1:
            #analize de chaque point
            corrected_list=[]
            #print(x_list)
            for idx_inpair in x_list:
                #print('per_ex[idx_inpair[1]-1][0]->',per_ex[idx_inpair[1]-1][0],'idx_inpair[0]->',idx_inpair[0])
                #print('per_ex[idx_inpair[1]+1][0]->',per_ex[idx_inpair[1]+1][0],'idx_inpair[0]->',idx_inpair[0])
                if not((perimetre[idx_inpair[1]-1][0]<ix and perimetre[idx_inpair[1]+1][0]<ix) or (perimetre[idx_inpair[1]-1][0]>ix and perimetre[idx_inpair[1]+1][0]>ix)):
                    corrected_list+=[idx_inpair]
                #print('*****',ix,idx_inpair,'/',per_ex[idx_inpair[1]-1],per_ex[idx_inpair[1]+1])
            
            xc_list_len=len(corrected_list)
            if xc_list_len%2 ==0:
                for idx_inpair in range(int(xc_list_len/2)):
                    track_pixels+=[(ix,corrected_list[2*idx_inpair][0]+i) for i in range(1,corrected_list[2*idx_inpair+1][0]-corrected_list[2*idx_inpair][0])]
    
    return track_pixels

def calculate_pixels_from_lines(aline):
    
    pixels=[]

    if aline[0][0]==aline[1][0]:
        pixels+=[(aline[0][0],aline[0][1]+i) for i in range(aline[1][1]-aline[0][1]+1)]
    if aline[0][1]==aline[1][1]:
        pixels+=[(aline[0][0]+i,aline[0][1]) for i in range(aline[1][0]-aline[0][0]+1)]
    return pixels

def init_game():
    
    racer.Load()
    #racer, angle=0, onboard=True, cp1=False, cp2=False, cp3=False, cp4=False, lap=1, laptime=[], total_time=[0], frame=0
    return (racer, 0, True, False, False, False, False, 1, [], [0], 0)

#track    
per_ex=calculate_perimeter(outside_line)
per_in=calculate_perimeter(inside_line)
len_ex=len(per_ex)
len_in=len(per_in)
big_area=calculate_area_pixels(per_ex)
small_area=calculate_area_pixels(per_in)
s = set(small_area)
track_area = [x for x in big_area if x not in s]

#checkpoints
chkpt1=[]
chkpt2=[]
chkpt3=[]
chkpt4=[]
for i in range(20):
    chkpt1+=calculate_pixels_from_lines([(500+i,150),(500+i,250)]) 
    chkpt2+=calculate_pixels_from_lines([(800,350+i),(1000,350+i)]) 
    chkpt3+=calculate_pixels_from_lines([(400-i,400),(400-i,630)]) 
    chkpt4+=calculate_pixels_from_lines([(103,470-i),(197,470-i)]) 

#car
racer = Sprite()
racer.Load()
xs = 150
ys = 500
car_original=pygame.Surface((CAR_WIDTH, CAR_LENGHT))
car_original.set_colorkey(WHITE)
car_original.fill(ORANGE)
angle=0
onboard=True

#agent
driver = Agent()
driver.Load()

#inits
cp1=False
cp2=False
cp3=False
cp4=False
lap=1
laptime=[]
total_time=[0]
frame=0

MAX_LAPS=3

selfdriving=True

#main loop
while running:
    
    screen.fill(WHITE)
    car_original.fill(ORANGE)
    draw_board(screen,outside_line,inside_line)
    clock.tick(24)
    frame+=1
    
    racer.Update(onboard)
    racer.Draw(xs,ys,screen,car_original,lap,laptime)
    
    #perimeter
    #for i in per_ex:
    #    pygame.draw.circle(screen, RED, i, 3)
    #for i in per_in:
    #    pygame.draw.circle(screen, RED, i, 3)
   
   #control lines
    #pygame.draw.lines(screen,BLUE,False,((500,150),(500,250)),1)
    #pygame.draw.lines(screen,BLUE,False,((800,350),(1000,350)),1)
    #pygame.draw.lines(screen,BLUE,False,((400,400),(400,630)),1)
    
    #front indicator
    pygame.draw.circle(screen, BLACK, (racer.x_front_i,racer.y_front_i), 2)

    #areas
    #for i in big_area:
    #    pygame.draw.circle(screen, BLACK, i, 1)

    #for i in small_area:
    #    pygame.draw.circle(screen, ORANGE, i, 1)

    #for i in track_area:
    #    pygame.draw.circle(screen, ORANGE, i, 1)

    #checkpoints
    if ((racer.x_front_i,racer.y_front_i) in chkpt1) and cp1==False:
        cp1=True
        cp4=False
    if ((racer.x_front_i,racer.y_front_i) in chkpt2) and cp1 and cp2==False:
        cp2=True
    if ((racer.x_front_i,racer.y_front_i) in chkpt3) and cp2 and cp3==False:
        cp3=True
    if ((racer.x_front_i,racer.y_front_i) in chkpt4) and cp3 and cp4==False:
        cp4=True
        lap+=1
        cp1=False
        cp2=False
        cp3=False
        total_time+=[frame/24]
        laptime+=[total_time[lap-1]-total_time[lap-2]]

    #collision
    if (racer.x_front_i,racer.y_front_i) not in track_area:
        onboard = False
        racer.speed=0
        car_original.fill(RED)
        racer.Draw(xs,ys,screen,car_original,lap,laptime)
    else:
        onboard=True

    key = pygame.key.get_pressed()
    
    #end race
    if lap > MAX_LAPS :
        racer.speed=0
        try:
            racer.angle+=5
        except:
            racer.angle=0
        if key[K_SPACE] :
            (racer, angle, onboard, cp1, cp2, cp3, cp4, lap, laptime, total_time, frame) = init_game()
        
        

    #display
    pygame.display.flip()

    #manual
    if not(selfdriving):
        if key[K_RIGHT] :
            racer.angle = (racer.angle+3)%360
        if key[K_LEFT]:
            racer.angle = (racer.angle+357)%360
        if key[K_q]:
                racer.acelerate()
        if key[K_a]:
                racer.brake()
    
    #agent
    elif selfdriving:
        #driver here
        racer.acelerate()
        racer.angle = (racer.angle+3)%360

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

