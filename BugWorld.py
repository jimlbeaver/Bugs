
#PGBugWorld where pygame dependent code goes

#contains draw code
#BWO's should have a draw method that includes itself, hitboxes (based on global var)
#should have a method to overwrite that knows how to draw itself
#toggle display of light, smell, sound

#----------------- START PYGAME SPECIFIC CODE ---------------------------------------

import pygame

#assume 2D graphics and using Pygame to render.
class PGObject():

	def draw( Self, surface ):
		x = int(Self.get_abs_x())
		y = int(Self.get_abs_y())
		pygame.draw.circle(surface, Self.color, (x, y), Self.size, 0) 
	
	def get_abs_x():
		pass

	def get_abs_y():
		pass


#world for simulations to happen 
#has boundaries
#has objects
#	- determines which type
#	- determines where and when
#	- kills objects
#	- determines rules for affecting object attributes (health, mutating, mating)

# need an easily updateable rules abstraction.  Table or something?  Dictionary?

#objects register for different types of collisions (physical, sound, smell, light(RGB))
#objects have hitboxes for each sensor.


#objects emit light at 1/r^2 three different colors
#objects emit sound (varies on speed)
#objects emit smell
#objects have physical collision
#objects have smell collision
#objects have sound collision


# has the sample time which is the update loop time...used for velocity and accleration

#detects collisions
#	- different hitbox shapes.  Hitbox needed for eyes so that collisions can be detected
#		in field of vision (use circles to start for everything.  Could use cones for vision eventually)
#	- should return "distance" so can be used for intensity
#	- returns an intensity of collision (for eye interaction with light, sound, smell)

	 ### MAIN TEST FOR Pointwise COLLISION ###
	 #   if(mx in range(x-radius,x+radius) and my in range(y-radius,y+radius)):
	 #      hit=True
	 #   else:
	 #       hit=False

	 ### Main test for colliding circles ##
	# The distance between the two centers (x1,y1) and (x2,y2) can be calculated and compared as:
	#d = sqrt((y2-y1) * (y2-y1) + (x2-x1) * (x2-x1));
	#if (d < r1 + r2) { ... bang ... }
	# OR to avoid sqrt for efficiency
	#dsqrd = (y2-y1) * (y2-y1) + (x2-x1) * (x2-x1);
	#if (dsqrd < (r1+r2)*(r1+r2)) { ... bang ... }



#updates objects

#eyes collide with light
#bodies collide with other solid bodies
#objects can emit light
#objects can collide with light
#contains rules of interactions
#how do bugs die
#have a score that indicates successfulness (distance travelled, area covered, energy amount (expended moving, gained eating) )
#how do bugs reproduce (should we use the "weakest 500" to avoid extinction events)


import numpy as np
import random
import transforms3d.affines as AFF 
import transforms3d.euler as E

#Color class so can separate out code from PG specific stuff.
#http://www.discoveryplayground.com/computer-programming-for-kids/rgb-colors/
class Color(): #RGB values
	BLACK = (0,0,0)
	WHITE = (255,255,255)
	RED = (255,0,0)
	GREEN = (0,255,0)
	BLUE = (0,0,255)
	YELLOW = (255,255,0)
	PINK = (255,192,203)
	BROWN = (160,82,45)
	ORANGE = (255, 165, 0)
	DARK_GREEN = (34,139,34)
	GREY = (190,190,190)


#Going to use 3D matrices even if in 2d
#See http://matthew-brett.github.io/transforms3d/ for details on the lib used
#Object's local coord frame is in the x,y plane and faces in the x direction.  
#Positive rotation follow RHR, x-axis into the y-axis...so z is up.

class BugWorld(): #defines the world, holds the objects, defines the rules of interaction

#--- Class Constants
	BOUNDARY_WIDTH = 800
	BOUNDARY_HEIGHT = 600
	BOUNDARY_WRAP = True

	NUM_CARNIVORE_BUGS = 3
	NUM_OMNIVORE_BUGS = 2
	NUM_HERBIVORE_BUGS = 10
	NUM_PLANT_FOOD = 20
	NUM_MEAT_FOOD = 1
	NUM_OBSTACLES = 15
	IDENTITY = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]] #equates to x=0, y=0, z=0, rotation = 0

	WorldObjects = []

#used for collisions
	#SolidObjects = [] #bugbodies, food, obstacles add themselves to this list
	#LightEmittingObjects = [] #bugbodies, food, obstacles add themselves to this list
	#LightDetectingObjects = [] #add eye hit boxes themselves to this list
	#OdorEmittingObjects 
	#OdorDetectingObjects
	#SoundEmittingObjects
	#SoundDetectingObjects

