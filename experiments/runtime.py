import time
import matplotlib.pyplot as plt

from src.graph_loader import load_graph
from src.louvain import louvain
from src.pagerank import pagerank

def runtime_comparison():

    datasets = [
        ("Karate", "data/test.txt"),
        ("HepTh", "data/CA-HepTh.txt"),
        ("AstroPh", "data/CA-AstroPh.txt"),
    ]

    sizes = []
    louvain_times = []
    pagerank_times = []

    print("\n===== Runtime Comparison =====")

    for name, path in datasets:

        graph = load_graph(path)

        sizes.append(len(graph))

        start = time.time()
        louvain(graph)
        t1 = time.time() - start

        start = time.time()
        pagerank(graph)
        t2 = time.time() - start

        louvain_times.append(t1)
        pagerank_times.append(t2)

        print(f"{name}: Louvain={t1:.4f}s | PageRank={t2:.4f}s")

    plt.figure()
    plt.plot(sizes, louvain_times, marker="o", label="Louvain")
    plt.plot(sizes, pagerank_times, marker="o", label="PageRank")

    plt.xlabel("Nodes")
    plt.ylabel("Time (s)")
    plt.title("Runtime vs Graph Size")

    plt.legend()
    plt.savefig("output/runtime.png")
    plt.close()