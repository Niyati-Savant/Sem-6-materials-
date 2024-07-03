import heapq


class Node:
    def __init__(self, name, cost=0, parent=None):
        self.name = name
        self.cost = cost
        self.parent = parent
        self.priority = 0

    def __lt__(self, other):
        return self.priority < other.priority


def heuristic(node, goal, heuristic_map):
    return heuristic_map.get(node.name, 0)


def a_star_search(start, goal, graph, heuristic_map):
    open_list = []
    heapq.heappush(open_list, (0, Node(start)))
    visited = set()

    while open_list:
        _, current_node = heapq.heappop(open_list)

        if current_node.name in visited:
            continue
        visited.add(current_node.name)

        if current_node.name == goal:
            path = []
            while current_node:
                path.append((current_node.name, current_node.priority))  # Include priority in the result
                current_node = current_node.parent
            return path[::-1]

        for neighbor, cost in graph[current_node.name].items():
            if neighbor not in visited:
                neighbor_node = Node(neighbor, current_node.cost + cost, current_node)
                neighbor_node.priority = neighbor_node.cost + heuristic(neighbor_node, goal, heuristic_map)
                heapq.heappush(open_list, (neighbor_node.priority, neighbor_node))

    return None



# Graph data
graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Bucharest': {'Urziceni': 85, 'Pitesti': 101, 'Giurgiu': 90, 'Fagaras': 211},
    'Craiova': {'Drobeta': 120, 'Rimnicu': 146, 'Pitesti': 138},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Neamt': {'Iasi': 87},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 146},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Zerind': {'Arad': 75, 'Oradea': 71}
}

# Heuristic values
heuristic_map = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# Run A* search algorithm

cities = [
    "Arad",
    "Bucharest",
    "Craiova",
    "Dobreta",
    "Eforie",
    "Fagaras",
    "Giurgiu",
    "Hirsova",
    "Iasi",
    "Lugoj",
    "Mehadia",
    "Neamt",
    "Oradea",
    "Pitesti",
    "Rimnicu_Vilcea",
    "Sibiu",
    "Timisoara",
    "Urziceni",
    "Vaslui",
    "Zerind"
]

print("Niyati's Code for A* algorithm")
for i in range(len(cities)):
    print(f"{i}. {cities[i]}")
start_city = int(input("Enter no. for  Start City: "))
start_city = cities[start_city]

goal_city = int(input("Enter no. Goal City: "))
goal_city = cities[goal_city]

path = a_star_search(start_city, goal_city, graph, heuristic_map)

print(f"Path from {start_city} to {goal_city}:", path)
