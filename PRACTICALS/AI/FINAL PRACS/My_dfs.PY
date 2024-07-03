def DFS(root, target, stack):
    path=[]
    while len(stack) != 0:
        current_node = stack.pop()
        path.append(current_node)
        if current_node[0] == target:
            print("Found goal")
            print(path)
            break
        else:
            children = Tree[current_node]
            stack.extend(children)
        print(stack)


Tree = {
    "A": ['C', 'B'],
    "B": ['E', 'D'],
    "C": ['G', 'F'],
    "D": ['H'],
    "E": ['I'],
    "G": ['J'],
    "F": [],
    "H": [],
    "I": [],
    "J": [],
}

# Tree = {
#     # "S": ['D', 'A'],
#     "A": ['B'],
#     "B": ['G1', 'C'],
#     "C": ['G2'],
#     "D": ['G3'],
#     "G1": [],
#     "G2": [],
#     "G3": ['Z'],
# }

# Tree={}
# print("Enter no. for multiple nodes of same name(Eg. G1,G2)")
# no_of_nodes = int(input("Enter total number of nodes: "))
# for n  in range(no_of_nodes):
#     x = input("Node: ")
#     Tree[x]=[]
# print(Tree)

# for node in Tree:
#     print(f'For node {node}')
#     noc = int(input("Number of children: "))
#     for _ in range(noc):
#         c = input('Child: ')
#         Tree[node].append(c)

print("The Tree structure is:{Parent:children}")
print(Tree)

root_node = input("Enter Root Node: ")
goal_node = input("Enter Goal Node: ")
stack=[root_node]
DFS(root_node, goal_node, stack)
