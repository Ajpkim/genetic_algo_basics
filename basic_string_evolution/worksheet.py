from basic_string_evolution import *

goal = 'evolution is lit'
n = 50
growth_rate = 1
mutation_rate = .05
generations = 10

fitev = FitnessEvaluator(goal)
pop = StringPopulation(n, len(goal), growth_rate, mutation_rate, fitev)

for s in pop.strings:
    print(s.contents)

print("")
pop.update()
for s in pop.strings:
    print(s.contents)


# for p in pop.phrases:
#     print(p.contents)
#     print(p.fitness_score)
#
# pop.update()
# for p in pop.phrases:
#     print(p.contents)
#     print(p.fitness_score)


# a = 'abc'
# b = a[0:2]
# print(b)

# fe = FitnessEvaluator(goal)
# print(fe)
#
# s = Phrase('evolution mm mmm', .01)
# print(s)
# print(s.fitness_score)
# fe.assign_fitness_score(s)
# print(s.fitness_score)

# pop = population

# a = [1, 2]
# b = 5
# for i in range(5):
#     a.append(b)
# print(a)
# a.append(9)
# a.append(b)
# print(a)
# a.remove(b)
# print(a)


# def evaluate(self, FitnessEvaluator):
#     FitnessEvaluator.assign_fitness_score(self)
#     FitnessEvaluator.assign_selection_prob(self)

#
# length = 10
# n = 5
# # s = ''
# s = [''.join(random.choices(string.ascii_lowercase, k=length)) for i in range(n)]
# print(s)
# s = s.join(random.choice(string.ascii_lowercase))
#
# print(s)
# for i in range(length):
#     s = s.join(random.choice(string.ascii_lowercase))
# s = ''.join(random.choice(string.ascii_lowercase) for i in range(length)
# s = [[''.join(random.choice(string.ascii_lowercase) for i in range(length)] for j in range(n)]


# for i in range(10):
# print(1+1)
# print(s)
# print(string.ascii_letters)
# s = 'abc'
# s = s.join('def')
# print(s)
