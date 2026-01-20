'''
return the # of connected components in the graph 

Strategy

1. visited set to keep track of whats been seen 
2. DFS on each connected component- if we have seen it pass up False otherwise true to add 1+ to the counter
3. return the count of each component


'''

def connected_components_count(graph):
  visited = set()
  connected_component_count = 0
  # explore each node to see what node belongs to what components
  for node in graph:
    if dfs_search(graph, node, visited): connected_component_count +=1
  return connected_component_count

def dfs_search(graph, current, visited):
  # if we have seen the node before return false
  if current in visited: return False 
  visited.add(current)
  
  for node in graph[current]:
    dfs_search(graph, node, visited)

  # pass up true to count the new component
  return True
  