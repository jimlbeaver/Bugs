"""
Test the performance of the best genome produced by evolve-ctrnn.py.
"""

from __future__ import print_function

import os
import pickle

from neat_bug import NeatBug

import neat
from neat import nn

# load the winner
with open('winner-ctrnn', 'rb') as f:
    c = pickle.load(f)

print('Loaded genome:')
print(c)

# Load the config file, which is assumed to live in
# the same directory as this script.
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config-ctrnn')
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     config_path)

sim = NeatBug()

net = neat.ctrnn.CTRNN.create(c, config, 1)

print()
print("Initial conditions:")
print("        x = {0:.4f}".format(sim.x))
print("    x_dot = {0:.4f}".format(sim.delta_x))
print("        y = {0:.4f}".format(sim.y))
print("    y_dot = {0:.4f}".format(sim.delta_y))
print()

# Run the given simulation for sim_time seconds.
sim_time = 5.0

while sim.t < sim_time:

    inputs = sim.get_scaled_state()
    print("inputs={}".format(inputs))

    action = net.advance(inputs, sim.time_step, sim.time_step)
    print("outputs={}".format(action))

    # Apply action to the simulated bug
    sim.step(action)
    print("{0:.4f},{1:.4f},{2:.4f},{3:.4f}".format(sim.x, sim.delta_x, sim.y, sim.delta_y))
    print()




print('bug ran for {0:.1f} seconds'.format(sim_time))
