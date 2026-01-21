'''
shortest anything on graph is best to use itertive BFS 
'''

from collections import deque

def shortest_path(edges, node_A, node_B):
  graph = create_adj_list(edges)
  visited = set([node_A])
  q = deque([(node_A, 0)])

  while q:
    node, distance = q.popleft()
    if node == node_B: return distance
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        q.append((neighbor, distance + 1))

  return -1

def create_adj_list(edges):
  graph = {}

  for edge in edges:
    a,b = edge

    # if the elements arent in the graph add them 
    if a not in graph: graph[a] = []
    if b not in graph: graph[b] = []

    graph[a].append(b)
    graph[b].append(a)

  return graph
      
   
    

  