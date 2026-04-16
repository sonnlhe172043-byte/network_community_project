from src.utils import to_networkx
import networkx as nx

def compute_centralities(graph):

    G = to_networkx(graph)

    return (
        nx.degree_centrality(G),
        nx.betweenness_centrality(G),
        nx.closeness_centrality(G)
    )