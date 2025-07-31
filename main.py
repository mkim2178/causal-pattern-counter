import networkx as nx
import matplotlib.pyplot as plt
import random



"""
A graph must have at least 3 nodes with 2 edges.
"""

def create_DAG(num_nodes, num_edges):
    """
    Create a directed acyclic graph (DAG) with specified number of nodes and edges.

    This function creates a DAG that satisfies following condtions:
    - at least 4 nodes and 3 edges
    - at most (number of nodes * number of nodes - 1) // 2 edges
    - the DAG is guaranteed to be connected

    Parameters:
        num_nodes (int): A number of DAG's nodes
        num_edges (int): A number of DAG's edges
    
    Returns:
        G (networkx.Digraph): A connected and directed acyclic graph that satisfies conditions from the long description
    
    Raise:
        ValueError:
            - if number of nodes is less than 4 or number of edges is less than 3
            - if number of edges exceeds the 'maximum_edges'
            - if number of edges is less than the number of nodes - 1
    """


    if num_nodes < 4 or num_edges < 3:
        raise ValueError("DAG has too few nodes or edges: minimum number of nodes: 4, minimum number of edges: 3")
    

    maximum_edges = (num_nodes * (num_nodes - 1)) // 2
    if num_edges > maximum_edges:
        raise ValueError("DAG has too many edges, which can create a cycle: reduce the number of edges")


    if num_edges < num_nodes - 1:
        raise ValueError("DAG can be disconnected: increase the number of edges")


    G = nx.DiGraph()

    # connect every node with num_nodes - 1 edges to guarantee a connected DAG
    for i in range(1, num_nodes):
        G.add_edge(i, i + 1)


    while G.number_of_edges() < num_edges:

        # get two random nodes and add it to the graph
        u, v = random.sample(range(1, num_nodes + 1), 2)

        # if there is no path where v -> u (checking a cycle) add the edge u -> v: this avoids the creation of a cycle
        if not nx.has_path(G, v, u):
            G.add_edge(u, v)
    
    return G


def check_DAG(test_DAG):
    """
    Print out a string "IS DAG" if the graph is directed acyclic graph.

    This function calls the networkx's 'is_directed_acyclic_graph' to check if the graph is a DAG (returns True if DAG, otherwise, False).

    Parameters:
        test_DAG (networkx.DiGraph): A directed graph that has been created from the function 'create_DAG'
    """

    if nx.is_directed_acyclic_graph(test_DAG):
        print("IS DAG")
    else:
        print("NOT A DAG")


"""
create functions that finds the collider and draw the graph (codes already in the main())
"""


def main():
    DAG = create_DAG(6, 7)

    check_DAG(DAG)




    colliders = nx.dag.colliders(DAG)

    graphs = []
    for collider in colliders:
        g = nx.DiGraph()
        g.add_edges_from([(collider[0], collider[1]), (collider[2], collider[1])])
        graphs.append(g)


    graphs.append(DAG)

    fig, axes = plt.subplots(1, len(graphs), figsize=(12, 4))

    for i, (G, ax) in enumerate(zip(graphs, axes)):
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color="lightblue")
        if i == len(graphs) - 1:
            ax.set_title(f"DAG")
        else:
            ax.set_title(f"Collider {i+1}")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()