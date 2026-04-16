from src.graph_loader import load_graph
from src.pagerank import pagerank
from src.sir import simulate_sir
import random


def compare_methods():

    datasets = [
        ("Karate", "data/test.txt"),
        ("HepTh", "data/CA-HepTh.txt"),
        ("AstroPh", "data/CA-AstroPh.txt")
    ]

    print("\n===== METHOD COMPARISON =====")

    for name, path in datasets:

        print(f"\n--- Dataset: {name} ---")

        graph = load_graph(path)
        pr = pagerank(graph)

        # Degree centrality
        degree = {node: len(graph[node]) for node in graph}

        nodes = list(graph.keys())

        # 🔥 PARAMETER THEO DATASET
        if name == "Karate":
            beta, gamma, steps = 0.1, 0.3, 20
            top_k = 3

        elif name == "HepTh":
            beta, gamma, steps = 0.04, 0.25, 30
            top_k = 5

        else:  # AstroPh
            beta, gamma, steps = 0.02, 0.4, 25
            top_k = 3   # 🔥 giảm để tránh random may mắn

        # Top-k selection
        top_pr = sorted(pr, key=pr.get, reverse=True)[:top_k]

        top_deg_full = sorted(degree, key=degree.get, reverse=True)
        # No overlap với PageRank
        top_deg = [n for n in top_deg_full if n not in top_pr][:top_k]

        # Random
        random.seed(42)
        top_rand = random.sample(nodes, top_k)

        print("\nTop PageRank:", top_pr)
        print("Top Degree:", top_deg)

        # 🔥 Multi-run SIR
        def avg_spread(seeds, runs=20):

            total = 0

            for i in range(runs):
                random.seed(42 + i)
                total += simulate_sir(graph, seeds, beta, gamma, steps)

            return total / runs

        spread_pr = avg_spread(top_pr)
        spread_deg = avg_spread(top_deg)
        spread_rand = avg_spread(top_rand)

        print("\n===== SIR Evaluation =====")
        print(f"PageRank: {spread_pr:.2f}")
        print(f"Degree:   {spread_deg:.2f}")
        print(f"Random:   {spread_rand:.2f}")