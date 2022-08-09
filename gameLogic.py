import pygame as pg
import os               # will be used to get the images
import target
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
TARGET_SIDE_SIZE = 30 #square
MOVING_SPEED = 5
BULLET_SPEED = 10
MAGAZINE_SIZE = 31
LABEL_LIMIT = 35


window = pg.display.set_mode((WIDTH, HEIGHT))
font = pg.font.Font('freesansbold.ttf', 32)


soldierImage = pg.image.load(os.path.join("images", "soldier.png"))
soldierImage = pg.transform.scale(soldierImage, (SOLDIER_WIDTH, SOLDIER_HEIGHT))
# rotatedSoldierImage = pg.transform.flip(soldierImage, False, True)

blackTargetImage = pg.image.load(os.path.join("images", "blacktarget.png"))
blackTargetImage = pg.transform.scale(blackTargetImage, (TARGET_SIDE_SIZE, TARGET_SIDE_SIZE))
greenTargetImage = pg.image.load(os.path.join("images", "greentarget.png"))
greenTargetImage = pg.transform.scale(greenTargetImage, (TARGET_SIDE_SIZE + 10, TARGET_SIDE_SIZE + 10))
specialTargetImage = pg.image.load(os.path.join("images", "specialtarget.png"))
specialTargetImage = pg.transform.scale(specialTargetImage, (TARGET_SIDE_SIZE + 30, TARGET_SIDE_SIZE + 30))


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
    global MAGAZINE_SIZE
    nbBullets = 31
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_SPACE and len(bullets) < nbBullets:
            bullet = pg.Rect(soldier.x + SOLDIER_WIDTH, soldier.y + 10, 10, 5)
            bullets.append(bullet)            
            MAGAZINE_SIZE -= 1
            text = font.render("Number of bullets: " + str(MAGAZINE_SIZE), 1, BLACK) # render everytime a bullet is generated
            

def shoot(bullets):
    for bullet in bullets:
        bullet.x += BULLET_SPEED

# def checkCollision(bullets)        

def createWindow(color, soldierRect, black, green, special, playersBullets): #this function takes care of everythin thing that appears in the display when the game starts
    pg.display.set_caption("Shoot the targets !")
    window.fill(color)

    window.blit(soldierImage, (soldierRect.x, soldierRect.y)) # will superpose the image into the rectangle, since we control the rectangle to move the image
    window.blit(blackTargetImage, (black.rect.x, black.rect.y))
    window.blit(greenTargetImage, (green.rect.x, green.rect.y))
    window.blit(specialTargetImage, (special.rect.x, special.rect.y))

    text = font.render("Number of bullets: " + str(MAGAZINE_SIZE), 1, BLACK) # text appears a first time at the beginning of the game, showcasing the amount of bullets
    window.blit(text, (10, 10))

    for bullet in playersBullets:    
        pg.draw.rect(window, BLACK, bullet) 
        

    pg.display.update()



def main():
    clock = pg.time.Clock()
    gameIsRunning = True
    
    soldier = pg.Rect(WIDTH//2, HEIGHT//3, SOLDIER_WIDTH, SOLDIER_HEIGHT)  # create rectangle to which the createWindow() will superpose an image
    blackTarget = target.BlackTarget(1)
    greenTarget = target.GreenTarget(2)
    specialTarget = target.SpecialTarget(3)

    soldierBullets = []

    while(gameIsRunning):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameIsRunning = False

            generateBullets(event, soldier, soldierBullets)
        
                

        pressedKeys = pg.key.get_pressed()  #during entire game time, append all key pressed into a list, which is taken as parameter in the method moveSoldier()
        moveSoldier(pressedKeys, soldier)
        shoot(soldierBullets)
        createWindow(WHITE, soldier, blackTarget, greenTarget, specialTarget, soldierBullets)


if __name__ == "__main__":
    main()