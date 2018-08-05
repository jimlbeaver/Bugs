
#Contains the bugs brain
#https://github.com/karpathy/notpygamejs/blob/master/demos/evolve.html
#http://www.doc.ic.ac.uk/~ejohns/Documents/christophe_steininger_thesis.pdf
#http://www.discovermileshill.com/2017/04/16/genetic-algorithms-tensorflow-and-tensorboard/
#
#Initial architecture
#Feedfoward only
#3 layers
#input
#hidden
#output


#Needs to:
#Instantiate via predefined architecture, Phase 2 it Mario's by developing via random architecture
#Feed forward
#Save itself
#Mutate randomly
#Mutate based on mating
#Normalize inputs based on max ranges (both input and output)

#----Inputs:

#Phase 1
# health
# energy
# score

#Phase 2
# Left Eye (r,g,b)
# Right Eye (r,g,b)

#Phase 3
# nose
# right ear
# left ear

#Phase 4
#recurrent
#randdom

#--------Outputs
#Phase 1
# left wheel value
# right wheel value

#Phase 2
# color (r,g,b)

#Phase 3
# eye position



class BugBrain():

	BRAIN_SIZE = 20
	NUM_INPUTS = 4 
	NUM_OUTPUTS = 2 
	NUM_INPUT_BIAS_NEURONS = 4
	
	
	__init__( Self )
	
		Self.inputs[0] = Self.health
		Self.inputs[1] = Self.energy
		Self.inputs[2] = Self.score
		Self.inputs[3] = Self.left_eye
		Self.inputs[4] = Self.right_eye
		Self.inputs[5] = 1 #bias neuron
		Self.inputs[6] = 1 #bian neuron

		

	def tick(self, inputs ): #called each update
		#take inputs assign to placeholders
		#execute graph
		#capture outputs
		#return outputs
		pass

def testbrain():
	rv1 = Rate(5)
	rv2 = Rate(5)

	for i in range( 1, 5 ):
		t.sleep(.5)
		print( i )
		print ( rv1.get_rate_per_sec(rv1.lastvalue + 5) )
		print ( rv2.get_rate_per_sec(rv2.lastvalue + 2*5) )

# testbrain()





