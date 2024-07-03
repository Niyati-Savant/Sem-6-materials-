import numpy as np

# Parameters
population_size = 6
gene_length = 4
num_generations = 100
crossover_rate = 0.5
mutation_rate = 0.1
num_parents = int(population_size / 2)

print("Niyati's Code for Genetics algorithm")

# Functions
def initialize_population(size, gene_length):
    return np.random.randint(0, 31, (size, gene_length))

def calculate_fitness(chromosome):
    objective_value = abs(sum([chromosome[i] * (i+1) for i in range(len(chromosome))]) - 30)
    fitness_value = 1 / (1 + objective_value)  # Modified to match the provided logic
    return fitness_value

def select_parents(population, fitness, num_parents):
    fitness_sum = np.sum(fitness)
    probability = fitness / fitness_sum
    chosen = set()  # Set to keep track of which individuals have been chosen
    
    parents = np.empty((num_parents, population.shape[1]))
    for parent_num in range(num_parents):
        rand = np.random.rand()
        cumulative_probability = 0.0
        for i in range(len(probability)):
            if i not in chosen:
                cumulative_probability += probability[i]
                if rand <= cumulative_probability:
                    parents[parent_num, :] = population[i, :]
                    chosen.add(i)  # Mark this individual as chosen
                    break
    return parents


def crossover(parents, offspring_size, crossover_rate):
    offspring = np.empty(offspring_size)
    for k in range(offspring_size[0]):
        if np.random.rand() < crossover_rate:
            parent1_idx = k % parents.shape[0]
            parent2_idx = (k+1) % parents.shape[0]
            crossover_point = np.random.randint(1, offspring_size[1])
            offspring[k, 0:crossover_point] = parents[parent1_idx, 0:crossover_point]
            offspring[k, crossover_point:] = parents[parent2_idx, crossover_point:]
    return offspring

def mutate(offspring_crossover, mutation_rate):
    for idx in range(offspring_crossover.shape[0]):
        for gene in range(offspring_crossover.shape[1]):
            if np.random.rand() < mutation_rate:
                offspring_crossover[idx, gene] = np.random.randint(0, 31)
    return offspring_crossover

# Genetic Algorithm Process with Outputs
population = initialize_population(population_size, gene_length)
print("Initial Population:\n", population)

for generation in range(num_generations):
    fitness = np.array([calculate_fitness(individual) for individual in population])
    print(f"\nGeneration {generation} Fitness:\n", fitness)
    parents = select_parents(population, fitness, num_parents)
    print("Selected Parents:\n", parents)
    offspring_crossover = crossover(parents, (population_size - num_parents, gene_length), crossover_rate)
    print("Crossover Offspring:\n", offspring_crossover)
    offspring_mutation = mutate(offspring_crossover, mutation_rate)
    print("Mutated Offspring:\n", offspring_mutation)
    population[:num_parents, :] = parents
    population[num_parents:, :] = offspring_mutation
    # Break after first generation for example
    break



def genetic_algorithm(population, population_size, gene_length, num_generations, crossover_rate, mutation_rate, num_parents):
    
    for generation in range(num_generations):
        # Calculate fitness for each individual in the population
        fitness = np.array([calculate_fitness(individual) for individual in population])
        # Select parents for mating
        parents = select_parents(population, fitness, num_parents)
        # Generate offspring through crossover
        offspring_crossover = crossover(parents, (population_size - num_parents, gene_length), crossover_rate)
        # Apply mutation to offspring
        offspring_mutation = mutate(offspring_crossover, mutation_rate)
        # Create new population by combining parents and offspring
        population[:num_parents, :] = parents
        population[num_parents:, :] = offspring_mutation
    
    # Identify the best solution at the end of the evolution
    final_fitness = np.array([calculate_fitness(individual) for individual in population])
    best_index = np.argmax(final_fitness)  # Use argmax because we are using inverted fitness values
    best_solution = population[best_index]
    
    # Print the best solution
    print("\nFinal Best Solution:\n", best_solution)
    print("With Fitness Score:", final_fitness[best_index])


# Run the genetic algorithm
genetic_algorithm(population, population_size, gene_length, num_generations, crossover_rate, mutation_rate,num_parents)