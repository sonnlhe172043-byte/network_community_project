from src.graph_loader import load_graph
from src.louvain import louvain
from src.pagerank import pagerank
from src.metrics import compute_modularity
from src.girvan_newman import girvan_newman_communities
from src.sir import sir_for_visualization

from experiments.runtime import runtime_comparison
from experiments.compare import compare_methods

from visualization.plot import draw_graph


def run_dataset(name, path):
    print(f"\n===== DATASET: {name} =====")

    graph = load_graph(path)
    edges = sum(len(graph[u]) for u in graph) // 2

    # ===== Louvain =====
    communities_louvain = louvain(graph)
    Q_louvain = compute_modularity(graph, communities_louvain)

    print("Nodes:", len(graph))
    print("Edges:", edges)
    print("Communities (Louvain):", len(set(communities_louvain.values())))
    print("Modularity (Louvain):", round(Q_louvain, 4))

    # ===== Girvan-Newman =====
    if name == "Karate":
        communities_gn = girvan_newman_communities(graph, depth=2)
        Q_gn = compute_modularity(graph, communities_gn)

        print("Communities (GN):", len(set(communities_gn.values())))
        print("Modularity (Girvan-Newman):", round(Q_gn, 4))

    # ===== PageRank =====
    pr = pagerank(graph)

    # ===== Visualization =====

    # Louvain
    draw_graph(graph, method="louvain", values=communities_louvain, name=name)

    # PageRank
    draw_graph(graph, method="pagerank", values=pr, name=name)

    # ===== SIR =====
    if name in ["Karate", "HepTh"]:

        #  (PageRank highest)
        seed = max(pr, key=pr.get)

        sir_state = sir_for_visualization(graph, seeds=[seed])

        # Karate → full
        if name == "Karate":
            draw_graph(graph, method="sir", values=sir_state, name=name)

        # HepTh →  subgraph
        elif name == "HepTh":
            draw_graph(
                graph,
                method="sir",
                values=sir_state,
                name=name,
                use_subgraph=True,
                center=seed,
                radius=2
            )


def main():

    datasets = [
        ("Karate", "data/test.txt"),
        ("HepTh", "data/CA-HepTh.txt"),
        ("AstroPh", "data/CA-AstroPh.txt"),
    ]

    for name, path in datasets:
        run_dataset(name, path)

    print("\n===== COMPARISON =====")
    compare_methods()

    print("\n===== RUNTIME =====")
    runtime_comparison()


if __name__ == "__main__":
    main()