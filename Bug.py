
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
		super()._init_( pos_transform, name )
		Self.size = size
		Self.color = Color.GREY 

	def update( Self, base ):
		#eyes don't move independent of bug, so relative pos won't change.
		Self.set_abs_position( base ) #update it based on the passed in ref frame

class Bug ( BWObject ):

	DEFAULT_TURN_AMT = np.deg2rad(30) # turns are in radians
	DEFAULT_MOVE_AMT = 5

	def __init__( Self, initial_pos, name = "Bug" ):
		super()._init_( initial_pos, name )
		Self.size = 10 #override default and set the intial radius of bug
		Self.color = Color.PINK #override default and set the initial color of a default bug

		#add the eyes for a default bug
		Self.RIGHT_EYE_LOC = BugWorld.get_pos_transform( Self.size, 0, np.deg2rad(-10) ) #put eye center on circumference
		Self.LEFT_EYE_LOC = BugWorld.get_pos_transform( Self.size, 0, np.deg2rad(10) )
		Self.EYE_SIZE = int(Self.size * 0.2) #set a percentage the size of the bug
		#instantiate the eyes
		Self.RightEye = BugEye( Self.RIGHT_EYE_LOC, Self.EYE_SIZE ) 
		Self.LeftEye = BugEye( Self.LEFT_EYE_LOC , Self.EYE_SIZE )

	def update( Self, base ):
		Self.wander() #changes the relative position
		Self.set_abs_position( base )
		Self.RightEye.update( Self.abs_position )
		Self.LeftEye.update( Self.abs_position )

	def draw( Self, surface ):
		super().draw(surface)
		Self.RightEye.draw(surface)
		Self.LeftEye.draw(surface)

	def move_forward( Self, amount_to_move = DEFAULT_MOVE_AMT ):
		#assume bug's 'forward' is along the x direction in local coord frame
		tM = BW.get_pos_transform( x=amount_to_move, y=0, z=0, theta=0 ) #create an incremental translation
		Self.set_rel_position ( np.matmul(Self.rel_postion, tM)) #update the new position

	def turn_left( Self, theta = DEFAULT_TURN_AMT ):
		rM = BW.get_pos_transform( x=0, y=0, z=0, theta=theta ) #create an incremental rotation
		Self.set_rel_position (np.matmul(Self.rel_position, rM )) #update the new position

	def turn_right( Self, theta  = DEFAULT_TURN_AMT ):
		#'turning right is just a negative angle passed to turn left'
		Self.turn_left( -theta )

	def wander( Self ):
		rand_x = random.randint( 0, Bug.DEFAULT_MOVE_AMT )
		rand_theta = random.uniform( -Bug.DEFAULT_TURN_AMT, Bug.DEFAULT_TURN_AMT )
		wM = BW.get_pos_transform( x=rand_x, y=0, z=0, theta=rand_theta ) #create an incremental movement
		Self.set_rel_position(np.matmul(Self.rel_position, wM )) #update the new relative position

class Herbivore( Bug ): 
	def __init__ (Self, starting_pos, name = "Herb" ):
		super().__init__( starting_pos, name )
		Self.color = Color.GREEN

class Omnivore( Bug ): #Orange
	pass

class Carnivore( Bug ): #Red
	pass


