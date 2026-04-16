import random

def simulate_sir(graph, seeds, beta=0.05, gamma=0.2, steps=30):
    """
    SIR simulation with multiple seeds (using PEAK infection)
    """

    infected = set(seeds)
    recovered = set()

    peak = len(infected)  # 🔥 track peak

    for _ in range(steps):

        new_infected = set()

        # Infection
        for node in infected:
            for neighbor in graph[node]:
                if neighbor not in infected and neighbor not in recovered:
                    if random.random() < beta:
                        new_infected.add(neighbor)

        new_recovered = set()

        # Recovery
        for node in infected:
            if random.random() < gamma:
                new_recovered.add(node)

        infected |= new_infected
        infected -= new_recovered
        recovered |= new_recovered

        # update peak
        if len(infected) > peak:
            peak = len(infected)

        if not infected:
            break

    return peak   # 🔥 KHÔNG dùng total nữa