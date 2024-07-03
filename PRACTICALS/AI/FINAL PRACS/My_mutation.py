import random

# Function to perform crossover operation
def mutation(population,no_of_mutations,total_gen):
    # Merge all chromosomes into one long string
    print("The muted genes are:")
    merged_population = ''.join(population)
    
    # Perform mutations
    for _ in range(no_of_mutations):
        # Generate a random index for mutation
        mutation_index = random.randint(0, total_gen - 1)
        print(mutation_index)
        # Replace the character at mutation_index with 0 or 1
        muted_gene =random.choice(['0', '1'])
        print(f'{merged_population[mutation_index]} is replaced with {muted_gene} ')
        merged_population = merged_population[:mutation_index] + muted_gene + merged_population[mutation_index + 1:]
        
    
    # Split the merged string back into separate chromosomes
    # new_population = [merged_population[i:i+len(population[0])] for i in range(0, len(merged_population), len(population[0]))]
    new_population = []
    for i in range(0,total_gen,8):
        chromo=merged_population[i:i+8]
        new_population.append(chromo)
    print(new_population)
    return new_population

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
def perform_iteration(population,chromosome_length, mutation_rate):
    new_population = []
    total_gen=len(population)*chromosome_length
    no_of_mutations=round(mutation_rate*total_gen)
    print(f"Of of the {total_gen} genes, {no_of_mutations} will be mutated")
    # Perform mutation
    new_population = mutation(population, no_of_mutations, total_gen)

    return new_population


# Main function
if __name__ == "__main__":
    population_size = 6
    chromosome_length = 8
    mutation_rate = 0.10
    
    # Initialize population
    population = initialize_population(population_size, chromosome_length)
    print("Initial Population:")
    for chromosome in population:
        print(chromosome, binary_to_int(chromosome))
    
    # Perform 1 iteration of genetic algorithm
    population = perform_iteration(population, chromosome_length,mutation_rate)
    print("\nAfter 1 Iteration:")
    for chromosome in population:
        print(chromosome,binary_to_int(chromosome))
