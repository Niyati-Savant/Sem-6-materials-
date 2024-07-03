from heapq import heappop, heappush 
def greedy_search(graph, start, goal, heuristic): 
    open_list = [(heuristic[start], start)] # Priority queue (heuristic value, node) tuple
    closed_list = []
    path = {} 
    explored_node = None
    while open_list: 
        _, current_node = heappop(open_list) 
        if current_node == goal: 
            print("Goal reached!") 
            print("Final Path:", construct_path(path, start, goal)) 
            return
        closed_list.append(current_node)
        for neighbor, _ in graph.get(current_node, []): 
            print(current_node,path)
            if neighbor not in closed_list and neighbor not in path: 
                path[neighbor] = current_node 
                heappush(open_list, (heuristic[neighbor], neighbor)) 
        explored_node = current_node 

        print("Open List:", open_list) 
        print("Closed List:", closed_list) 
        print("Current Explored Node:", explored_node) 
        print("Path:", construct_path(path, start, explored_node)) 
        print("-----------------------") 
    print("Goal not foUnd!") 

def construct_path(path, start, goal): 
    result = [goal] 
    current = goal 
    while current != start: 
        current = path[current] 
        result.append(current) 
    result.reverse() 
    return result 

graph = { 
'A': [('B', 3), ('C',4)], 
'B': [('D', 4), ('C', 5),('A',3)], 
'C': [('A', 4), ('B',5), ('E',2)], 
'D': [('B', 4), ('E', 5), ('F',4)], 
'E':[('C', 2), ('D', 5), ('G',4)], 
'F': [('D', 4)], 
'G': [('H', 3), ('E', 4)],
'H':[('G', 3)], 
}

heuristic = {
'A': 15,
'B': 14,
'C': 12,
'D': 10,
'E': 10,
'F': 8,
'G':10,
'H':0,
}


start_node, goal_node = input("Enter start and goal nodes separated by a space: ").split() 
print("Greedy Search") 
greedy_search(graph, start_node, goal_node, heuristic)

# graph = { 
# 'A': [('B', 2), ('E', 3)], 
# 'B': [('A',2), ('C', 1), ('G',9)], 
# 'C': [('B', 1)], 
# 'D': [('E',6), ('G', 1)], 
# 'E':[('A',3),('D',6)], 
# 'G':[('B',9), ('D',1)] 
# }
# heuristic = {
# 'A': 11,
# 'B': 6,
# 'C': 99,
# 'D': 1,
# 'E': 7,
# 'G': 0,
# }