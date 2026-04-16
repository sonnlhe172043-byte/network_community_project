from src.graph_loader import load_graph
from src.louvain import louvain
from src.pagerank import pagerank
from src.metrics import compute_modularity

from experiments.runtime import runtime_comparison
from experiments.compare import compare_methods

from visualization.plot import draw_graph



def run_dataset(name, path):

    print(f"\n===== DATASET: {name} =====")

    graph = load_graph(path)
    edges = sum(len(graph[u]) for u in graph) // 2
    communities = louvain(graph)
    pr = pagerank(graph)
    Q = compute_modularity(graph, communities)

    print("Modularity:", round(Q, 4))
    print("Nodes:", len(graph))
    print("Edges:", edges)
    print("Communities:", len(set(communities.values())))

    draw_graph(graph, communities, name)


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