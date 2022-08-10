from tabnanny import check
import pygame as pg
import os               # will be used to get the images
import target
import random

pg.font.init()
# this file will contain the main loop, where the game will be running
# creating the window : createWindow() uses parameters windth height and color to create the display
# importing the image and represent it as a rectangle to use it

FPS = 60
WIDTH, HEIGHT = 1100, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SOLDIER_WIDTH = 70
SOLDIER_HEIGHT = 90
TARGET_SIDE_SIZE_SMALL = 30 
TARGET_SIDE_SIZE_MEDIUM = 50
TARGET_SIDE_SIZE_LARGE = 70
MOVING_SPEED = 5
BULLET_SPEED = 20
MAGAZINE_SIZE = 31
LABEL_LIMIT = 35


window = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.Font('freesansbold.ttf', 32)


soldierImage = pg.image.load(os.path.join("images", "soldier.png"))
soldierImage = pg.transform.scale(soldierImage, (SOLDIER_WIDTH, SOLDIER_HEIGHT))


blackTargetImage = pg.image.load(os.path.join("images", "blacktarget.png"))
blackTargetImage = pg.transform.scale(blackTargetImage, (TARGET_SIDE_SIZE_SMALL, TARGET_SIDE_SIZE_SMALL))
greenTargetImage = pg.image.load(os.path.join("images", "greentarget.png"))
greenTargetImage = pg.transform.scale(greenTargetImage, (TARGET_SIDE_SIZE_MEDIUM + 10, TARGET_SIDE_SIZE_MEDIUM + 10))
specialTargetImage = pg.image.load(os.path.join("images", "specialtarget.png"))
specialTargetImage = pg.transform.scale(specialTargetImage, (TARGET_SIDE_SIZE_LARGE + 30, TARGET_SIDE_SIZE_LARGE + 30))


def moveSoldier(events : list, soldier):
    if events[pg.K_w] and soldier.y - MOVING_SPEED > LABEL_LIMIT:  ## add collisions with target to avoir going through targets
        soldier.y -= MOVING_SPEED
    if events[pg.K_s] and soldier.y + MOVING_SPEED + SOLDIER_HEIGHT < HEIGHT:
        soldier.y += MOVING_SPEED
    if events[pg.K_d] and soldier.x + MOVING_SPEED + SOLDIER_WIDTH < WIDTH:
        soldier.x += MOVING_SPEED
    if events[pg.K_a] and soldier.x - MOVING_SPEED > 0:        
        soldier.x -= MOVING_SPEED
            
def generateBullets(event, soldier, bullets: list):    
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE and len(bullets) < MAGAZINE_SIZE:
            bullet = pg.Rect(soldier.x + SOLDIER_WIDTH, soldier.y + 10, 10, 5)
            bullets.append(bullet)            
            
def shoot(bullets):
    for bullet in bullets:
        bullet.x += BULLET_SPEED

def checkCollision(bullets, targets):
    for bullet in bullets:
        for singleTarget in targets:
            if bullet.colliderect(singleTarget):
                bullets.remove(bullet)
                whiteSquare = pg.image.load(os.path.join("images", "whitesquare.png")) 
                if isinstance(singleTarget, target.BlackTarget):
                    whiteSquare = pg.transform.scale(whiteSquare, (TARGET_SIDE_SIZE_SMALL, TARGET_SIDE_SIZE_SMALL))
                    window.blit(whiteSquare, (singleTarget.x, singleTarget.y))
                if isinstance(singleTarget, target.GreenTarget):
                    singleTarget.life -= 1
                    if singleTarget.life == 0:
                        whiteSquare = pg.transform.scale(whiteSquare, (TARGET_SIDE_SIZE_MEDIUM, TARGET_SIDE_SIZE_MEDIUM))
                        window.blit(whiteSquare, (singleTarget.x, singleTarget.y))
                if isinstance(singleTarget, target.SpecialTarget):
                    singleTarget.life -= 1
                    if singleTarget.life == 0:
                        whiteSquare = pg.transform.scale(whiteSquare, (TARGET_SIDE_SIZE_LARGE, TARGET_SIDE_SIZE_LARGE))
                        window.blit(whiteSquare, (singleTarget.x, singleTarget.y))

    

def createWindow(color, soldierRect, targets, playersBullets): #this function takes care of everythin thing that appears in the display when the game starts
    pg.display.set_caption("Shoot the targets !")
    window.fill(color)

    window.blit(soldierImage, (soldierRect.x, soldierRect.y)) # will superpose the image into the rectangle, since we control the rectangle to move the image
    
    for singleTarget in targets:
        if isinstance(singleTarget, target.BlackTarget):
            window.blit(blackTargetImage, (singleTarget.rect.x, singleTarget.rect.y))
        if isinstance(singleTarget, target.GreenTarget):
            window.blit(greenTargetImage, (singleTarget.rect.x, singleTarget.rect.y))
        if isinstance(singleTarget, target.SpecialTarget):
            window.blit(specialTargetImage, (singleTarget.rect.x, singleTarget.rect.y))    

    for bullet in playersBullets:    
        pg.draw.rect(window, BLACK, bullet) 

    checkCollision(playersBullets, targets)
        
    pg.display.update()

def generateSoldier():
    return pg.Rect(WIDTH//2, HEIGHT//3, SOLDIER_WIDTH, SOLDIER_HEIGHT)

def generateTargets(soldier) -> list:
    generated = []
    for i in range(3):
        black = target.BlackTarget(1, random.randint(2*SOLDIER_HEIGHT, WIDTH-SOLDIER_HEIGHT), random.randint(SOLDIER_HEIGHT , HEIGHT-SOLDIER_HEIGHT))
        green = target.GreenTarget(2, random.randint(2*SOLDIER_HEIGHT, WIDTH-SOLDIER_HEIGHT), random.randint(SOLDIER_HEIGHT, HEIGHT-SOLDIER_HEIGHT))
        special = target.SpecialTarget(3, random.randint(2*SOLDIER_HEIGHT, WIDTH-SOLDIER_HEIGHT), random.randint(SOLDIER_HEIGHT, HEIGHT-SOLDIER_HEIGHT))
        if not black.rect.colliderect(green) and not black.rect.colliderect(special) and not green.rect.colliderect(special):
            generated.append(black)
            generated.append(green)
            generated.append(special) 

    return generated

def main():
    clock = pg.time.Clock()
    gameIsRunning = True
    
    soldier = generateSoldier()  # create rectangle to which the createWindow() will superpose an image    
    soldierBullets = []
    allTargets = generateTargets(soldier)

    while(gameIsRunning):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameIsRunning = False
            generateBullets(event, soldier, soldierBullets)
                    
        pressedKeys = pg.key.get_pressed()  #during entire game time, append all key pressed into a list, which is taken as parameter in the method moveSoldier()
        moveSoldier(pressedKeys, soldier)
        shoot(soldierBullets)
        # checkCollision(soldierBullets, allTargets)
        createWindow(WHITE, soldier, allTargets, soldierBullets)


if __name__ == "__main__":
    main()