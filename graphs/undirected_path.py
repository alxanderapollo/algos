'''
undirected path
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.


test 0
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'j', 'm') # -> True


test 1 
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'm', 'j') # -> True

test 2 
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'l', 'j') # -> True

test 3 
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'k', 'o') # -> False

test 4
edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

undirected_path(edges, 'i', 'o') # -> False


test 5 
edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]


undirected_path(edges, 'a', 'b') # -> True

'''


def undirected_path(edges, node_A, node_B):
  graph = reconvert_into_adj_list(edges)

  visited = set()
  if search_path(graph, node_A, node_B, visited) == True: 
    return True
  else: 
    return False 
  
def search_path(graph, start, dst, visited):
  if start == dst: return True
  if start in visited: return False
  
  visited.add(start)
  for neighbor in graph[start]:
    if search_path(graph, neighbor, dst, visited) == True: 
      return True 

      
# we need to convert back into an adj list
def reconvert_into_adj_list(edges): 

  graph = {}
  for edge in edges:
    a,b = edge
    if a not in graph: graph[a] = []
    if b not in graph: graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

  return graph