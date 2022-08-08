from asyncio import FastChildWatcher
import pygame as pg
import os               # will be used to get the images

# this file will contain the main loop, where the game will be running
# creating the window : createWindow() uses parameters windth height and color to create the display
# importing the image and represent it as a rectangle to use it

FPS = 60
WIDTH, HEIGHT = 1100, 800
WHITE = (255, 255, 255)
SOLDIER_SIZE = (70, 90)
MOVING_SPEED = 20

window = pg.display.set_mode((WIDTH, HEIGHT))

soldierImage = pg.image.load(os.path.join("images", "soldier.png"))
soldierImage = pg.transform.scale(soldierImage, SOLDIER_SIZE)
rotatedSoldierImage = pg.transform.flip(soldierImage, False, True)


targetImage = pg.image.load(os.path.join("images", "target.png"))


def moveSoldier(event, soldier):
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_w:
            soldier.y -= MOVING_SPEED
        if event.key == pg.K_s:
            soldier.y += MOVING_SPEED
        if event.key == pg.K_d:
            soldier.x += MOVING_SPEED
        if event.key == pg.K_a:
            
            soldier.x -= MOVING_SPEED
            



def createWindow(color, soldierRect):
    pg.display.set_caption("Shoot the targets !")
    window.fill(color)

    window.blit(soldierImage, (soldierRect.x, soldierRect.y)) # will superpose the image into the rectangle, since we control the rectangle to move the image
    

    pg.display.update()


def main():
    clock = pg.time.Clock()
    gameIsRunning = True
    
    soldier = pg.Rect(WIDTH//2, HEIGHT//3, 30, 60)  # create rectangle to which the createWindow() will superpose an image

    while(gameIsRunning):
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameIsRunning = False

            moveSoldier(event, soldier)

                

        
        createWindow(WHITE, soldier)


if __name__ == "__main__":
    main()