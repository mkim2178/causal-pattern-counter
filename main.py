import networkx as nx
import matplotlib.pyplot as plt
import random
import time
from dag_generator import DAG_Generator




# --------------------------------------WORK IN PROGRESS--------------------------------------
def find_colliders(test_DAG):

    colliders = nx.dag.colliders(test_DAG)

    if list(colliders) == 0:
        return []
    
    collider_graphs = []

    for collider in colliders:
        g = nx.DiGraph()
        g.add_edges_from([(collider[0], collider[1]), (collider[2], collider[1])])
        collider_graphs.append(g)
    
    return collider_graphs


def find_forks(test_DAG):

    print(test_DAG.edges)
# --------------------------------------WORK IN PROGRESS--------------------------------------
    








def has_cycle(G):
    try:
        list(nx.find_cycle(G, orientation='original'))
        return True
    except nx.exception.NetworkXNoCycle:
        return False


def create_DAG(n):
    """
    check the cycle

    1. choose a random number of edge
    2. choose two random nodes for starting and ending node
    3. add first with those nodes (bigger node, smaller node)
    4. check if there is a cycle -> if there is, remove the latest added edge
    5. return the graph
    """
    min_edges = n - 1
    max_edges = (n * (n - 1)) // 2

    random_edges = random.randint(min_edges, max_edges)
    G = nx.DiGraph()

    while G.number_of_edges() < random_edges:
        u, v = random.sample(range(1, n + 1), 2)
        big = max(u, v)
        small = min(u, v)

        G.add_edge(big, small)

        if not nx.is_directed_acyclic_graph(G):
            G.remove_edge(big, small)
    
    print(G.number_of_edges())
    return G











def create_DAG_alternative_ver(n):
    """
    1. create every node
    2. create every possible edge with using the logic (larger -> smaller)
    3. choose a random number of edge
    4. choose possible random edges from step 2 with using a random number from step 3
    5. add every node and edge
    6. return the graph

    This is more efficient because since our possible edge lists includes NEVER create a cycle
    we don't have to check if there is a cycle in our current graph every time.
    """

    nodes = list(range(n, 0, -1))

    able_edges = [] # every possible edge
    for i in range(n):
        for j in range(i + 1, n):
            able_edges.append((nodes[i], nodes[j]))
    
    min_edges = n - 1
    max_edges = len(able_edges) 
    num_edges = random.randint(min_edges, max_edges)
    edges = random.sample(able_edges, num_edges)

    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    print(G.number_of_edges())
    return G


def measure_time(f, n):
    start = time.time()
    f(n)
    end = time.time()

    return end - start


def main():

    dag_generator = DAG_Generator(10)


    DAG = dag_generator.generate_random_dag()
    print(nx.is_directed_acyclic_graph(DAG))

    pos = nx.spring_layout(DAG, k=0.8, iterations=20)
    nx.draw(DAG, pos, with_labels=True, arrows=True, node_color="lightblue")
    plt.show()

    




    # DAG = create_DAG_alternative_ver(15)



    # DAGS = [cycle_check_DAG, DAG]


    # fig, axes = plt.subplots(1, len(DAGS), figsize=(12, 4))

    # for i, (G, ax) in enumerate(zip(DAGS, axes)):
    #     pos = nx.spring_layout(DAG, k=0.8, iterations=20)
    #     nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color="lightblue")

    # plt.tight_layout()
    # plt.show()

if __name__ == "__main__":
    main()