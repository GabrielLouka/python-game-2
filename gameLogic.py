import pygame as pg
import os               # will be used to get the images

# this file will contain the main loop, where the game will be running
# creating the window : createWindow() uses parameters windth height and color to create the display
# importing the image and represent it as a rectangle to use it

WIDTH, HEIGHT = 900, 600
WHITE = (255, 255, 255)
window = pg.display.set_mode((WIDTH, HEIGHT))

soldierImage = pg.image.load(os.path.join("images", "soldier.png"))
targetImage = pg.image.load(os.path.join("images", "target.png"))




def createWindow(color):
    pg.display.set_caption("Shoot the targets !")
    window.fill(color)

    

    pg.display.update()


def main():
    gameIsRunning = True
    while(gameIsRunning):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameIsRunning = False
                

        createWindow(WHITE)


if __name__ == "__main__":
    main()