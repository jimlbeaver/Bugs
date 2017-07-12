
import time as t

class Rate(): #Object that gives a rate in seconds

	def __init__( Self, initial_value = 0 ):
		Self.lasttime = t.time() #in seconds including decimal values to microseconds
		Self.lastvalue = initial_value #could be initial position of something

	def get_rate_per_sec(Self, updated_value ):
		dv = updated_value - Self.lastvalue #gives a vector value so could be negative
		Self.lastvalue = updated_value

		curr_time = t.time()
		dt = curr_time - Self.lasttime
		# print (curr_time, Self.lasttime, dt )

		Self.lasttime = curr_time

		if dt:
			return dv/dt
		else:
			return 0 #no elapsed time so can't be a rate


def testrate():

	rv1 = Rate(5)
	rv2 = Rate(5)

	for i in range( 1, 5 ):
		t.sleep(.5)
		print( i )
		print ( rv1.get_rate_per_sec(rv1.lastvalue + 5) )
		print ( rv2.get_rate_per_sec(rv2.lastvalue + 2*5) )

# testrate()







