def pagerank(graph, d=0.85, max_iter=100, tol=1e-6):

    nodes = list(graph.keys())
    n = len(nodes)

    pr = {node: 1/n for node in nodes}
    degree = {node: len(graph[node]) for node in nodes}

    for _ in range(max_iter):

        new_pr = {}

        dangling_sum = sum(pr[node] for node in nodes if degree[node] == 0)

        for node in nodes:

            rank_sum = 0

            for neighbor in graph[node]:
                if degree[neighbor] > 0:
                    rank_sum += pr[neighbor] / degree[neighbor]

            new_pr[node] = (
                (1 - d) / n
                + d * rank_sum
                + d * dangling_sum / n
            )

        diff = sum(abs(new_pr[node] - pr[node]) for node in nodes)

        pr = new_pr

        if diff < tol:
            break

    # normalize
    total = sum(pr.values())
    return {k: v / total for k, v in pr.items()}