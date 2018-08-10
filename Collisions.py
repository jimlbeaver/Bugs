
'''
Collision API
	Collisions() - container for the list of objects
	CollisionObject() - necessary class to participate in the API

	Usage:
		1) Create a Collisions object
		2) Add the types of objects that can collide and the method to call when they do
		3) add the instances of the objects...destructor takes care of removing it from the collisions list if the object
			is deleted

	Definitions:
		1) Hitbox is the object that gets detected.  Sometimes the hitbox is the object.  Other times, the hitbox is a child
		   off of the object because it is offset from the object
		2) Hitbox type will be used to use circles, bounding boxes etc.  Would like to do a cone for eyesight to get directionality




	Used to hold references to objects that can collide
	Detects collisions of those objecs
	Calls a handler method depending on the type of the object
	Defines an interface that collision objects must inherit/support for it to work
	Support different bounding box, aka hit box types
	recursively calls "isThisMe" to make sure it isn't colliding with itself or it's owner
	does having emmitters and detectors and separate lists help with processing time?
	register the hitboxes
	the objects should know what lists they are on but should be encapsulated so don't have to know internal structure

'''

#Use transforms to represent absolute position, that way always know regardless of env

#Have CollisionObject defined int the Collision class?

class CollisionObject():

	HITBOX_CIRCLE = int(1)
	HITBOX_RECT	= int(2)

	def __init__( Self )
		#must be overwritten so that if an object inherits this, it MUST know to add itself to a Collisions list.
		pass

	def get_abs_x(Self):
		#must override
		pass

	def get_abs_y(Self):
		#must override
		pass

	def get_size(Self):
		#must override and return radius
		pass

	def get_hitbox_type( Self ):
		#default will be circle
		pass

	def set_hitbox_type( Self ):
		Self.hitbox_type = HITBOX_CIRCLE





class CollisionDict():

	#need add
	#method to call handler

	def add_handler(CO1, CO2, fucntion_to_call)
	#make an entry for both CO1, CO2 and CO2, CO1 unless they are the same

#Could have different classes upon inheritance so it would know which Collision class to call


class Collisions():
	_co = CollisionObject[]

	_cd = CollisionDict()

	def add_object(Self, CollisonObject co):
		collision_objects.append = co

	def remove_object(Self, CollisionObject co):
		#find object in list and remove it

	def print_collision( OB1, OB2 ):
		# print(OB1.name + 'T: ' + str(OB1.type) + ' H: ' + str(OB1.health) + ', ' 
			# + OB2.name + 'T: ' + str(OB2.type) + ' H: ' + str(OB2.health))
		pass		

	def detect_collision( Self, hb1, hb2 )
		if (hb1.hitbox_type != Collision.CollisionObject.hitbox_circle ):
			pass
		if (hb2.hitbox_type != Collision.CollisionObject.hitbox_circleCircleHitbox ):
			pass
		return Self.circle_collision( hb1, hb2 )

	def circle_collision( Self, CO1, CO2 ):	#takes two Circle Hitbox Objects in.
		dx = CO1.get_abs_x() - CO2.get_abs_x()
		dy - CO1.get_abs_y() - CO2.get_abs_y()

		dist_sqrd = ( dx * dx ) + ( dy * dy )
		#size is radius of objections circle hit box
		if (dist_sqrd < (CO1.get_size() + CO2.get_size())**2) : return True
		else: return False


#-------------------------------------------


class CollisonObjectType():

	#use integers so it is faster for dict lookups
	HERB = int(1) # Herbivore
	OMN = int(2)  # Omnivore
	CARN = int(3) # Carnivore 
	OBST = int(4) # Obstacle
	MEAT = int(5) # Food for Carnivore and Omnivore
	PLANT = int(6)# Food for Herbivore and Omnivore
	OBJ = int(7)  #catch all for the base class.  Shouldn't ever show up

	EYE = int(8)

	
class PhysicalCollisions():
	#Dictionary: two types as the keys, function as the item 
	#passes pointers into each object