#--- Instance Methods	
	def __init__(Self):
		Self.rel_position = BugWorld.IDENTITY #sets the world as the root equates to x=0, y=0, z=0, rotation = 0
		for i in range(0, BugWorld.NUM_HERBIVORE_BUGS):
			start_pos = BugWorld.get_random_location_in_world()
			Self.WorldObjects.append( Herbivore( start_pos, "H"+ str(i) ))

		for i in range(0, BugWorld.NUM_CARNIVORE_BUGS):
			start_pos = BugWorld.get_random_location_in_world()
			Self.WorldObjects.append( Carnivore( start_pos, "C"+ str(i) ))

		for i in range(0, BugWorld.NUM_OMNIVORE_BUGS ):
 			start_pos = BugWorld.get_random_location_in_world()
 			Self.WorldObjects.append( Omnivore( start_pos, "O"+ str(i) ))

	def update(Self):
		for BWO in Self.WorldObjects:
			BWO.update(Self.rel_position)

	def draw( Self, surface ):
		for BWO in Self.WorldObjects:
			BWO.draw( surface )
	
	def detect_collisions():
		#detect light collisions
		#detect physical collisons
		#detect odor collisions
		#detect sound collisions
		pass

	def detect_light_collisions():
		#loop through light emitting objects and see if they collide with light detecting
		#make sure doesn't collide with self
		#need to differientiate between RGB detection/emission
		#need to differentiate intensities so objects further away stimulate less
		pass

	def detect_physical_collisions():
		#loop through solid bodies
		#call collision handlers on each object
		pass

#----- Utility Class Methods ----------------

	def adjust_for_boundary( wT ): #adjust an inputed transform to account for world boundaries and wrap
		if BugWorld.BOUNDARY_WRAP:
			if wT[0][3] < 0:  wT[0][3] = BugWorld.BOUNDARY_WIDTH 
			elif wT[0][3] > BugWorld.BOUNDARY_WIDTH: wT[0][3] = 0

			if wT[1][3] < 0: wT[1][3] = BugWorld.BOUNDARY_HEIGHT
			elif wT[1][3] > BugWorld.BOUNDARY_HEIGHT: wT[1][3] = 0
		else:
			if wT[0][3] < 0:  wT[0][3] = 0 
			elif wT[0][3] > BugWorld.BOUNDARY_WIDTH: wT[0][3] = BugWorld.BOUNDARY_WIDTH

			if wT[1][3] < 0: wT[1][3] = 0
			elif wT[1][3] > BugWorld.BOUNDARY_HEIGHT: wT[1][3] = BugWorld.BOUNDARY_HEIGHT

		return wT #return the updated transform

	def get_pos_transform( x=0, y=0, z=0, theta=0 ): #utility function to encapsulate translation and rotation
		#use this anytime a transform is needed in the world.  
		#assume the angle is measured in the x,y plane around z axis
		#it will be an absolute transform in the local x, y, theta space
		T = [x, y, z] #create a translation matrix
		R = E.euler2mat( 0, 0, theta ) #create a rotation matrix around Z axis.
		Z = [1, 1, 1] # zooms...only included because API required it... will ignore the skew
		return AFF.compose(T, R, Z)

	def get_x( position ):
		return position[0][3] 

	def get_y( position ):
		return position[1][3] 

	def get_random_location_in_world():
		x = random.randint(0, BugWorld.BOUNDARY_WIDTH )
		y = random.randint(0, BugWorld.BOUNDARY_HEIGHT)
		z = 0
		theta = random.uniform(0, 2*np.pi) #orientation in radians
		return BugWorld.get_pos_transform( x, y, z, theta )
	

class BWObject( PGObject ): #Bug World Object

	#Everything is a BWObject including bug body parts (e.g., eyes, ears, noses).
	#has a position and orientation relative to the container, which could be the world.  But it could be the body, the eye
	#has a color
	#has a size
	#has a name
	#stores an absolute position to prevent recalculating it when passing to contained objects.

	#stub methods for what collisions to register for

	def __init__(Self, starting_pos = BugWorld.IDENTITY, name = "BWOBject"):
  		Self.rel_position = starting_pos
  		Self.abs_position = starting_pos
  		Self.name = name
  		Self.size = 1 #default...needs to be overridden
  		Self.color = Color.BLACK #default...needs to be overridden

	def __repr__(Self):
  		return ( Self.name + ": abs position={}".format(Self.abs_position) ) #print its name and transform

	def set_rel_position(Self, pos_transform = BugWorld.IDENTITY): # position relative to its container
		Self.rel_position = BugWorld.adjust_for_boundary( pos_transform ) #class method handles boundary adjustment
		return Self.rel_position			

	def set_abs_position(Self, base_transform = BugWorld.IDENTITY):
		Self.abs_position = np.matmul( base_transform, Self.rel_position )
		return Self.abs_position

	def get_abs_x( Self ):
		return( BugWorld.get_x( Self.abs_position ) )

	def get_abs_y( Self ):
		return( BugWorld.get_y( Self.abs_position ) )

	def update( Self, base ): #stub method. Override to move this object each sample period
		pass	

	def register_collision_detection():
		pass

	def collision_handler(): #stub method.  Override this to handle collsions 
		pass

	
