import networkx as nx

def to_networkx(graph):
    G = nx.Graph()
    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)
    return G