import pygame as pg

# organisation : import image from image file and create an object with it -> Pygame rectangle to represent it for the soldier and circle for the target
# either create two small classes : Soldier and Target and make them inherit from pg.Rect()
# one button to generate 10 random targets =>
# when all targets are taken down, annouce that the game is over and allow to click the regenerate button
#
#
# **Moves logic : reflect the soldier's image depending on input (in this case : A and D/Left and Right arrows)
#
#
# THIS FILE WILL CONTAIN THE GENERAL LOGIC OF THE GAME AND ALL IMPORTS FROM MODULES AND PACKAGES

WINDOW_WINDTH, WINDOW_HEIGHT = 1000, 800
GAME_WINDOW = pg.display.set_mode((WINDOW_WINDTH, WINDOW_HEIGHT))
WHITE = (0, 0, 0) 

pg.display.set_caption("Shoot the targets !")

def main():
    gameRunning = True
    while(gameRunning):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameRunning = False
                pg.quit()
        
        GAME_WINDOW.fill(WHITE)


if __name__ == "__main__":
    main() 


