import random

# Function to perform crossover operation
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    print(f"Crossover point {crossover_point}")
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Function to convert binary string to integer
def binary_to_int(binary_str):
    return int(binary_str, 2)


# Function to initialize population
def initialize_population(population_size, chromosome_length):
    population = []
    for _ in range(population_size):
        chromosome = ''.join([random.choice(['0', '1']) for _ in range(chromosome_length)])
        population.append(chromosome)
    return population

# Function to perform 1 iteration of genetic algorithm
def perform_iteration(population, crossover_rate):
    new_population = []
    for i in range(0, len(population), 2):
        parent1 = population[i]
        parent2 = population[i + 1] if i + 1 < len(population) else population[0]  # Wrap around to the first chromosome if population size is odd
        print(f"Parents are {parent1} i.e {binary_to_int(parent1)} and {parent2} i.e {binary_to_int(parent2)}")
        print("Post cross-over")
        a_random_no = random.random()
        print(a_random_no)
        if a_random_no < crossover_rate:
            child1, child2 = crossover(parent1, parent2)
            print(child1, child2)
            new_population.extend([child1, child2])
        else:
            new_population.extend([parent1, parent2])
            print(parent1, parent2)
    return new_population

# Main function
if __name__ == "__main__":
    population_size = 6
    chromosome_length = 8
    crossover_rate = 0.25
    
    # Initialize population
    population = initialize_population(population_size, chromosome_length)
    print("Initial Population:")
    for chromosome in population:
        print(chromosome, binary_to_int(chromosome))
    
    # Perform 1 iteration of genetic algorithm
    population = perform_iteration(population, crossover_rate)
    print("\nAfter 1 Iteration:")
    for chromosome in population:
        print(chromosome,binary_to_int(chromosome))
