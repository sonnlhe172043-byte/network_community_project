from src.utils import to_networkx
import matplotlib.pyplot as plt
import networkx as nx
import os

def draw_graph(graph, method=None, values=None, name="Graph",
               save=True, use_subgraph=False, center=None, radius=2):

    # ===== SKIP LARGE GRAPH =====
    if name not in ["Karate", "HepTh"]:
        print(f"[SKIP] Visualization skipped for {name} (too large)")
        return

    G = to_networkx(graph)
    if use_subgraph and center is not None:
        G = nx.ego_graph(G, center, radius=radius)

    plt.figure(figsize=(8, 6))

    # ===== LAYOUT =====
    if name == "Karate":
        pos = nx.spring_layout(G, seed=42)
        base_size = 80

    else:  # HepTh
        #
        pos = nx.spring_layout(G, seed=42, iterations=15)
        base_size = 10

    # ===== DEFAULT =====
    colors = "blue"
    sizes = base_size

    # ===== LOUVAIN =====
    if method == "louvain" and values:
        colors = [values[node] for node in G.nodes()]

    # ===== PAGERANK =====
    elif method == "pagerank" and values:
        colors = "skyblue"
        # normalize
        max_pr = max(values.values())
        sizes = [values[node] / max_pr * 3000 for node in G.nodes()]

    # ===== SIR =====
    elif method == "sir" and values:
        color_map = {
            "S": "blue",
            "I": "red",
            "R": "gray"
        }
        colors = [color_map.get(values[node], "black") for node in G.nodes()]

    # ===== DRAW =====
    draw_kwargs = dict(
        G=G,
        pos=pos,
        node_color=colors,
        node_size=sizes,
        with_labels=False
    )

    # only cmap when Louvain
    if method == "louvain":
        draw_kwargs["cmap"] = plt.cm.tab20

    nx.draw(**draw_kwargs)

    plt.title(f"{name} - {method}")

    # ===== SAVE =====
    if save:
        os.makedirs("output", exist_ok=True)
        file = f"output/{name}_{method}.png"
        plt.savefig(file, dpi=300, bbox_inches="tight")
        print(f"[SAVED] {file}")

    plt.show()
    plt.close()