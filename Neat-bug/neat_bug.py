'''
General settings and implementation of a test bug
'''
#http://nn.cs.utexas.edu/downloads/papers/stanley.ieeetec05.pdf

import numpy as np

class NeatBug(object):

    time_step = 0.5  # time step in seconds
    ef = .50 #the energy factor...how much does energy count towards fitness
    hf = .50 #the health factor...how much does the health count towards fitness
    sf = 1.0 #the score factor...how much does the score count towards fitness
    target_x_range = [-1000, 1000]
    target_y_range = [-1000, 1000]
    target_x = 300
    target_y = 400

    def __init__( self ):
        self.size = 10  #size of the bug used for kinematics
        self.health = 100 #starting health of the bug
        self.energy = 50 #starting energy of the bug
        self.score = 0 #starting score of the bug
        self.age = 0 #used in rtNeat so that young agents aren't deleted or mated.
        self.x, self.delta_x = 0,0 #starting position
        self.y, self.delta_y = 0,0 #starting position
        self.max_dist = self.size * 5
        self.bias = 1.0 #to nudge it if need be
        self.theta = 0 #starting orientation
        self.t = 0
        self.dt = self.time_step #how much time in between brain activations.
        self.generate_target()

    def generate_target( self ):
        self.target_x = np.random.randint( self.target_x_range[0],self.target_x_range[1]  )
        self.target_y = np.random.randint( self.target_y_range[0],self.target_y_range[1]   )
        #print("x:{0} y:{1}".format(self.target_x, self.target_y))


    def step( self, action ):

        self.kinematic_wander( action )

        distance_from_target = np.sqrt((self.target_x-self.x)**2+(self.target_y-self.y)**2)

        #make the fitness number really large if very close to the target
        if( distance_from_target > 0 ):
            self.score = 1/distance_from_target 

        #increment the simulation time that has occurred
        self.t += self.dt
 
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))
    
    def get_scaled_state(self):

        #get the sensor input for the current time step

        #normalize them from 0-1

        #return as inputs for the net

        #health and energy should be inputs to net
        #delta_x ...feeds back how much it actually moved
        #delta_y ...feeds back how much it actually moved
        #delta_theta ... feeds back how much it actually moved

        #could do food distance as well?  what does it "desire"

        #Get full state, scaled into (approximately) [0, 1].

        #normalize across all inputs...
        #sigmoid goes from [0,1]
        #x_dist = self.sigmoid((self.target_x-self.x))
        #y_dist = self.sigmoid((self.target_y-self.y))
        
        #tanh goes from [-1,1]
        x_dist = np.tanh((self.target_x-self.x))
        y_dist = np.tanh((self.target_y-self.y))
 
        if (np.abs(x_dist) < 1.0 or np.abs(y_dist) < 1.0 ):
            #print("x:{0} y:{1}".format(x_dist, y_dist))
            pass

        return [ x_dist, y_dist, 1, 1, 1, 1 ] #have 4 bias neurons that are always on
 

    def fitness(self):

#        return ((self.hf*self.health)*(self.ef*self.energy))+self.sf*self.score
        #fitness is only based on how close to the target it gets.
        return( self.score )


    def kinematic_wander(self, action):
        velocity_scale = 10.0
        vr = action[0] * velocity_scale #velocity for right wheel
        vl = action[1] * velocity_scale #velocity for left wheel

        #how much to move in x, y and in rotation
        self.delta_x, self.delta_y, self.delta_theta = self.kinematic_move( vr, vl )
        self.x += self.delta_x
        self.y += self.delta_y
        self.theta += self.delta_theta

    def kinematic_move( Self, vel_r, vel_l ): #assume bugbot with two wheels on each side of it.
                                              #taken from GRIT robotics course
        wheel_radius = Self.size * 0.5 #wheel radius is some proportion of the radius of the body
        wheel_separation = Self.size * 2 #wheels are separated by the size of the bug
        delta_theta = ( wheel_radius/wheel_separation)*(vel_r - vel_l )
        temp_vect = (wheel_radius/2)*(vel_r + vel_l)
        delta_x = temp_vect * np.cos( delta_theta )
        delta_y = temp_vect * np.sin( delta_theta )
        return delta_x, delta_y, delta_theta

        #update health, energy and score
        #self.health = calc_health()
        #for this sim, the further it moves from origin, the more likely something bad happened
        #however, it can regain some health over time
'''
        prh = 1-np.exp(-distance_since_start) #probability that a hit happened
        rv = random.uniform(0,1)*10   #how much damage did it do?
        hhv = rv*prh #health hit value
        hrv = 1 #health regen value each step
        self.health =  self.health+hrv - hhv
        if self.health > 100: self.health = 100
        elif self.health < 0: self.health = 0
'''

        #self.energy = calc_energy()
        #for this sime, the further it moved and the more it turned, the more energy used
        #but the more likely it found food and energy increased
        #should be asymptotic to 100...max energy
'''
        self.energy = self.energy - self.delta_x - self.delta_y
        if self.energy > 100: self.energy = 100
        elif self.energy < 0: self.engery = 0
'''
        #self.score = calc_score()