class Circle(object):
	def __init__(self, x0, y0, R):
		self.x, self.y, self.R = x0, y0, R

	def area(self):
		return pi*self.R**2

	def circumference(self):
		return 2*pi*self.R

	def circle_collision( c1, c2 ):	#takes two Circle class objects in.
		dx = c1.x - c2.x;
		dy = c1.y - c2.y;
		distance = np.sqrt(dx * dx + dy * dy);

		if (distance < c1.radius + c2.radius): return True
		else: return False

#Things to do
#import logging
#fix z axis flip from pygame to local coord system
#have a scale for drawing in pygame that is independent of bug kinematics


#have a sample period so can do velocity
#simulate collision dynamics to mimic accelerometer
#kinematics for zumo
#kinematics for gopigo

#range
#collisions could do damage
#minimize energy spent
#maximize health


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


class Obstacle( BWObject ): #yellow
	pass

class Meat( BWObject ): #brown
	pass

class Plant( BWObject ): #dark green
	pass
#---------


class BugEye( BWObject ):
	def __init__( Self, pos_transform = BugWorld.IDENTITY, size = 1 ):
		Self.name = "E"
		super().__init__( pos_transform, Self.name )
		Self.size = size
		Self.color = Color.GREY 

	def update( Self, base ):
		#eyes don't move independent of bug, so relative pos won't change.
		Self.set_abs_position( base ) #update it based on the passed in ref frame

class Bug ( BWObject ):

	DEFAULT_TURN_AMT = np.deg2rad(30) # turns are in radians
	DEFAULT_MOVE_AMT = 5

	def __init__( Self, initial_pos, name = "Bug" ):
		super().__init__( initial_pos, name )
		Self.size = 10 #override default and set the intial radius of bug
		Self.color = Color.PINK #override default and set the initial color of a default bug

		#add the eyes for a default bug
		#put eye center on circumference, rotate then translate.
		rT = BugWorld.get_pos_transform( 0, 0, 0, np.deg2rad(-30) )
		tT = BugWorld.get_pos_transform( Self.size, 0, 0, 0 )
		Self.RIGHT_EYE_LOC = np.matmul(rT,tT)

		rT = BugWorld.get_pos_transform( 0, 0, 0, np.deg2rad(30) )
		Self.LEFT_EYE_LOC = np.matmul(rT,tT)

		Self.EYE_SIZE = int(Self.size * 0.50) #set a percentage the size of the bug
		#instantiate the eyes
		Self.RightEye = BugEye( Self.RIGHT_EYE_LOC, Self.EYE_SIZE )
#		Self.RightEye.color = Color.RED

		Self.LeftEye = BugEye( Self.LEFT_EYE_LOC, Self.EYE_SIZE )


	def update( Self, base ):
		Self.wander() #changes the relative position
#		Self.move_forward( 1 )
		Self.set_abs_position( base )
		Self.RightEye.update( Self.abs_position )
		Self.LeftEye.update( Self.abs_position )

	def draw( Self, surface ):
		super().draw(surface) #inherited from BWObject
		Self.RightEye.draw(surface)
		Self.LeftEye.draw(surface)

	def move_forward( Self, amount_to_move = DEFAULT_MOVE_AMT ):
		#assume bug's 'forward' is along the x direction in local coord frame
		tM = BugWorld.get_pos_transform( x=amount_to_move, y=0, z=0, theta=0 ) #create an incremental translation
		Self.set_rel_position ( np.matmul(Self.rel_position, tM)) #update the new position

	def turn_left( Self, theta = DEFAULT_TURN_AMT ):
		rM = BugWorld.get_pos_transform( x=0, y=0, z=0, theta=theta ) #create an incremental rotation
		Self.set_rel_position (np.matmul(Self.rel_position, rM )) #update the new position

	def turn_right( Self, theta  = DEFAULT_TURN_AMT ):
		#'turning right is just a negative angle passed to turn left'
		Self.turn_left( -theta )

	def wander( Self ):
		rand_x = random.randint( 0, Bug.DEFAULT_MOVE_AMT )
		rand_theta = random.uniform( -Bug.DEFAULT_TURN_AMT, Bug.DEFAULT_TURN_AMT )
		wM = BugWorld.get_pos_transform( x=rand_x, y=0, z=0, theta=rand_theta ) #create an incremental movement
		Self.set_rel_position(np.matmul(Self.rel_position, wM )) #update the new relative position

class Herbivore( Bug ): 
	def __init__ (Self, starting_pos, name = "Herb" ):
		super().__init__( starting_pos, name )
		Self.color = Color.GREEN

class Omnivore( Bug ): #Orange
	def __init__ (Self, starting_pos, name = "OMN" ):
		super().__init__( starting_pos, name )
		Self.color = Color.ORANGE

class Carnivore( Bug ): #Red
	def __init__ (Self, starting_pos, name = "CARN" ):
		super().__init__( starting_pos, name )
		Self.color = Color.RED



