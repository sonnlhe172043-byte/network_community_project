from src.utils import to_networkx
import matplotlib.pyplot as plt
import networkx as nx

def draw_graph(graph, communities=None, name="Graph"):

    # CHỈ vẽ Karate và HepTh
    global node_size
    if name not in ["Karate", "HepTh"]:
        print(f"[SKIP] Visualization skipped for {name} (too large)")
        return

    G = to_networkx(graph)

    plt.figure(figsize=(8, 6))

    # màu theo community
    if communities:
        colors = [communities[node] for node in G.nodes()]
    else:
        colors = "blue"

    # 🔥 layout riêng cho từng dataset
    if name == "Karate":
        pos = nx.spring_layout(G, seed=42)  # đẹp
        node_size = 80

    elif name == "HepTh":
        pos = nx.spring_layout(G, seed=42, iterations=20)  # giảm load
        node_size = 10

    nx.draw(
        G, pos,
        node_color=colors,
        node_size=node_size,
        cmap=plt.cm.tab20,
        with_labels=False
    )

    plt.title(name)
    plt.show()