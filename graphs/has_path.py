'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.

Hey. This is our first graph problem, so you should be liberal with watching the Approach and Walkthrough. Be productive, not stubborn. -AZ


test 0
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'k') # True

test 1 
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'f', 'j') # False

test 2 
graph = {
  'f': ['g', 'i'],
  'g': ['h'],
  'h': [],
  'i': ['g', 'k'],
  'j': ['i'],
  'k': []
}

has_path(graph, 'i', 'h') # True

test 3 
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'w') # True

test 4 
graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

has_path(graph, 'v', 'z') # False
'''


# breadth first approach

# from collections import deque 
# def has_path(graph, src, dst):
#   q = deque([src])
#   while q:
#     current_node = q[0]
#     if current_node == dst: 
#       return True
#     # remove the node
#     q.popleft()
#     for neighbor in graph[current_node]:
#       q.append(neighbor)
      
#   return False


# dfs approach 
# def has_path(graph, src, dst):
#   stack = [src]

#   while stack:
#     current_node = stack[-1]
    
#     if current_node == dst: return True

#     stack.pop()
#     for neighbor in graph[current_node]:
#       stack.append(neighbor)

#   return False


def has_path(graph, src, dst):
  if DFS_search(graph, src, dst) == True: return True
  else :  return False


def DFS_search(graph, src, dst):
  if src == dst: return True
  for neighbor in graph[src]:
    if DFS_search(graph, neighbor, dst) == True: return True
    
  
