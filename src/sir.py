import random

def simulate_sir(graph, seeds, beta=0.05, gamma=0.2, steps=30):
    """
    SIR simulation with multiple seeds (using TOTAL infected)
    """

    infected = set(seeds)
    recovered = set()

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

        if not infected:
            break

    # TOTAL INFECTED
    return len(recovered)

def sir_for_visualization(graph, seeds, beta=0.05, gamma=0.2, steps=30):
    """
    Independent SIR function for visualization only
    Does NOT affect your original simulate_sir

    Return:
        dict: {node: "S" | "I" | "R"}
    """

    infected = set(seeds)
    recovered = set()

    for _ in range(steps):

        new_infected = set()
        new_recovered = set()

        # Infection
        for node in infected:
            for neighbor in graph[node]:
                if neighbor not in infected and neighbor not in recovered:
                    if random.random() < beta:
                        new_infected.add(neighbor)

        # Recovery
        for node in infected:
            if random.random() < gamma:
                new_recovered.add(node)

        infected |= new_infected
        infected -= new_recovered
        recovered |= new_recovered

        if not infected:
            break

    # Build state
    return {
        node: "I" if node in infected else
              "R" if node in recovered else
              "S"
        for node in graph
    }