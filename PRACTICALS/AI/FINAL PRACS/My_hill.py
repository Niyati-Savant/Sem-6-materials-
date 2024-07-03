import random
import math
def objectiveFunction(x):
    # return (-5*(x**2)+3*x+6)
    return math.sin(x) # -5*(x**2)+3*x+6
   
def generateNeighbors(solution):
    neighbors = []
    for delta in [-1, 1]: #left or right
        neighbors.append(solution + delta)
    return neighbors
def getBestNeighbor(neighbors):
    bestNeighbor = neighbors[0]
    bestQuality = objectiveFunction(bestNeighbor)
    for neighbor in neighbors:
        neighborQuality = objectiveFunction(neighbor)
        if neighborQuality >= bestQuality:
            bestQuality = neighborQuality
            bestNeighbor = neighbor 
    print(bestNeighbor,bestQuality)
    return bestNeighbor
def hill():
    currSolution = random.randint(-10, 10)
    print(currSolution,objectiveFunction(currSolution) )
    while True:
        neighbors = generateNeighbors(currSolution)
        bestNeighbors = getBestNeighbor(neighbors)
        if objectiveFunction(bestNeighbors) <= objectiveFunction(currSolution):
            print(objectiveFunction(currSolution))
            return currSolution
        currSolution = bestNeighbors

bestSolution = hill()
if bestSolution:
    print("Best Solution Found!")
else:
    print("Best Solution Not Found!")
print("Objective Function Value: ", objectiveFunction(bestSolution))

# import random
# import math

# def objectiveFunction(x):
#     # return (-5*(x**2)+3*x+6)
#     return(-(x**2))
#     # return math.sin(x)

# def generateNeighbors(solution):
#     neighbors = []
#     for delta in [-1, 1]: #left or right
#         neighbors.append(solution + delta)
#     return neighbors

# def getBestNeighbor(neighbors):
#     bestNeighbor = neighbors[0]
#     bestQuality = objectiveFunction(bestNeighbor)
#     for neighbor in neighbors:
#         neighborQuality = objectiveFunction(neighbor)
#         if neighborQuality >= bestQuality:
#             bestQuality = neighborQuality
#             bestNeighbor = neighbor 
#     print(bestNeighbor,bestQuality)
#     return bestNeighbor

# def hill():
#     currSolution = random.randint(-10, 10)
#     print(currSolution)
#     while True:
#         neighbors = generateNeighbors(currSolution)
#         bestNeighbors = getBestNeighbor(neighbors)
#         if objectiveFunction(bestNeighbors) >= objectiveFunction(currSolution):
#             print(objectiveFunction(currSolution))
#             return currSolution
#         currSolution = bestNeighbors

# bestSolution = hill()
# if bestSolution:
#     print("Best Solution Found!")
# else:
#     print("Best Solution Not Found!")
# print("Objective Function Value: ", objectiveFunction(bestSolution))
