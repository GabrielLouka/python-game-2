from tabnanny import check
import pygame as pg
import os              
import target
import random

pg.font.init()

WIDTH, HEIGHT = 1700, 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SOLDIER_WIDTH = 70
SOLDIER_HEIGHT = 90
TARGET_SIDE_SIZE_SMALL = 30 
TARGET_SIDE_SIZE_MEDIUM = 50
TARGET_SIDE_SIZE_LARGE = 70

FPS = 60
MOVING_SPEED = 7
BULLET_SPEED = 15
MAGAZINE_SIZE = 18
LABEL_LIMIT = 35

BLACK_HIT = pg.USEREVENT + 1    #custom events
GREEN_HIT = pg.USEREVENT + 2
SPECIAL_HIT = pg.USEREVENT + 3
TARGET_HIT = pg.USEREVENT + 4
BULLET_SHOT = pg.USEREVENT + 5


window = pg.display.set_mode((WIDTH, HEIGHT))

whiteSquare = pg.image.load(os.path.join("images", "whitesquare.png"))
soldierImage = pg.image.load(os.path.join("images", "soldier.png"))
soldierImage = pg.transform.scale(soldierImage, (SOLDIER_WIDTH, SOLDIER_HEIGHT))


blackTargetImage = pg.image.load(os.path.join("images", "blacktarget.png"))
blackTargetImage = pg.transform.scale(blackTargetImage, (TARGET_SIDE_SIZE_SMALL, TARGET_SIDE_SIZE_SMALL))
greenTargetImage = pg.image.load(os.path.join("images", "greentarget.png"))
greenTargetImage = pg.transform.scale(greenTargetImage, (TARGET_SIDE_SIZE_MEDIUM + 10, TARGET_SIDE_SIZE_MEDIUM + 10))
specialTargetImage = pg.image.load(os.path.join("images", "specialtarget.png"))
specialTargetImage = pg.transform.scale(specialTargetImage, (TARGET_SIDE_SIZE_LARGE + 30, TARGET_SIDE_SIZE_LARGE + 30))


def moveSoldier(events : list, soldier):
    if events[pg.K_w] and soldier.y - MOVING_SPEED > LABEL_LIMIT:
        soldier.y -= MOVING_SPEED
    if events[pg.K_s] and soldier.y + MOVING_SPEED + SOLDIER_HEIGHT < HEIGHT:
        soldier.y += MOVING_SPEED
    if events[pg.K_d] and soldier.x + MOVING_SPEED + SOLDIER_WIDTH < WIDTH:
        soldier.x += MOVING_SPEED
    if events[pg.K_a] and soldier.x - MOVING_SPEED > 0:        
        soldier.x -= MOVING_SPEED
            

def generateBullets(event, soldier, bullets: list):    
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE and len(bullets) < int(MAGAZINE_SIZE):            
            pg.event.post(pg.event.Event(BULLET_SHOT))
            bullet = pg.Rect(soldier.x + SOLDIER_WIDTH, soldier.y + 10, 10, 5)
            bullets.append(bullet)                        
            

def shootAndChekCollisions(bullets, targets, imageToInsert):
    for bullet in bullets:
        bullet.x += BULLET_SPEED        
        for singleTarget in targets:
            if bullet.colliderect(singleTarget): 
                bullets.remove(bullet)                                      
                if isinstance(singleTarget, target.BlackTarget):  
                    singleTarget.life -= 1
                    if singleTarget.life == 0:                        
                        pg.event.post(pg.event.Event(BLACK_HIT))
                        imageToInsert = pg.transform.scale(imageToInsert, (TARGET_SIDE_SIZE_SMALL, TARGET_SIDE_SIZE_SMALL))                       
                        window.blit(imageToInsert, (singleTarget.x, singleTarget.y))                        
                if isinstance(singleTarget, target.GreenTarget):
                    singleTarget.life -= 1
                    if singleTarget.life == 0:
                        pg.event.post(pg.event.Event(GREEN_HIT))          
                        imageToInsert = pg.transform.scale(imageToInsert, (TARGET_SIDE_SIZE_MEDIUM, TARGET_SIDE_SIZE_MEDIUM))
                        window.blit(imageToInsert, (singleTarget.x, singleTarget.y))
                if isinstance(singleTarget, target.SpecialTarget):
                    singleTarget.life -= 1
                    if singleTarget.life == 0:                        
                        pg.event.post(pg.event.Event(SPECIAL_HIT))                                                                     
                        imageToInsert = pg.transform.scale(imageToInsert, (TARGET_SIDE_SIZE_LARGE, TARGET_SIDE_SIZE_LARGE))
                        window.blit(imageToInsert, (singleTarget.x, singleTarget.y))     
    pg.display.update()
         


