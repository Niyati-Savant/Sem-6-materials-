def DLS(current, limit, current_depth, goal, stack):
    current=stack.pop()
    if (current_depth > limit):
        return False
    if current[0] == goal:
        return True
    else:
        children = Tree[current]
        if (current_depth<limit):
            stack.extend(children[::-1])
            print(stack)
            for child in children:
                if DLS(child, limit, (current_depth + 1), goal, stack):
                    return True

def IDDFS(root,goal):
    limit = 0
    found = False
    stack = [root]
    while not found:
        print(f"At depth limit {limit}:")
        print(stack)
        found = DLS(root, limit, 0, goal, stack)
        stack = [root]
        limit += 1
        if limit > total_depth:
            print("NOT Exist")
            break
    if found:
        print(f"Found at depth {limit-1 }")
Tree = {
    "S": ['D', 'A'],
    "A": ['B'],
    "B": ['G1', 'C'],
    "C": ['G2'],
    "D": ['G3'],
    "G1": [],
    "G2": [],
    "G3": ['Z'],
}

root_node ='S'
goal_node = 'Z'
total_depth = 4
IDDFS(root_node,goal_node)