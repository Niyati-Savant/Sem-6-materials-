
import heapq

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]  # (total_cost, node)
    parent = {}  # Dictionary to store the parent node of each visited node
    
    while priority_queue:
        total_cost, current_node = heapq.heappop(priority_queue)
        
        if current_node[0] == goal:
            path = [goal]
            while path[-1] != start:
                path.append(parent[path[-1]])
            return path[::-1]
        
        if current_node not in visited:
            visited.add(current_node)
            for neighbor, neighbor_cost in graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (total_cost + neighbor_cost, neighbor))
                    parent[neighbor] = current_node
    
    return None  # No path found

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('C', 3), ('D', 2)],
    'B': [('G1', 5)],
    'C': [('E', 5)],
    'D': [('F', 4),('G2', 3)],
    'E': [('G3', 5)],
    'F': [],
    'G1': [],
    'G2': [],
    'G3': [],
}

start_node = 'A'
goal_node = 'G'
path = uniform_cost_search(graph, start_node, goal_node)
if path:
    print("Shortest path:", path)
    total_cost = sum(graph[node][i][1] for i, node in enumerate(path[:-1]))
    print("Total cost:", total_cost)
else:
    print("No path found")




