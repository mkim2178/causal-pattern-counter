import networkx as nx
import random
import string
from exceptions import InvalidInputException

ALPHABETS = list(string.ascii_uppercase)
MIN_NODE = 3
MAX_NODE = 26
VALID_ORDERS = ["DESC", "ASC"]

class DagGenerator:


    def handle_invalid_node_number(self, node_number):

        if not isinstance(node_number, int) or isinstance(node_number, bool):
            raise InvalidInputException("Invalid type: should be an integer")

        if not (MIN_NODE <= node_number <= MAX_NODE):
            raise InvalidInputException(f"Invalid range: should be between {MIN_NODE} ~ {MAX_NODE}")
        

    def handle_invalid_order(self, order):
        
        if not isinstance(order, str) or isinstance(order, bool):
            raise InvalidInputException("Invalid type: should be a string")

        if order not in VALID_ORDERS:
            raise InvalidInputException(f"Invalid string: should be one of {" and ".join(VALID_ORDERS)}")

    
    def generate_connected_random_dag(self, node_number):
        """
        Generates a connected random DAG without enforcing a topological sequence.
        """

        self.handle_invalid_node_number(node_number)

        random_nodes = random.sample(ALPHABETS, node_number)
        random_edge_number = random.randint(node_number - 1, (node_number * (node_number - 1)) // 2)

        G = nx.DiGraph()

        for i in range(node_number - 1):
            G.add_edge(random_nodes[i], random_nodes[i + 1])

        while G.number_of_edges() < random_edge_number:
            source, target = random.sample(random_nodes, 2)
            
            if not G.has_edge(source ,target):
                G.add_edge(source, target)
                if not nx.is_directed_acyclic_graph(G):
                    G.remove_edge(source, target)
        
        return G


    def generate_connected_random_dag_using_topological_order(self, node_number, order):
        """
        Generates a connected random DAG by enforcing a topological sequence.
        """

        self.handle_invalid_node_number(node_number)
        self.handle_invalid_order(order)

        numerical_nodes = [i for i in range(node_number, 0, -1)]
        possible_edges = []

        if order == "ASC":
            numerical_nodes = [i for i in range(1, node_number + 1)]

        # guarantee a connected graph
        # we will use this set when checking if a possible edge is already in the 'connected_edges' list, `not in set()`` is more efficient than `not in list()`
        connected_edges = [(numerical_nodes[i], numerical_nodes[i + 1]) for i in range(node_number - 1)]
        connected_edges_set = set(connected_edges)

        for i in range(node_number):
            for j in range(i + 1, node_number):
                possible_edge = (numerical_nodes[i], numerical_nodes[j])
                if possible_edge not in connected_edges_set:
                    possible_edges.append(possible_edge)

        random_edge_number = random.randint(node_number - 1, (node_number * (node_number - 1)) // 2)
        additional_edge_number = random_edge_number - len(connected_edges)
        additional_edges = random.sample(possible_edges, additional_edge_number)

        G = nx.DiGraph()
        G.add_nodes_from(numerical_nodes)
        G.add_edges_from(connected_edges + additional_edges)

        return G