def createWindow(color, soldierRect, targets, playersBullets, score, numberBullets):
    pg.display.set_caption("Shoot the targets !")
    font = pg.font.SysFont("monospace", 22)
    window.fill(color)

    window.blit(soldierImage, (soldierRect.x, soldierRect.y))
    
    for singleTarget in targets:
        if isinstance(singleTarget, target.BlackTarget):
            window.blit(blackTargetImage, (singleTarget.rect.x, singleTarget.rect.y))
        if isinstance(singleTarget, target.GreenTarget):
            window.blit(greenTargetImage, (singleTarget.rect.x, singleTarget.rect.y))
        if isinstance(singleTarget, target.SpecialTarget):
            window.blit(specialTargetImage, (singleTarget.rect.x, singleTarget.rect.y))    

    for bullet in playersBullets:    
        pg.draw.rect(window, BLACK, bullet) 


    scoreText = font.render(f"Score : {score}", 1, BLACK)
    bulletsText = font.render(f"Number of bullets : {numberBullets}", 1, BLACK)
    window.blit(scoreText, (10, 10))
    window.blit(bulletsText, (WIDTH - 300, 10))    
        
    pg.display.update()


def generateSoldier():
    return pg.Rect(WIDTH//2, HEIGHT//3, SOLDIER_WIDTH, SOLDIER_HEIGHT)


def generateTargets() -> list:
    generated = []
    for i in range(random.randint(1, 4)):
        black = target.BlackTarget(1, random.randint(2*SOLDIER_HEIGHT, WIDTH-SOLDIER_HEIGHT), random.randint(SOLDIER_HEIGHT , HEIGHT-SOLDIER_HEIGHT))
        green = target.GreenTarget(2, random.randint(2*SOLDIER_HEIGHT, WIDTH-SOLDIER_HEIGHT), random.randint(SOLDIER_HEIGHT, HEIGHT-SOLDIER_HEIGHT))
        special = target.SpecialTarget(3, random.randint(2*SOLDIER_HEIGHT, WIDTH-SOLDIER_HEIGHT), random.randint(SOLDIER_HEIGHT, HEIGHT-SOLDIER_HEIGHT))
        if not black.rect.colliderect(green.rect) and not black.rect.colliderect(special.rect) and not green.rect.colliderect(special.rect):
            generated.append(black)
            generated.append(green)
            generated.append(special) 
    
    return generated


def main():
    clock = pg.time.Clock()
    gameIsRunning = True
    soldier = generateSoldier()   
    soldierBullets = []

    allTargets = generateTargets()
    score = 0
    numberBullets = MAGAZINE_SIZE

    while(gameIsRunning):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameIsRunning = False
            generateBullets(event, soldier, soldierBullets)

            if event.type == BLACK_HIT:
                score += 1
            if event.type == GREEN_HIT:
                score += 2
            if event.type == SPECIAL_HIT:
                score += 3            

            if event.type == BULLET_SHOT:
                numberBullets -= 1
                                                     
        pressedKeys = pg.key.get_pressed()
        moveSoldier(pressedKeys, soldier)
        shootAndChekCollisions(soldierBullets, allTargets, whiteSquare)
        createWindow(WHITE, soldier, allTargets, soldierBullets, score, numberBullets)


if __name__ == "__main__":
    main()