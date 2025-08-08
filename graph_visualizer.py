import networkx as nx
import matplotlib.pyplot as plt
import random
from pyvis.network import Network
from exceptions import MissingGraphException


class GraphVisualizer:

    def visualize_single_graph(self, graph, graph_title, node_color, with_using):

        if not graph:
            raise MissingGraphException(f"{graph_title} does not exist")

        print(type(graph))


        if with_using == "matplotlib":

            nx.draw(graph, with_labels=True, node_color=node_color)
            plt.title(graph_title)
            plt.show()
        
        else:

            pos = nx.spring_layout(graph, seed=42)
            net = Network(notebook=False, directed=True)
            net.from_nx(graph)
            scale = graph.number_of_nodes() * 100
            
            for node, (x, y) in pos.items():
                pyvis_node = net.get_node(node)
                pyvis_node['x'] = x * scale
                pyvis_node['y'] = y * scale
                pyvis_node['fixed'] = True
        
            net.toggle_physics(False)
            net.show("DAG.html")
    

    def visualize_multiple_graphs(self, graphs, graph_title, node_color):
        """
        A function that visualizes multiple sub graphs

        1. If `graphs` list is empty, raise a MissingGraphException.
        2. Else if the length of `graphs` list is equal to 1, excecute the `visualize_single_graph` function
        3. Otherwise, select two random graphs and visualize both of them side-by-side.
        """


        if len(graphs) == 0:
            raise MissingGraphException(f"{graph_title} does not exist")
        
        elif len(graphs) == 1:

            nx.draw(graphs[0], with_labels=True, node_color=node_color)
            plt.title(graph_title)
            plt.show()
            # self.visualize_single_graph(graphs[0], graph_title, node_color)

        else:

            two_random_graphs = random.sample(graphs, 2)

            fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
            for i, (G, ax) in enumerate(zip(two_random_graphs, axes)):
                pos = nx.spring_layout(G, k=0.8, iterations=20, seed=10)
                nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color=node_color)
                ax.set_title(f"Random {graph_title} {i + 1}")

            plt.subplots_adjust(wspace=0.5)
            plt.tight_layout()
            plt.show()
