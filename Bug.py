
#Things to do
#import logging
#fix z axis flip from pygame to local coord system
#have a scale for drawing in pygame that is independent of bug kinematics
#have a sample period so can do velocity
#simulate collision dynamics to mimic accelerameter
#kinematics for zumo

#food
#objects
#eyes
#range
#collisions could do damage
#minimize energy

import numpy as np
import transforms3d.affines as AFF 
import transforms3d.euler as E
import random as rand

#Bug
#knows how to move
#holds attributes
#has a brain
#has sensors
#has outputs

#Bug parts
#has a shape, size, color, location(relative to base), hitbox(relative to location)
#knows how to draw itself
#knows what type of collisions to register for

#Collision 
#type
#callback method

#Color class so can separate out code from PG specific stuff.
class Color:
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	RED = (255,0,0)
	BLUE = (0,255,0)
	GREEN = (0,0,255)




class Bug:

	#Going to use 3D matrices even if in 2d
	#See http://matthew-brett.github.io/transforms3d/ for details on the lib used

	#Bug's local coord frame is in the x,y plane and faces in the x direction.  
	#Positive rotation follow RHR, x-axis into the y-axis...so z is up.

	DEFAULT_TURN_AMT = np.deg2rad(30) # turns are in radians
	DEFAULT_MOVE_AMT = 5
	
	def __init__( Self, starting_x = 0, starting_y = 0, starting_z = 0, starting_theta = 0 ):
		Self.set_position( starting_x, starting_y, starting_z, starting_theta)

	def __repr__(Self):
		return( "position={}".format(Self.position) )

	def set_position( Self, x=0, y=0, z=0, theta=0 ):
		#assume the angle is measured in the x,y plane around z axis

		T = [x, y, z] #create a translation matrix
		R = E.euler2mat( 0, 0, theta ) #create a rotation matrix around Z axis.
		Z = [1, 1, 1] # zooms...only included because API required it... will ignore the skew
		Self.position = AFF.compose(T, R, Z)

	def move_forward( Self, amount_to_move = DEFAULT_MOVE_AMT ):
		#assume bug's 'forward' is along the x direction in local coord frame
		mF = np.identity(4)
		mF[0][3] = amount_to_move 
		Self.position = np.matmul( Self.position, mF ) #translate the position by the translation transformation

	def turn_left( Self, theta = DEFAULT_TURN_AMT ):
		#create a rotation matrix around z
		#positive angle means CCW from x axis
		T = [0, 0, 0] #create a translation matrix
		R = E.euler2mat( 0, 0, theta ) #create a rotation matrix around Z axis.
		Z = [1, 1, 1] # zooms...only included because API required it... will ignore the skew
		rM = AFF.compose(T, R, Z)
		Self.position = np.matmul(Self.position, rM )

	def turn_right( Self, theta  = DEFAULT_TURN_AMT ):
		#'turning right is just a negative angle passed to turn left'
		Self.turn_left( -theta )

	def wander( Self ):
		rand_x = rand.randint( 0, Bug.DEFAULT_MOVE_AMT )
		T = [ rand_x, 0, 0]
		rand_theta = rand.uniform( -Bug.DEFAULT_TURN_AMT, Bug.DEFAULT_TURN_AMT )
		R = E.euler2mat( 0, 0, rand_theta )
		Z = [1, 1, 1] # zooms...only included because API required it... will ignore the skew
		rM = AFF.compose(T, R, Z) #random transformation including turn and forward
		Self.position = np.matmul(Self.position, rM )


#----------------- START PYGAME SPECIFIC CODE ---------------------------------------

import pygame

#assume 2D graphics and using Pygame to render.
class PGBug(Bug):

	pg2bugxform = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]] 
	bug2pgxform = pg2bugxform

	def __init__(Self, color , starting_x = 0, starting_y = 0, starting_theta = 0 ):
		Self.color = color
		Self.size = 10
		Self.wrap = True
		super(PGBug, Self).__init__( starting_x, starting_y, 0, starting_theta )
	
	# PyGame canvas starts x=0, y=0 at upper left rather than lower left
	# which inverts the z-axis due to right hand rule.
	# So, need a transformation from virtual coord system of the bug to display coord system
	def pg2bug_coord( PG_coords ):
		return (np.matmul(PGBug.pg2bugxform, PG_coords))

	def bug2pg_coord( Bug_coords ):
		return (np.matmul(PGBug.bug2pgxform, Bug_coords))

	def draw(Self, surface):
		
		width, height = surface.get_size()

		if Self.wrap:
			if Self.position[0][3] < 0:  Self.position[0][3] = width 
			elif Self.position[0][3] > width: Self.position[0][3] = 0

			if Self.position[1][3] < 0: Self.position[1][3] = height
			elif Self.position[1][3] > height: Self.position[1][3] = 0
		else:
			if Self.position[0][3] < 0:  Self.position[0][3] = 0 
			elif Self.position[0][3] > width: Self.position[0][3] = width

			if Self.position[1][3] < 0: Self.position[1][3] = 0
			elif Self.position[1][3] > height: Self.position[1][3] = height

		PG_coords = PGBug.bug2pg_coord( Self.position )
		#print(PG_coords)
		x = int(PG_coords[0][3])
		y = int(PG_coords[1][3])
		pygame.draw.circle(surface, Self.color, (x,y), Self.size, 0) 
	
