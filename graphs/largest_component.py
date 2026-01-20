

def largest_component(graph):
  visited = set()
  largest_component_count = 0

  for node in graph:
    largest_component_count = max(dfs_explore(graph, node, visited),largest_component_count)
  
  return largest_component_count # todo


def dfs_explore(graph, current, visited):
  if current in visited: return 0
  # add 1 bc it represents the node we are on rn 
  count = 1
  visited.add(current)

  # keeps adding on 1 to the count
  for node in graph[current]:
       count += dfs_explore(graph, node, visited)
  return count

  