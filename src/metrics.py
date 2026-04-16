from src.utils import to_networkx
import networkx as nx

def compute_modularity(graph, communities):

    G = to_networkx(graph)

    comms = {}
    for node, cid in communities.items():
        comms.setdefault(cid, set()).add(node)

    return nx.algorithms.community.modularity(G, comms.values())