'''
experiment using a continuous-time recurrent neural network (CTRNN).
'''

from __future__ import print_function

import os
import pickle

import neat_bug

import neat
from neat.math_util import mean
import visualize

runs_per_net = 1
simulation_seconds = 10.0
time_step = neat_bug.NeatBug.time_step


# Use the CTRNN network phenotype.
def eval_genome(genome, config):

    #create a new brain
    net = neat.ctrnn.CTRNN.create(genome, config, 1)

    #a store of the fitness for each run for the bug
    fitnesses = []

    #do several simulation runs per bug
    for runs in range(runs_per_net):
        #create a new bug but will use the current net.
        bug = neat_bug.NeatBug()

        #reset the net as if it hadn't run yet due to the recurrent nature of net
        net.reset()

        fitness = 0.0
        # Run the given simulation for up to num_steps time steps.
        # unless there is randomness or variability in the bug, each run will be the same

        #limit each simulation run by time
        while bug.t < simulation_seconds:

            #get the inputs to the net from the sensors
            inputs = bug.get_scaled_state()

            #run the inputs the nets activation collect the outputs (i.e., action)
            action = net.advance(inputs, time_step, time_step)

            # Apply action to the bug
            bug.step(action)

            #update the fitness based on last iteration    
            fitness = bug.fitness()


        #after simulation complete capture the fitness for that run 
        #print("fitness {0}".format(fitness))   
        fitnesses.append(fitness)

 
    # The genome's fitness is its worst performance across all runs.
    #print("fitness {0}".format(min(fitnesses))) 
    return max(fitnesses)


def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = eval_genome(genome, config)


def run():
    # Load the config file, which is assumed to live in
    # the same directory as this script.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-ctrnn')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    pop = neat.Population(config)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.StdOutReporter(True))

    if True:
        winner = pop.run(eval_genomes, 2000)
    else:
        pe = neat.ParallelEvaluator(4, eval_genome)
        winner = pop.run(pe.evaluate, 2000)

    # Save the winner.
    with open('winner-ctrnn', 'wb') as f:
        pickle.dump(winner, f)

    print(winner)

    # visualize.plot_stats(stats, ylog=True, view=True, filename="ctrnn-fitness.svg")
    # visualize.plot_species(stats, view=True, filename="ctrnn-speciation.svg")

    # node_names = {-1: 'dx', -2: 'dy', 0: 'vr', 1: 'vl'}
    # visualize.draw_net(config, winner, True, node_names=node_names)

    # visualize.draw_net(config, winner, view=True, node_names=node_names,
    #                    filename="winner-ctrnn.gv")
    # visualize.draw_net(config, winner, view=True, node_names=node_names,
    #                    filename="winner-ctrnn-enabled.gv", show_disabled=False)
    # visualize.draw_net(config, winner, view=True, node_names=node_names,
    #                    filename="winner-ctrnn-enabled-pruned.gv", show_disabled=False, prune_unused=True)


if __name__ == '__main__':
    run()
