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


#contains rules of interactions
#how do bugs die
#have a score that indicates successfulness (distance travelled, area covered, energy amount (expended moving, gained eating) )
#how do bugs reproduce (should we use the "weakest 500" to avoid extinction events)


import numpy as np
import random
import transforms3d.affines as AFF 
import transforms3d.euler as E
import random as rand

class Circle(object):
    def __init__(self, x0, y0, R):
        self.x, self.y, self.R = x0, y0, R

    def area(self):
        return pi*self.R**2

    def circumference(self):
        return 2*pi*self.R

	def 2D_circle_collision( c1 c2 )
		#takes two Circle class objects in.
		dx = circle1.x - circle2.x;
		dy = circle1.y - circle2.y;
		distance = np.sqrt(dx * dx + dy * dy);

		if (distance < c1.radius + c2.radius): return True
		else: return False


def BWObject():

	#everything is a BWO object including bug body parts (e.g., eyes, ears, nose).
	#it has a position and orientation relative to the container, which could be the world.  But it could be the body, the eye
	#should store its location and orientation
	#should know what collisions to register for
	#should know how to set its absolute location so can draw and detect collisions

	position = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]] #equates to x=0, y=0, z=0, rotation = 0
	abs_position = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]] #equates to x=0, y=0, z=0, rotation = 0
	BWObject container #callback handler to the object that contains this.  E.g., for a bug it would be the world, for an eye, it would be the bug

 	def __init__(Self, container ):
 		Self.container = container #a pointer back to the object that is holding this one.

	def set_rel_position(Self, pos_transform): # position relative to its container
		Self.position = pos_transform #assume identity matrix
		Self.set_hitbox()

	def set_abs_position(Self, base_transform)
		return np.matmul( base_transform, Self.position )

	def get_abs_position(Self): #gets relative to its container
		try:
			ct = Self.container.get_rel_position() #get the accumulated container transform
			return np.matmul(ct, Self.position )
		except: 
			print("Couldn't call the container position")
			return Self.position

	def get_rel_position(Self): #gets position within the world
		#get parent position, which will be recursive
		#multiply parent * Self.position
		return Self.position
	

	def set_hitbox( Self, circle ):
		pass

	def get_hitbox( Self, circle ):
		pass

	def collision_handler(): #called if 
		pass

#eyes collide with light
#bodies collide with other solid bodies
#objects can emit light
#objects can collide with light


class BugWorld():
	#defines the world, holds the objects, defines the rules of interaction
	BOUNDARY_WIDTH = 800
	BOUNDARY_HEIGHT = 600

	NUM_CARNIVORE_BUGS = 3
	NUM_OMNIVORE_BUGS = 2
	NUM_HERBIVORE_BUGS = 10
	NUM_PLANT_FOOD = 20
	NUM_MEAT_FOOD = 1
	NUM_OBSTACLES = 15

	position = [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]] #sets the world as the root equates to x=0, y=0, z=0, rotation = 0
	
	#Master list of all objects
		#create
		#update
		#detect collisions
		#draw



	#used for collisions
	SolidObjects = [] #bugbodies, food, obstacles add themselves to this list
	LightEmittingObjects = [] #bugbodies, food, obstacles add themselves to this list
	LightDetectingObjects = [] #add eye hit boxes themselves to this list
	#OdorEmittingObjects 
	#OdorDetectingObjects
	#SoundEmittingObjects
	#SoundDetectingObjects


	def __init__( Self, starting_x = 0, starting_y = 0, starting_z = 0, starting_theta = 0 ):
		Self.set_position( starting_x, starting_y, starting_z, starting_theta) #base coord system for world
		# Create all of the items in the world

		for _ in 

	def get_pos_transform( x=0, y=0, z=0, theta=0 ): #utility function to encapsulate translation and rotation
		#use this anytime a transform is needed in the world.  
		#assume the angle is measured in the x,y plane around z axis
		#it will be an absolute transform in the local x, y, theta space
		T = [x, y, z] #create a translation matrix
		R = E.euler2mat( 0, 0, theta ) #create a rotation matrix around Z axis.
		Z = [1, 1, 1] # zooms...only included because API required it... will ignore the skew
		return AFF.compose(T, R, Z)

	def set_position( Self, x=0, y=0, z=0, theta=0 ):
		Self.position = Self.get_pos_transform( x, y, z, theta)

	def get_random_location_in_world():
		x = random.randint(0, BOUNDARY_WIDTH )
		y = random.randint(0, BOUNDARY_HEIGHT)
		z = 0
		theta = random.uniform(0, 2*np.pi) #orientation in radians
		return = Self.get_pos_transform( x, y, z, theta )
	
	def update():
		#call update on each object passing base coord
		#detect collisions

		#For PG method, change display with info data
		pass

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






#----------------------------
#PGBugWorld where pygame dependent code goes

#contains draw code
#BWO's should have a draw method that includes itself, hitboxes (based on global var)
#should have a method to overwrite that knows how to draw itself
#toggle display of light, smell, sound

#how to do top down draw so that matmuls are only done once.