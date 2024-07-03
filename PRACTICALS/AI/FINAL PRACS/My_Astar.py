from heapq import heappop, heappush 
def astar_search(graph, start, goal, heuristic): 
    open_list = [(heuristic[start], 0, start)] # Priority queue (f-value, cost, node)
    closed_list = []
    path = {} 
    explored_node = None
    while open_list: 
        _,cost, current_node = heappop(open_list) 
        if current_node == goal: 
            print("Goal reached!") 
            final_path = construct_path(path, start, goal)
            total_cost = calculate_cost(final_path, graph)
            print("Final Path:", final_path) 
            print("Total Cost:", total_cost)
            return
        closed_list.append(current_node) 
        for neighbor, edge_cost in graph.get(current_node, []): 
            if neighbor not in closed_list: 
                new_cost = cost + edge_cost
                f_value = new_cost + heuristic[neighbor]

                if neighbor not in path or new_cost < path[neighbor][1]: 
                    path[neighbor] = (current_node, new_cost)
                    heappush(open_list, (f_value, new_cost, neighbor)) 
        explored_node = current_node 
        print("Open List:", open_list) 
        print("Closed List:", closed_list) 
        print("Current Explored Node:", explored_node) 
        print("Path:", construct_path(path, start, explored_node)) 
        print("-----------------------") 
    print("Goal not found!") 


def construct_path(path, start, goal): 
    result = [goal] 
    current = goal 
    while current != start: 
        current = path[current][0] 
        result.append(current) 
    result.reverse() 
    return result 

def calculate_cost(path, graph):
    total_cost = 0
    for i in range(len(path)-1):
        node = path[i]
        next_node = path[i+1]
        for neighbor, cost in graph[node]:
            if neighbor == next_node:
                total_cost += cost
    return total_cost


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
print("A* Search") 
astar_search(graph, start_node, goal_node, heuristic)