import networkx as nx
import random
import string
from exceptions import InvalidInputException


ALPHABETS = list(string.ascii_uppercase)
MIN_NODE = 3
MAX_NODE = 26
VALID_ORDERS = ["DESC", "ASC"]

class DAG_Generator:

    def __init__(self):
        pass


    def handle_invalid_node_number(self, node_number):

        if not isinstance(node_number, int) or isinstance(node_number, bool):
            raise InvalidInputException("INVALID TYPE: SHOULD BE AN INTEGER")

        if not (MIN_NODE <= node_number <= MAX_NODE):
            raise InvalidInputException(f"INVALID RANGE: SHOULD BE BETWEEN {MIN_NODE} ~ {MAX_NODE}")
        
    def handle_invalid_order(self, order):
        
        if not isinstance(order, str) or isinstance(order, bool):
            raise InvalidInputException("INVALID TYPE: SHOULD BE A STRING")

        if order not in VALID_ORDERS:
            raise InvalidInputException(f"INVALID STRING: SHOULD BE ONE OF: {VALID_ORDERS}")


    
    def generate_random_dag(self, node_number):
        """
        This function creates an alphabetical random DAG.

        1. Check if the number of node is valid.
        2. Initialize a list of nodes by select 'node_number' random nodes from 'ALPHABETS'.
        3. Initialize a random edge number (the possible edge number for a connected DAG will be between the node_number - 1 to (node_number * (node_number - 1)) // 2).
        4. Initialize a networkx.DiGraph() object (a directed graph).
        5. Run a while loop until the number of edges in the networkx.DiGraph() is equal to the 'random_edge_number'.
        6. Randomly select two nodes from the list from the first step (source and target)
        7. If there is no edge between source and target create an edge.
        8. Check if there is a cycle in our current graph (use networkx.is_directed_acyclic_graph).
        9. If a cycle exists, remove the edge that has been recently added.
        10. After the while loop, return the networkx.DiGraph() object.
        """

        self.handle_invalid_node_number(node_number)

        alphabetical_nodes = random.sample(ALPHABETS, node_number)
        random_edge_number = random.randint(node_number - 1, (node_number * (node_number - 1)) // 2)

        G = nx.DiGraph()

        while G.number_of_edges() < random_edge_number:
            source, target = random.sample(alphabetical_nodes, 2)

            if not G.has_edge(source, target):
                G.add_edge(source, target)
                if not nx.is_directed_acyclic_graph(G):
                    G.remove_edge(source, target)
        
        return G


    def generate_random_topological_dag(self, node_number, order):
        """
        This function creates a topological DAG.

        1. Check if the number of node and the order string is valid.
        3. Initialize a list of 'node_number' nodes that has a descending order.
        4. Create an empty list to store every possible edge
        5. Check the order option -> if order is "ASC", re-initialize the node list into an ascending order.
        6. Use a 2D for loop to add every possible edge with using a certain order.
        7. Initialize a random edge number (the possible edge number for a connected DAG will be between the node_number - 1 to (node_number * (node_number - 1)) // 2).
        8. Randomly select edges using the 'random_edge_number'.
        9. Initialize a networkx.DiGraph() object (a directed graph).
        10. Add all nodes and edges.
        11. Return the networkx.DiGraph() object.
        """
        self.handle_invalid_node_number(node_number)
        self.handle_invalid_order(order)

        numerical_nodes = [i for i in range(node_number, 0, -1)]
        possible_edges = []

        if order == "ASC":
            numerical_nodes = [i for i in range(1, node_number + 1)]

        # guarantee a connected graph
        connected_edges = [(numerical_nodes[i], numerical_nodes[i + 1]) for i in range(node_number - 1)]
        connected_edges_set = set(connected_edges) # this will be more efficient when checking if a possible edge is already in the `conected_edges` list

        for i in range(node_number):
            for j in range(i + 1, node_number):
                possible_edge = (numerical_nodes[i], numerical_nodes[j])
                if possible_edge not in connected_edges_set: # we're using set instead of list when using `in` so it would be more efficient if the length of connected_edges_set is big
                    possible_edges.append(possible_edge)

        random_edge_number = random.randint(node_number - 1, (node_number * (node_number - 1)) // 2)
        additional_edge_number = random_edge_number - len(connected_edges)
        additional_edges = random.sample(possible_edges, additional_edge_number)

        G = nx.DiGraph()
        G.add_nodes_from(numerical_nodes)
        G.add_edges_from(connected_edges + additional_edges)

        return G

