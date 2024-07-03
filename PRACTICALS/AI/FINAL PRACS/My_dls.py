def DLS(current, limit, current_depth, goal, stack):
    
    current=stack.pop()
    if (current_depth > limit):
        return False
    if current[0] == goal:
        return True
    else:     
        if (current_depth<limit):
            children = Tree[current]
            stack.extend(children)
            print(stack)
            for child in children:
                if DLS(child, limit, (current_depth + 1), goal, stack):
                    return True

Tree = {
    "S": ['A', 'D'],
    "A": ['B'],
    "B": ['C', 'G1'],
    "C": ['G2'],
    "D": ['G3'],
    "G1": [],
    "G2": [],
    "G3": ['Z'],
}

print("The Tree structure is:{Parent:children}")
print(Tree)

# root_node = input("Enter Root Node: ")
# goal_node = input("Enter Goal Node: ")
# stack=[root_node]
# limit = int(input("Enter depth limit: "))
root_node = 'S'
goal_node = 'Z'
stack=[root_node]
limit = 2
print(stack)
if DLS(root_node, limit, 0, goal_node, stack):
    print("Found within given depth")
else:
    print("Not Found within given depth")
