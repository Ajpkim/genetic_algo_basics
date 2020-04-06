import random
import string


def simulation(goal, n, growth_rate, mutation_rate, generations):
    """
    XYZ
    """

    fitness_evaluator = FitnessEvaluator(goal)
    population = StringPopulation(n, len(goal), growth_rate, mutation_rate, fitness_evaluator)
    beginning_strings = [s.content for s in population.strings]  # for printing later

    all_time_top_score = 0
    all_time_most_fit = ''
    generation = 0

    for i in range(generations):
        generation += 1
        population.update()
        most_fit, top_score = population.report_most_fit()
        print('{}      fitness score: {}, gen: {}'.format(
            most_fit, round(top_score/len(goal), 3), generation))

        if top_score > all_time_top_score:
            all_time_most_fit = most_fit

        if most_fit == goal:
            print('')
            print('THE STRINGS HAVE REACHED THE GOAL:', goal)
            print('generation:', generation)
            return

    current_most_fit, current_top_score = population.report_most_fit()
    print('')
    print("Simulation is over. No string reached the goal: {}".format(goal))
    print("Most fit string currently: {}. All time most fit: {}.".format(
        current_most_fit, all_time_most_fit))

    # prints for looking at evolution from start to finish
    # print('')
    # print('beginning strings:')
    # for s in beginning_strings:
    #     print(s)
    # print('')
    # print('current strings:')
    # for s in population.strings:
    #     print(s.content)


class Phrase():
    """
    XYZ
    """

    def __init__(self, content, mutatation_rate):
        self.content = content
        self.mutatation_rate = mutatation_rate
        self.fitness_score = 0
        self.selection_prob = 0

    def mutate(self):
        if random.random() < self.mutatation_rate:
            mutation_index = random.randint(0, len(self.content) - 1)
            mutatation = random.choice(string.ascii_lowercase + ' ')
            self.content = self.content[0:mutation_index] + mutatation + \
                self.content[mutation_index:len(self.content)]

    def __repr__(self):
        return "Phrase object: {}.".format(self.content)


class StringPopulation():
    def __init__(self, n, length, growth_rate, mutatation_rate, FitnessEvaluator):
        self.strings = [Phrase(''.join(random.choices(string.ascii_lowercase + ' ',
                                                      k=length)), mutatation_rate) for i in range(n)]
        self.length = length
        self.growth_rate = growth_rate
        self.fitness_evaluator = FitnessEvaluator
        # initialize string fitness_score, selection_prob variables
        self.evaluate_strings()

    def update(self):
        self.evaluate_strings()
        parents = self.choose_parents()
        new_phrases = self.crossover(parents)
        self.mutate()
        self.strings.clear()
        self.strings = new_phrases

    def evaluate_strings(self):
        for phrase in self.strings:
            self.fitness_evaluator.assign_fitness_score(phrase)
            self.fitness_evaluator.assign_selection_prob(phrase)

    def choose_parents(self):
        parents = []

        while len(parents) < len(self.strings):
            s = random.choice(self.strings)
            if random.random() < s.selection_prob:
                parents.append(s)

        return parents

    def crossover(self, parents):
        new_phrases = []
        while len(new_phrases) < len(self.strings):  # * self.growth_rate:

            p1 = random.choice(parents)
            p2 = random.choice(parents)
            while p2 == p1:
                p2 = random.choice(parents)

            split_index = random.randint(0, len(p1.content)-1)

            string_a = p1.content[0:split_index] + \
                p2.content[split_index:len(p1.content)]
            string_b = p2.content[0:split_index] + \
                p1.content[split_index:len(p1.content)]

            offspring_a = Phrase(string_a, p1.mutatation_rate)
            offspring_b = Phrase(string_b, p2.mutatation_rate)

            new_phrases.append(offspring_a)
            new_phrases.append(offspring_b)

        return new_phrases

    def mutate(self):
        for s in self.strings:
            s.mutate()

    def report_most_fit(self):

        self.evaluate_strings()
        most_fit = ''
        top_score = 0

        for phrase in self.strings:
            if phrase.fitness_score > top_score:
                top_score = phrase.fitness_score
                most_fit = phrase.content

        return most_fit, top_score


class FitnessEvaluator():
    def __init__(self, goal):
        self.goal = goal
        self.max_score = len(goal)

    def assign_fitness_score(self, phrase):
        "Assign fitness score to phrase based on similarity to goal statement"
        score = 0
        for i in range(len(self.goal)):
            if phrase.content[i] == self.goal[i]:
                score += 1
        phrase.fitness_score = score

    def assign_selection_prob(self, phrase):
        "Return selection prob that is proportionally to fitness score"
        phrase.selection_prob = float(phrase.fitness_score / self.max_score)

    def __repr__(self):
        return 'FitnessEvaluator object. Goal: {}'.format(self.goal)


if __name__ == '__main__':
    pass
