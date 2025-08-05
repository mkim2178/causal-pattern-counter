import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import math
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
    








def main():

    dag_generator = DAG_Generator()

    DAG = dag_generator.generate_random_topological_dag(26, "ASC")
    print(f"DAG?: {nx.is_directed_acyclic_graph(DAG)}")
    print(f"CONNECTED?: {nx.is_weakly_connected(DAG)}")
    pos = nx.spring_layout(DAG, k=0.8, iterations=20)
    nx.draw(DAG, pos, with_labels=True, arrows=True, node_color="lightblue")
    plt.tight_layout()
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