import pygame
import time
import random

display_width =820
display_height = 600
pygame.init()
screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Dodge It')
clock = pygame.time.Clock()

bump_width = 70
bump_height = 70
block_width = 120
block_height = 70
bump_zonel = display_width*0.30
bump_zoner = display_width*0.70
cone_img = pygame.image.load('cone.png')
cone_img = pygame.transform.scale(cone_img, (bump_width, bump_height))
money_img = pygame.image.load('money.png')
money_img = pygame.transform.scale(money_img, (bump_width, bump_height))
block_img = pygame.image.load('block.png')
block_img = pygame.transform.scale(block_img, (block_width, block_height))
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (bump_width, bump_height))
hole_img = pygame.image.load('manhole.png')
hole_img = pygame.transform.scale(hole_img, (bump_width, bump_height))


track_startx = display_width/2
track_diff = 100
track_width = 20
track_height = 60

left_width = display_width*0.175
left_height = display_height
left_x = 0
right_width = display_width*0.175
right_height = display_height
right_x = display_width*0.825

grass_img = pygame.image.load('grass.png')
grass_img = pygame.transform.scale(grass_img, (50, 50))

brick_width = 25
brick_height = display_height
brick_xl = left_width-brick_width
brick_xr = right_x



def car(car_width, car_height, x,y,h):
    car_img = pygame.image.load('racecar.png')
    car_img = pygame.transform.scale(car_img, (car_width+h, car_height+h))
    screen.blit(car_img, (x,y))


def display_score(score,color):
   #color = (40,152,40,100)
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf',25)
    text = "Score: "+str(score)
    msg = font.render(text,True,color)
    msg_rect = msg.get_rect()
    msg_rect.center = (55,40)
    screen.blit(msg,msg_rect)

    

def display_msg(text,sc):
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf',80)
    msg = font.render(text,True,(0,0,255))
    msg_rect = msg.get_rect()
    msg_rect.center = ((display_width/2),(display_height*0.25))
    screen.blit(msg,msg_rect)
    score_tex = "Your Score : " + str(sc)
    button(score_tex, 0.5, (205, 145, 158, 255),(50,50,50))
    button("Play Again", 0.7, (0,255,0),(50,50,50))
    pygame.display.update()
   
    
def button(text, loc, color1, color2):
    font = pygame.font.Font('freesansbold.ttf', 50) 
    text = font.render(text, True, color1, color2) 
    textRect = text.get_rect()  
    textRect.center = ((display_width/2),(display_height*loc))
    screen.blit(text, textRect)

def instr():
    color1 = (255,255,255)
    color2 = (9,11,158,74)
    text = "Press 'H'"
    font = pygame.font.Font('freesansbold.ttf', 25) 
    text = font.render(text, True, color1, color2) 
    textRect = text.get_rect()  
    textRect.center = ((display_width*0.92),(display_height*0.06))
    screen.blit(text, textRect)
    text = "for help"
    font = pygame.font.Font('freesansbold.ttf', 25) 
    text = font.render(text, True, color1, color2) 
    textRect = text.get_rect()  
    textRect.center = ((display_width*0.92),(display_height*0.1))
    screen.blit(text, textRect)

def instruction():
    color1 = (255,255,255)
    color2 = (0,0,0)
    text = "Use left and right arrow keys to move the car" 
    font = pygame.font.Font('freesansbold.ttf', 30) 
    text = font.render(text, True, color1, color2) 
    textRect = text.get_rect()  
    textRect.center = ((display_width/2),(display_height*0.4))
    screen.blit(text, textRect)
    text = "and space bar to jump" 
    font = pygame.font.Font('freesansbold.ttf', 30) 
    text = font.render(text, True, color1, color2) 
    textRect = text.get_rect()  
    textRect.center = ((display_width/2),(display_height*0.5))
    screen.blit(text, textRect)
    text = "To score points, collect coins and jump over manholes" 
    font = pygame.font.Font('freesansbold.ttf', 30) 
    text = font.render(text, True, color1, color2) 
    textRect = text.get_rect()  
    textRect.center = ((display_width/2),(display_height*0.6))
    screen.blit(text, textRect)
    button("PLAY", 0.7, (0,0,255),(0,255,0))


