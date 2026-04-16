def load_graph(path):
    graph = {}

    with open(path, 'r') as f:
        for line in f:
            line = line.strip()

            # Skip  header/comment
            if (
                not line
                or line.startswith('%')
                or line.startswith('#')
            ):
                continue

            parts = line.split()

            # Skip  metadata line : n n m
            if len(parts) < 2:
                continue
            if len(parts) == 3:
                # size of .mtx
                continue

            try:
                u, v = map(int, parts[:2])
            except ValueError:
                continue

            # if want to 0-index:
            # u -= 1
            # v -= 1

            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []

            graph[u].append(v)
            graph[v].append(u)

    return graph