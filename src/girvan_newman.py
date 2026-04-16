import networkx as nx
from networkx.algorithms.community import girvan_newman


def girvan_newman_communities(graph, depth=1):

    G = nx.Graph()

    for u in graph:
        for v in graph[u]:
            G.add_edge(u, v)

    comp = girvan_newman(G)

    communities = None

    for _ in range(depth):
        communities = next(comp)

    node_comm = {}

    for i, comm in enumerate(communities):
        for node in comm:
            node_comm[node] = i

    return node_comm