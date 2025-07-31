import networkx as nx
import matplotlib.pyplot as plt
import random


def create_random_DAG(nodes, edges):
    G = nx.DiGraph()
    while G.number_of_edges() < edges:
        u, v = random.sample(range(1, nodes + 1), 2)
        G.add_edge(u, v)
        if not nx.is_directed_acyclic_graph(G):
            cycle_list = list(nx.find_cycle(G, orientation="original"))
            G.remove_edges_from(cycle_list)
    return G

DAG = create_random_DAG(10, 9)
print(nx.is_directed_acyclic_graph(DAG))
nx.draw(DAG, with_labels=True, node_color="lightblue")
plt.title("Random DAG")
plt.show()



# print(G.nodes)

# print(nx.is_directed_acyclic_graph(G))

# print(nx.is_directed(G))

# G = nx.DiGraph()
# G.add_node("X")
# G.add_edges_from([("X", "R"), 
#             ("R", "S"), 
#             ("S", "T"), 
#             ("U", "T"),
#             ("V", "U"),
#             ("V", "Y")
#             ])


# # print(nx.is_directed_acyclic_graph(G))
# # print(nx.ancestors(G, "S"))
# # print(list(nx.dag.colliders(G)))
# # print(nx.dag_longest_path(G))
# print(list(nx.dag.v_structures(G)))
# print(list(nx.dag.colliders(G)))
# print(nx.descendants(G, "X"))