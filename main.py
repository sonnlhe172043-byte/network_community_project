from src.graph_loader import load_graph
from src.louvain import louvain
from src.pagerank import pagerank
from src.metrics import compute_modularity

from experiments.runtime import runtime_comparison
from experiments.compare import compare_methods

from visualization.plot import draw_graph
from src.girvan_newman import girvan_newman_communities




def run_dataset(name, path):
    print(f"\n===== DATASET: {name} =====")

    graph = load_graph(path)
    edges = sum(len(graph[u]) for u in graph) // 2

    # ===== Louvain =====
    communities_louvain = louvain(graph)
    Q_louvain = compute_modularity(graph, communities_louvain)

    print("Modularity (Louvain):", round(Q_louvain, 4))
    print("Nodes:", len(graph))
    print("Edges:", edges)
    print("Communities (Louvain):", len(set(communities_louvain.values())))

    # ===== Girvan-Newman =====
    #
    if name == "Karate":
        communities_gn = girvan_newman_communities(graph, depth=2)
        Q_gn = compute_modularity(graph, communities_gn)

        print("Modularity (Girvan-Newman):", round(Q_gn, 4))
        print("Communities (GN):", len(set(communities_gn.values())))

    # ===== Visualization =====
    #draw_graph(graph, communities_louvain, name)


def main():

    datasets = [
        ("Karate", "data/test.txt"),
        ("HepTh", "data/CA-HepTh.txt"),
        ("AstroPh", "data/CA-AstroPh.txt"),
    ]

    for name, path in datasets:
        run_dataset(name, path)

    compare_methods()
    runtime_comparison()


if __name__ == "__main__":
    main()