from deap import algorithms
from deap import base
from deap import creator
from deap import tools
import array
import random
import json
from VASSAR import VASSAR

instruments = ['A','B','C','D','E','F','G','H','I','J','K','L']

def arch_to_array(architecture):
    array = [0] * 60
    arch = json.loads(architecture)
    for j in range(0,5):
        for i in range(0, 12):
            if instruments[i] in arch[j]:
                array[i+j*12] = 1
    return array

def array_to_arch(array):
    arch = '["'
    for j in range(0,5):
        for i in range(0, 12):
            if array[i+j*12] == 1:
                arch += instruments[i]
        if j < 4:
            arch += '","'
    arch += '"]'
    return arch

vassar = VASSAR.VASSAR()

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", array.array, typecode='b', fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool", random.randint, 0, 1)

toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_bool, 60)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evaluate(individual):
    architecture = array_to_arch(individual)
    result = vassar.evaluateArch(architecture)
    return result[0],

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    print "globalExplorer"
    pop = toolbox.population(n=300)
    hof = tools.HallOfFame(1)

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, 
                                ngen=40, halloffame=hof, verbose=True)

    return pop, log, hof

if __name__ == '__main__':
    main()
