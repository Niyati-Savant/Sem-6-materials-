import random
def fitness_function(chromosome):
    a,b,c,d=chromosome
    return abs((a+2*b+3*c+4*d)-30)
def initialize_population(population_size):
    population=[]
    for _ in range(population_size):
        chromosome=[random.randint(0, 30) for _ in range(4)]
        population.append(chromosome)
    return population

# Selection: Roulette wheel selection
def roulette_wheel_selection(population):
    total_fitness = sum(fitness_function(chromosome) for chromosome in population)
    selection_point = random.uniform(0, total_fitness)
    cumulative_fitness = 0
    for chromosome in population:
        cumulative_fitness += fitness_function(chromosome)
        if cumulative_fitness >= selection_point:
            return chromosome
        
def crossover(parent1,parent2,crossover_rate):
    if random.random() > crossover_rate:
        return parent1, parent2
    crossover_point=random.randint(1,len(parent1)-1)
    child1=parent1[:crossover_point]+parent2[crossover_point:]
    child2=parent2[:crossover_point]+parent1[crossover_point:]
    return child1, child2

def mutation(child, mutation_rate):
    mutated_child=[]
    for gene in child:
        if random.random()<mutation_rate:
            mutated_gene=random.randint(0,30)
            mutated_child.append(mutated_gene)
        else:
            mutated_child.append(gene)
    return mutated_child
def genetic_algorithm(population_size,crossover_rate,mutation_rate):
    population=initialize_population(population_size)
    print("Initial population:")
    print(population)
    iteration=0
    for generation in range(1000):
        new_population=[]
        iteration+=1
        while len(new_population)< population_size:
            parent1=roulette_wheel_selection(population)
            parent2=roulette_wheel_selection(population)
            child1,child2=crossover(parent1,parent2,crossover_rate)
            child1=mutation(child1,mutation_rate)
            child2=mutation(child2,mutation_rate)
            new_population.extend([child1,child2])
        population=new_population
        best_chromosome=min(population,key=fitness_function)
        if fitness_function(best_chromosome)==0:
            break
    return best_chromosome, iteration
#main
crossover_rate=0.25
mutation_rate=0.1
population_size=6
best_chromosome,iteration=genetic_algorithm(population_size,crossover_rate,mutation_rate)
print("Best chromosome: ",best_chromosome)
print("Iteration: ",iteration)

