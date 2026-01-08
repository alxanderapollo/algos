#  Basic DFS pattern Itertive and recurisve

def dfs(graph, start):
    stack = [start]
    while stack: 
        top_element = stack[-1]
        print(top_element)
        stack.pop()
        # iterate through the neighbors and push them back into the adjacency list
        for neighbor in graph[top_element]:
            stack.append(neighbor)


def dfs_recursive(graph, start):
    print(start)
    for neighbor in graph[start]:
        dfs_recursive(graph, neighbor)
        

# breadth first 
from collections import deque 
def bfs(graph, start): 
    q = deque([start])
    while q:
        current_node = q[0]
        print(current_node)
        q.popleft()
        for neighbor in graph[current_node]:
            q.append(neighbor)




graph = {
  "a": ["b", "c"],
  "b": ["d"],
  "c": ["e"],
  "d": ["f"],
  "e": [],
  "f": []
}

# dfs(graph, "a")
# dfs_recursive(graph, "a")
bfs(graph, "a")