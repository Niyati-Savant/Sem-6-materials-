import random

# Objective function to be maximized
def objective_function(x):
    return -x ** 2

# Generate initial solution randomly
def generate_initial_solution():
    return random.randint(-100, 100)

# Generate neighbour solutions
def generate_neighbours(solution):
    neighbours = []
    for delta in [-1, 1]:
        neighbours.append(solution + delta)
    return neighbours

# Get highest quality neighbour of current solution
def get_best_neighbour(neighbours):
    best_neighbour = neighbours[0]
    best_quality = objective_function(best_neighbour)
    for neighbour in neighbours[1:]:
        neighbour_quality = objective_function(neighbour)
        if neighbour_quality > best_quality:
            best_quality = neighbour_quality
            best_neighbour = neighbour
    return best_neighbour

# Hill climbing algorithm
def hill_climbing():
    current_solution = generate_initial_solution()
    # print("Initial Solution: ", current_solution)
    while True:
        neighbours = generate_neighbours(current_solution)
        best_neighbour = get_best_neighbour(neighbours)
        if objective_function(best_neighbour) <= objective_function(current_solution):
            return current_solution
        current_solution = best_neighbour


best_solution = hill_climbing()
print("Niyati's Code for Hill Climbing")
print("Best solution found:", best_solution)
print("Objective function value:", objective_function(best_solution))

