#world for simulations to happen 
#has boundaries
#has objects
#	- determines which type
#	- determines where and when
#	- kills objects
#	- determines rules for affecting object attributes (health, mutating, mating)

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
#	- different hitbox shapes (use circles to start for everything)
#	- returns an intensity of collision (for eye interaction with light)
#updates objects

#contains rules of interactions
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




#----------------------------
#PGWorld where pygame dependent code goes

#contains draw code
#toggle display of light, smell, sound