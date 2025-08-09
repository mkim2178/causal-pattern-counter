import networkx as nx
import random
import os
import webbrowser
from pyvis.network import Network
from exceptions import MissingGraphException


class GraphVisualizer:

    def visualize_single_graph(self, graph):

        if not graph:
            raise MissingGraphException(f"graph does not exist")

        net = Network(width='100vw', height='100vh', notebook=False, directed=True)
        net.from_nx(graph)
        scale = graph.number_of_nodes() * 100

        pos = nx.spring_layout(graph, seed=42)
            
        for node, (x, y) in pos.items():
            pyvis_node = net.get_node(node)
            pyvis_node['x'] = x * scale
            pyvis_node['y'] = y * scale
            pyvis_node['fixed'] = True
        
        net.toggle_physics(False)
        html_file = "graph.html"
        net.show(html_file)

        full_path = os.path.abspath(html_file)
        webbrowser.open(f"file://{full_path}")

    

    def rename_graph_nodes(self, G, prefix):
        mapping = {node: f"{prefix}_{node}" for node in G.nodes()}
        return nx.relabel_nodes(G, mapping)


    def visualize_multiple_graphs(self, graphs, graph_title):
        """
        A function that visualizes multiple sub graphs

        1. If `graphs` list is empty, raise a MissingGraphException.
        2. Else if the length of `graphs` list is equal to 1, excecute the `visualize_single_graph` function
        3. Otherwise, select two random graphs and visualize both of them side-by-side.
        """

        if len(graphs) == 0:
            raise MissingGraphException(f"{graph_title} does not exist")
        
        random_graphs = None
        
        if len(graphs) == 1:
            random_graphs = graphs
        else:
            random_graphs = random.sample(graphs, 2)

        net = Network(width='100vw', height='100vh', notebook=False, directed=True)
        renamed_graphs = [self.rename_graph_nodes(G, f"{graph_title[:4]}{i+1}") for i, G in enumerate(random_graphs)]
        combined = nx.compose_all(renamed_graphs)
        net.from_nx(combined)

        scale = 300
        pos = nx.spring_layout(combined, seed=42)

        for node, (x, y) in pos.items():
            pyvis_node = net.get_node(node)
            pyvis_node['x'] = x * scale
            pyvis_node['y'] = y * scale
            pyvis_node['fixed'] = True

        net.toggle_physics(False)
        html_file = "merged_graph.html"
        net.show(html_file)

        full_path = os.path.abspath(html_file)
        webbrowser.open(f"file://{full_path}")