def play_again():
    x,y = pygame.mouse.get_pos()
    
    if(x>=280 and x<=540 and y>=395 and y<=442):
        main()
   

def bumps(bumpx, bumpy, bumpw, bumph, r):
    if r == 1:
        screen.blit(block_img, (bumpx,bumpy))
    elif r == 2:
        screen.blit(money_img, (bumpx,bumpy))
    elif r == 3:
        screen.blit(cone_img, (bumpx,bumpy))
    elif r == 4:
        screen.blit(bird_img, (bumpx,bumpy))
    elif r == 5:
        screen.blit(hole_img, (bumpx,bumpy))
    
        


def draw_track(y):
    for i in range(-1,6):
        pygame.draw.rect(screen, (255,255,255), [track_startx, y+ i*track_diff, track_width, track_height])

def draw_field():
    color = (40,152,40,100)
    pygame.draw.rect(screen, color, [left_x, 0, left_width, left_height])
    pygame.draw.rect(screen, color, [right_x, 0, right_width, right_height])

def draw_brick(x):
    yellow = (241,240,9,100)
    black = (20,20,2,100)
    brown = (113,40,4,89)
    pygame.draw.rect(screen, brown, [x,0, brick_width, brick_height])

def draw_grass():
    for i in range(6):
        grass_x_left = random.randrange(0, int(brick_xl)-50)
        grass_x_right = random.randrange(int(brick_xr + brick_width+10), display_width-55)
        grass_y_left = random.randrange(0, display_height)
        grass_y_right = random.randrange(0, display_height)
        screen.blit(grass_img, (grass_x_left ,grass_y_left))
        screen.blit(grass_img, (grass_x_right ,grass_y_right))


def main():
    startx = display_width*0.47
    starty = display_height*0.8
    car_vel = 0
    d = False
    score = 0

    h = 0
    jump = False
    car_width = 70
    car_height = 110

    track_starty = 0
    track_speed = 20
    

    bump_startx = random.randrange(bump_zonel, bump_zoner)
    bump_starty = -100
    bump_speed = 30

    g = 0 #help window
    
    r = random.randrange(1,6)

    gameOver = False
    while not gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_vel= -30
                if event.key == pygame.K_RIGHT:
                    car_vel = 30
                if event.key == pygame.K_SPACE:
                        jump = True
                if event.key == pygame.K_h:
                        gameOver = True
                        g = 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_SPACE:
                    car_vel = 0

        #jumping
        if jump:
            h += 2
            if h >= 20:
                jump = False
    
        elif h > 0 and jump == False:
            h -= 2
        
        startx += car_vel
        bump_starty += bump_speed
        track_starty += track_speed
        track_starty = track_starty % track_diff
        
        screen.fill((111,111,122,70))

        draw_field()
        draw_grass()
        instr()
        draw_brick(brick_xl)
        draw_brick(brick_xr)
        draw_track(track_starty)
        bumps(bump_startx,bump_starty,bump_width,bump_height,r)
        car(car_width, car_height, startx,starty,h)

       
        #boundary check
        if((startx > right_x - car_width) or (startx<left_width)):
            gameOver = True
            g = 0
        
        
        #collision check
        if starty < bump_starty+bump_height:
            flag = False
            if startx > bump_startx and startx < bump_startx + bump_width or startx+car_width > bump_startx and startx + car_width < bump_startx+bump_width:
                if r==2 or (r==5 and h!=0):
                    flag = True
                else:
                    gameOver = True
                    g = 0
        
        #bumper fall
        if(bump_starty>display_height):
            bump_starty = 0
            bump_startx = random.randrange(bump_zonel, bump_zoner)
            r = random.randrange(1,6)
            if flag == True:
                score = score + 1
            bump_speed += 1.5
            
    
        display_score(score,(0,0,0))
                
        pygame.display.update()
        clock.tick(60)
    
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.MOUSEBUTTONUP:
                d = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                d = True
            if(d):
                play_again()
        bump_speed = 0
        
        display_score(score,(40,152,40,100))

        if g==0:
            display_msg("You crashed.",score)
        if g==1:
            instruction()
        
        

        pygame.display.update()
        clock.tick(60)

        
main()
pygame.quit()
quit()
