# Tree_BFS = {
# "A": ['C', 'B'],
# "B": ['E', 'D'],
# "C": ['G', 'F'],
# "D": ['H'],
# "E": ['J', 'I'],
# "F": ['L', 'K'],
# "G": ['M'],
# "H": [],
# "I": [],
# "J": [],
# "K": [],
# "L": [],
# "M": []
# }
Tree_BFS = {
    "S": ['A', 'D'],
    "A": ['B'],
    "B": ['C', 'G1'],
    "C": ['G2'],
    "D": ['G3'],
    "G1": [],
    "G2": [],
    "G3": ['Z']
}

def BFS(node,goal):
  queue = []
  path=[]
  queue.append(node)
#   path.append(node)
  print(queue)
  while len(queue)!=0:
    node = queue[0]
    if queue[0][0]==goal:
      path.append(queue[0])
      print("The path is :")
      print(path)
      return("Goal node found")
      
    else:
      x=queue.pop(0)
      path.append(x)
      children = Tree_BFS[node]
      queue.extend(children)
      print(queue)
  return("Not exist After exploring all nodes")

root_node = 'S'
goal_node = 'Z'
stack = ['S']
print(BFS(root_node, goal_node))