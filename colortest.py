
import pygame
from pygamehelper import *

class Color:
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	RED = (255,0,0)
	BLUE = (0,255,0)
	GREEN = (0,0,255)
	
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

#main control loop of the pygame
class ColorSim( PygameHelper ):

    #put one circle in the middle of the screen
    starting_x = (DISPLAY_WIDTH * 0.5)
    starting_y = (DISPLAY_HEIGHT * 0.5)
    starting_size = 30
    color_index = 0
    color = Color.RED
    color_inc = 10
         
    def __init__(Self):
        super(ColorSim,Self).__init__( (DISPLAY_WIDTH, DISPLAY_HEIGHT), Color.WHITE )

        Self.color = ColorSim.color
        Self.color_index = ColorSim.color_index
        Self.x = ColorSim.starting_x
        Self.y = ColorSim.starting_y
        Self.size = ColorSim.starting_size
             
    def update(Self):
        pass

    def draw( Self ):
        #print('drawing:', Self.color, Self.x, Self.y, Self.size)
        Self.screen.fill(Color.WHITE)
        pygame.draw.circle(Self.screen, Self.color, (int(Self.x), int(Self.y)), Self.size, 0) 
        pygame.display.update()
	
    def keyDown(Self, key):
            
        if key == K_SPACE:
            pass
        elif key == K_LEFT:
            pass
        elif key == K_RIGHT:
              pass
        elif key == K_UP:
            R,G,B = Self.color
            
            R += ColorSim.color_inc
            if R > 255: R = 255

            Self.color = R,G,B
            print(Self.color, Self.x, Self.y, Self.size)

            
        elif key == K_DOWN:
            R,G,B = Self.color
            
            R -= ColorSim.color_inc
            if R < 0: R = 0

            Self.color = R,G,B
            print(Self.color, Self.x, Self.y, Self.size)
        else:
                print(key)

if __name__ == "__main__":
        g = ColorSim()
        g.mainLoop(60)
        pygame.quit()

