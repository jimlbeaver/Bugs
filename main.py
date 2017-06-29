import pygame 
import os 
os.environ['SDL_VIDEO_CENTERED'] = '1'

from pygame.locals import *

BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0,255,0)
GREEN = pygame.Color(0,0,255)
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400

#Helper class that controls interaction loop in Pygame
from pygamehelper import *

#Use the pygame version of the bug so can display in pygame
from Bug import PGBug

#main control loop of the pygame
class BugSim( PygameHelper ):

	#put one bug in the middle of the screen
	starting_x = (DISPLAY_WIDTH * 0.5)
	starting_y = (DISPLAY_HEIGHT * 0.5)
	starting_theta = 0
	
	def __init__(Self):
		super(BugSim,Self).__init__( (DISPLAY_WIDTH, DISPLAY_HEIGHT), WHITE )

		Self.myBug = PGBug( RED, BugSim.starting_x, BugSim.starting_y, BugSim.starting_theta )
		#print(Self.myBug)

	def update(Self):
		Self.myBug.wander()

	def draw( Self ):
		Self.screen.fill(WHITE)
		Self.myBug.draw(Self.screen)
		pygame.display.update()

	def keyDown(Self, key):
		
		if key == K_SPACE:
			Self.myBug.move_forward()
		elif key == K_LEFT:
			Self.myBug.turn_left()
		elif key == K_RIGHT:
			Self.myBug.turn_right()
		else:
			print(key)

		#print(Self.myBug.position)


if __name__ == "__main__":
	g = BugSim()
	g.mainLoop(60)
    