#Bug to Bug interactions
	def herb_omn( herb, omn ): #handle herbivore an omnivore collision
		BWCollisionDict.print_collision( herb, omn )
		#do damage to herbivore
		herb.health -= 1

	def herb_carn( herb, carn):
		BWCollisionDict.print_collision( herb, carn )
		#do damage to herbivore
		herb.health -= 20

	def herb_herb( herb1, herb2 ):
		BWCollisionDict.print_collision( herb1, herb2 )
		#certain probability of mating?

	CollisionDict={ # look up which function to call when two objects of certain types collide
		(BWOType.HERB, BWOType.OMN): herb_omn,
		(BWOType.HERB, BWOType.CARN ): herb_carn,
		(BWOType.HERB, BWOType.HERB): herb_herb,
		(BWOType.OMN, BWOType.OMN ): omn_omn,
		(BWOType.OMN, BWOType.CARN): omn_carn,
		(BWOType.CARN, BWOType.CARN ): carn_carn,
		(BWOType.HERB, BWOType.PLANT ): herb_plant,
		(BWOType.OMN, BWOType.PLANT ): omn_plant,
		(BWOType.OMN, BWOType.MEAT ): omn_meat,
		(BWOType.CARN, BWOType.MEAT ): carn_meat,
		(BWOType.HERB, BWOType.OBST ): herb_obst,
		(BWOType.OMN, BWOType.OBST ): omn_obst,
		(BWOType.CARN, BWOType.OBST ): carn_obst

		}

	def handle_collision( Self, OB1, OB2):
		if (OB1.type > OB2.type ): Self.handle_dict(OB2, OB1) #order the keys for dict lookup
		else: Self.handle_dict(OB1, OB2)

	def handle_dict( Self, OB1, OB2 ):
		try:
			Self.CollisionDict[(OB1.type,OB2.type)]( OB1, OB2 ) #use types to lookup function to call and then call it
		except KeyError:
			pass #ignore it if isn't in dictionary

			# for debugging
			# if not (OB1.type == BWOType.OBST or OB2.type == BWOType.OBST ): #ignore if something dies on an obstacle
			# 	print('No handler for: ' + OB1.name + ' T:' + str(OB1.type)	+ ", " +
			# 							OB2.name + ' T:' + str(OB2.type))




	def detect_collisions( Self ):
		#loop through solid bodies
		#call collision handlers on each object
		for CO1 in Self._co:
			for CO2 in Self._co:
				if CO1 == CO2: continue #need to call isThisMe()
				elif Self.circle_collision(CO1, CO2):
					# print("Hit " + CO1.name + " and " + CO2.name )
					Self.CollisionDict.handle_collision(CO1, CO2)



'''
	For an object to participate in Collision Detection it must inherit from the Collisions.CollisionObject class
	and must override the methods needed during collision detection
'''

class CollisionTestObject( Collisions.CollisionObject ):

	def __init__( Self, CollisionTestWorld, x, y, size ):
		Self.x = x
		Self.y = y
		Self.size = size
		Self.World = CollsionTestWorld #handle back to container so can call instance methods on it.

	def get_abs_x( Self ):
		return Self.x

	def get_abs_y( Self ):
		return Self.y

	def get_size( Self ):
		return Self.size	



class CollisionTestBug( CollisionTestObject ):

	def __init__( Self, x, y, size ):
		super().init( x, y, size )
		#register for vision emmitter
		#register for physical collision emitter
		#register for physical collision detector

class CollisionTestEye( CollisionTestObject ):
	def __init__( Self, x, y, size ):
		super().init( x, y, size )
		#register for vision detector



class CollisionTestWorld():
	#create multiple collision collections

	def __init__(Self):
		PhysicalCollisions = Collisions()
		VisualCollsions = Collisions()

	def register_physical_emitter()
		pass

	def register_visual_detector()
		pass

	def register_visual_emmitter()
		pass

	def add_bodies( Self ):
		b1 = CollisionTestObject(Self, 0, 0, 10 )
		b2 = CollisionsTestObject( Self, 5, 5, 10)
		b2 = CollisionsTestObject( Self, 5, 5, 10)




	#test constructor/destructor removal



	#test recursive isThisMe


	#test adding handler methods



	#test collision detection

	#test hitbox type checking

	#test bad cases: empty lists, wrong types, no handler, no bounding box type


	#test logging/printing


	def post_collision_processing ( Self ):
		#loop through objects and delete them, convert them etc.
		#if health < 0, delete.
		#if was a bug, convert it to meat
		#if it was a plant, just delete it

		#need to keep track of where in list when deleting so that when an item is deleted, the range is shortened.
		list_len = len( Self.WorldObjects ) #starting lenght of the list of objects
		i = 0 #index as to where we are in the list

		#loop through every object in the list
		while ( i < list_len ):
			if ( Self.WorldObjects[i].health <= 0 ): #if the objects health is gone, deal with it.
				co = Self.WorldObjects[i] #get the current object

				#if it is a bug, then convert it to meat
				if( co.type in { BWOType.HERB, BWOType.OMN, BWOType.CARN } ):
			   		start_pos = co.get_abs_position() #get location of the dead bug
			   		Self.WorldObjects.append( Meat( start_pos, "M"+ str(i) )) #create a meat object at same location
			   		#list length hasn't changed because we are going to delete and add one
				else:
					list_len -= 1	#reduce the length of the list 

				del Self.WorldObjects[i] #get rid of the object
				#'i' should now point to the next one in the list because an item was removed so shouldn't have to increment
			else:
				i += 1 #manually increment index pointer because didn't delete the object


	