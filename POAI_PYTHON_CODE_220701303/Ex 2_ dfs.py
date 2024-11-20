import networkx as nx

def solveDFS(graph, v, visited):
    visited.add(v)
    print(v, end=' ')
    for neighbour in graph[v]:
        if neighbour not in visited:
            solveDFS(graph, neighbour, visited)

g = nx.DiGraph()
g.add_edges_from([('A', 'B'), ('A', 'C'), ('C', 'G'), ('B', 'D'), ('B', 'E'), ('D', 'F'), ('A', 'E')])
nx.draw(g, with_labels=True)
print("Following is DFS from (starting from vertex A)")
visited = set()
solveDFS(g, 'A', visited)
