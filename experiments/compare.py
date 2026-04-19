from src.graph_loader import load_graph
from src.pagerank import pagerank
from src.sir import simulate_sir
from src.centrality import compute_centralities
from src.utils import to_networkx
import networkx as nx
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

        # Degree (có thể normalize nếu muốn)
        degree = {node: len(graph[node]) for node in graph}

        # ===== BETWENNESS =====
        if name == "Karate":
            # full
            _, bet_cent, _ = compute_centralities(graph)

        elif name == "HepTh":
            # approx
            G = to_networkx(graph)
            bet_cent = nx.betweenness_centrality(G, k=100)

        else:
            # skip
            bet_cent = None

        nodes = list(graph.keys())

        # ===== PARAMS =====
        if name == "Karate":
            beta, gamma, steps = 0.1, 0.3, 20
            top_k = 3

        elif name == "HepTh":
            beta, gamma, steps = 0.04, 0.25, 30
            top_k = 5

        else:
            beta, gamma, steps = 0.02, 0.4, 25
            top_k = 3

        # ===== TOP-K =====
        top_pr = sorted(pr, key=pr.get, reverse=True)[:top_k]

        top_deg_full = sorted(degree, key=degree.get, reverse=True)
        top_deg = [n for n in top_deg_full if n not in top_pr][:top_k]

        if bet_cent:
            top_bet_full = sorted(bet_cent, key=bet_cent.get, reverse=True)
            top_bet = [n for n in top_bet_full if n not in top_pr][:top_k]
        else:
            top_bet = None

        print("\nTop PageRank:", top_pr)
        print("Top Degree:", top_deg)
        if top_bet:
            print("Top Betweenness:", top_bet)

        # ===== SIR =====
        def avg_spread(seeds, runs=20):
            total = 0
            for i in range(runs):
                random.seed(42 + i)
                total += simulate_sir(graph, seeds, beta, gamma, steps)
            return total / runs

        def avg_spread_random(runs=20):
            total = 0
            for i in range(runs):
                random.seed(100 + i)
                seeds = random.sample(nodes, top_k)
                total += simulate_sir(graph, seeds, beta, gamma, steps)
            return total / runs

        spread_pr = avg_spread(top_pr)
        spread_deg = avg_spread(top_deg)

        if top_bet:
            spread_bet = avg_spread(top_bet)
        else:
            spread_bet = None

        spread_rand = avg_spread_random()

        print("\n===== SIR Evaluation =====")
        print(f"PageRank:    {spread_pr:.2f}")
        print(f"Degree:      {spread_deg:.2f}")

        if spread_bet is not None:
            print(f"Betweenness: {spread_bet:.2f}")

        print(f"Random:      {spread_rand:.2f}")