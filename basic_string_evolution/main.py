from basic_string_evolution import *

goal = 'evolution is pretty lit'
n = 1000
growth_rate = 1
mutation_rate = .03
generations = 100


# fix growth growth_rate stuff
# make plots showing impact of mutation rate, growth rate, generations, and starting pop size

def main(goal, n, growth_rate, mutation_rate, generations):
    simulation(goal, n, growth_rate, mutation_rate, generations)


if __name__ == '__main__':
    main(goal, n, growth_rate, mutation_rate, generations)
