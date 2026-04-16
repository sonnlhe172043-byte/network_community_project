from src.utils import to_networkx
from networkx.algorithms.community import louvain_communities

def louvain(graph):

    G = to_networkx(graph)

    communities = louvain_communities(G)

    node_comm = {}
    for i, comm in enumerate(communities):
        for node in comm:
            node_comm[node] = i

    return node_comm