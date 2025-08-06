import networkx as nx
import matplotlib.pyplot as plt
from exceptions import MissingGraphException


class GraphVisualizer:

    def visualize_single_graph(self, graph, graph_title, node_color):

        if not graph:
            raise MissingGraphException(f"{graph_title} does not exist")

        nx.draw(graph, with_labels=True, node_color=node_color)
        plt.title(graph_title)
        plt.show()
    

    def visualize_multiple_graphs(self, graphs, graph_title, node_color):


        if len(graphs) == 0:
            raise MissingGraphException(f"{graph_title} does not exist")
        
        if len(graphs) == 1:
            self.visualize_single_graph(graphs[0], graph_title, node_color)

        else:
            fig, axes = plt.subplots(nrows=len(graphs), ncols=1, figsize=(6, len(graphs)*5))
            for i, (G, ax) in enumerate(zip(graphs, axes)):
                pos = nx.spring_layout(G, k=0.8, iterations=20, seed=10)
                nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color=node_color)
                ax.set_title(f"{graph_title} {i + 1}")

            plt.subplots_adjust(wspace=0.5)
            plt.tight_layout()
            plt.show()
