# use the graph method to go through a DFS algorithm

graph = {"you":   set(['bob','alice','claire']),
         'bob':   set(['anuj','peggy']),
         'alice': set(['peggy']),
         'claire':set(['thom','jonny']),
         'anuj': set(),
         'peggy': set(),
         'thom' :set(),
         'jonny':set()
         }

figure = list(graph)
for name in figure:
    if "m" in name:
        goal = name
def dfs_path(graph, start,goal,path = None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_path(graph, next, goal,path+[next])
print(list(dfs_path(graph,'you',goal)))

def dfs(graph, start , goal ):
    visited, stack = set(), [start]
    while stack :
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
        if vertex == goal:
            break
    return visited
print(dfs(graph,'you',goal))