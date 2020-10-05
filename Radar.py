import sys
import pygame
from math import sqrt, atan

class Radar:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("The Straight Line")
        self.font = pygame.font.SysFont("Helvetica", 25)
        self.font1 = pygame.font.SysFont("Calibri", 19)
        self.font3 = pygame.font.SysFont('Arial', 40)
        clicked = False
        self.draw()

    def draw(self):
        global WHITE, BLUE, GREEN, RED, BLACK
        WHITE = (255, 255, 255)
        GREEN = (20, 255, 20)
        GREEN_ = (0, 255, 0)
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        BLACK = (0, 0, 0)
        x = 0
        y = 0
        X = 7  
        for i in range(4):
            pygame.draw.rect(self.screen, WHITE, (X, 607, 90, 50))
            X += 113
        self.screen.blit(self.font.render('Gradient', True, BLACK), (10, 610))        
        self.screen.blit(self.font.render('Distance', True, BLACK), (130, 610))
        self.screen.blit(self.font.render('Refresh', True, BLACK), (245, 610))
        self.screen.blit(self.font.render('Midpoint', True, BLACK), (350, 610))
        
        for i in range(60):
            pygame.draw.rect(self.screen, GREEN, (x, 0, 2, 600))
            x+=20

        for i in range(30):
            pygame.draw.rect(self.screen, GREEN, (0, y, 1000, 2))
            y+=20
        x1 = 0
        y1 = 0
        for i in range(30):
            pygame.draw.rect(self.screen, GREEN_, (x1, 0, 4, 600))
            x1+=40
        for i in range(16):
            pygame.draw.rect(self.screen, GREEN_, (0, y1, 1000, 4))
            y1+=40

    def point(self, coord_list, zero):
        try:
            pygame.draw.circle(self.screen, BLUE, coord_list[zero], 5)
            zero += 1
            if len(coord_list) > zero:
                geo.point(coord_list, zero)
        except IndexError: pass
            
    def run(self):
        clicked = False
        mouse_coords = []
        while True:
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.screen.fill(BLACK)
                self.draw()
                
                if event.type == pygame.MOUSEBUTTONUP and pos[1]<600:
                    pos = pygame.mouse.get_pos()
                    mouse_coords.append(pos)
                    clicked = True
                if clicked == True:
                    geo.point(mouse_coords, 0)
                    
                if event.type == pygame.MOUSEMOTION:
                    if pos[0] > 340 and pos[0] < 430:
                        if pos[1] > 607 and pos[1] < 660:
                            pygame.draw.rect(self.screen, BLUE, (346, 607, 90, 50))
                            self.screen.blit(self.font.render('Midpoint', True, WHITE), (350, 610))
                            self.screen.blit(self.font1.render('find the midpoint of the first two points', True, RED), (385, 597))
                    if pos[0] > 240 and pos[0]<330:
                        if pos[1] >607 and pos[1] <660:
                            pygame.draw.rect(self.screen, BLUE, (233, 607, 90, 50))
                            self.screen.blit(self.font.render('Refresh', True, WHITE), (245, 610))
                            self.screen.blit(self.font1.render('refresh the grid page', True, RED), (285, 597))
                    else:
                        pygame.draw.rect(self.screen, WHITE, (233, 607, 90, 50))
                        self.screen.blit(self.font.render('Refresh', True, BLACK), (245, 610))
                        
                    if pos[0] > 120 and pos[0] < 210:
                        if pos[1] > 607 and pos[1] < 660:
                            pygame.draw.rect(self.screen, BLUE, (120, 607, 90, 50))
                            self.screen.blit(self.font.render('Distance', True, WHITE), (130, 610))
                            self.screen.blit(self.font1.render('find the distance between the last 2 points', True, RED), (227, 597))
                    else:
                        pygame.draw.rect(self.screen, WHITE, (120, 607, 90, 50))
                        self.screen.blit(self.font.render('Distance', True, BLACK), (130, 610))

                    if pos[0] > 7 and pos[0] < 77:
                        if pos[1] > 607 and pos[1] < 657:
                            pygame.draw.rect(self.screen, BLUE, (7, 607, 90, 50)) 
                            self.screen.blit(self.font.render('Gradient', True, WHITE), (10, 610))
                            self.screen.blit(self.font1.render('find the gradient of the first 2 points', True, RED), (77, 597))
                    else:
                        pygame.draw.rect(self.screen, WHITE, (7, 607, 70, 50))
                        self.screen.blit(self.font.render('Gradient', True, BLACK), (10, 610))

                if event.type == pygame.MOUSEBUTTONUP:
                    prev_pos = None
                    if pos[0] > 120 and pos[0] < 210:
                        if pos[1] > 607 and pos[1] < 660:
                            try:
                                prev_pos = [mouse_coords[-1], mouse_coords[-2]]
                            except IndexError: pass
                            
                            if prev_pos != None:
                                pygame.draw.line(self.screen, WHITE, prev_pos[0], prev_pos[1]) #draw line connecting the last 2 points
                                X1 = mouse_coords[0][0]
                                X2 = mouse_coords[1][0]
                                Y1 = mouse_coords[0][1]
                                Y2 = mouse_coords[1][1]
                                dist = sqrt((X2-X1)**2+(Y2 - Y1)**2)
                                distance = round(dist, 1)
                                self.screen.blit(self.font.render("Distance = " + str(distance), True, WHITE), (830, 640))
                            #sleep(5)

                    if pos[0] > 240 and pos[0]<330:
                        if pos[1] >607 and pos[1] <660:
                            mouse_coords = []
                            
                    if pos[0] > 340 and pos[0] < 430:
                        if pos[1] > 607 and pos[1] < 660:
                            try:
                                X1 = mouse_coords[0][0]
                                X2 = mouse_coords[1][0]
                                Y1 = mouse_coords[0][1]
                                Y2 = mouse_coords[1][1]
                                midpointX = (X1 + X2)//2
                                midpointY = (Y1+Y2)//2
                                midpoint = X1 + X2//2, Y1 + Y2//2
                                self.screen.blit(self.font3.render("X", True, RED), (midpointX, midpointY))
                                self.screen.blit(self.font.render('MIDPOINT = ' + str(midpoint), True, WHITE), (790, 640))
                            except: pass

                    if pos[0] > 7 and pos[0] < 77:
                        if pos[1] > 610 and pos[1] < 657:
                            try:
                                X1 = mouse_coords[0][0]
                                X2 = mouse_coords[1][0]
                                Y1 = mouse_coords[0][1]
                                Y2 = mouse_coords[1][1]
                            except IndexError: pass
                            try:
                                _gradient = (Y2-X2)//(Y1-X1)
                                gradient_ = atan(_gradient)
                                gradient = round(gradient_, 1)
                                self.screen.blit(self.font.render(f"Gradient = {gradient}", True, WHITE), (790, 640))
                            except UnboundLocalError: pass
                            
                self.screen.blit(self.font.render(f'X: {pos[0]}  Y: {pos[1]}', True, WHITE), (850, 610))
                pygame.display.flip()  
            pygame.display.update()

if __name__=='__main__':
    geo = Radar()
    geo.run()
