import networkx as nx
import random
import string

ALPHABETS = set(string.ascii_uppercase)
MIN_NODE = 3
MAX_NODE = 26
VALID_ORDERS = {"desc", "asc"}


class RandomDagGenerator:

    def __init__(self, node, edge=None, order=None):

        self.node = self.validate_node(node) # 3 ~ 26

        self.min_edge = self.node - 1
        self.max_edge = (self.node * (self.node - 1)) // 2

        self.edge = self.validate_edge(self.node, edge) # self.node - 1 ~ (self.node * (self.node - 1)) // 2

        self.order = self.validate_order(order)


    def validate_node(self, node):

        if not isinstance(node, int) or isinstance(node, bool):
            raise TypeError(f"Invalid type: {type(node).__name__}, should be an int.")
        if node < MIN_NODE or MAX_NODE < node:
            raise ValueError(f"Invalid node value: {node} -> expected an integer between {MIN_NODE} and {MAX_NODE} inclusive.")
        return node
    
    def validate_edge(self, node, edge):

        if edge is None:
            return edge
        if not isinstance(edge, int) or isinstance(edge, bool):
            raise TypeError(f"Invalid type: {type(edge).__name__}, should be an int.")
        if edge < node - 1 or edge > (node * (node - 1)) // 2:
            raise ValueError(f"Invalid edge value: {edge} -> expected an integer between {self.min_edge} and {self.max_edge} inclusive.")
        return edge
    
    def validate_order(self, order):

        if order is None:
            return order
        if not isinstance(order, str) or isinstance(order, bool):
            raise TypeError(f"Invalid type: {type(order).__name__}, should be a string.")
        if order not in VALID_ORDERS:
            raise ValueError(f"Invalid order value: {order} -> expected one of these strings: {VALID_ORDERS}.")
        return order
    


    def absolute_topological(self):

        numerical_nodes = [i for i in range(self.node, 0, -1)]
        possible_edges = []

        if self.order == "asc":
            numerical_nodes = [i for i in range(1, self.node + 1)]

        # guarantee a connected graph
        # we will use this set when checking if a possible edge is already in the 'connected_edges' list, `not in set()`` is more efficient than `not in list()`
        connected_edges = [(numerical_nodes[i], numerical_nodes[i + 1]) for i in range(self.node - 1)]
        connected_edges_set = set(connected_edges)

        for i in range(self.node):
            for j in range(i + 1, self.node):
                possible_edge = (numerical_nodes[i], numerical_nodes[j])
                if possible_edge not in connected_edges_set:
                    possible_edges.append(possible_edge)

        if self.edge is None:
            self.edge = random.randint(self.min_edge, self.max_edge)
        additional_edge_number = self.edge - len(connected_edges)
        additional_edges = random.sample(possible_edges, additional_edge_number)

        G = nx.DiGraph()
        G.add_nodes_from(numerical_nodes)
        G.add_edges_from(connected_edges + additional_edges)

        return G


    def generate_graph(self):

        if self.order is None:

            random_nodes = random.sample(sorted(ALPHABETS), self.node)
            
            if self.edge is None:
                self.edge = random.randint(self.min_edge, self.max_edge)

            G = nx.DiGraph()

            for i in range(self.node - 1):
                G.add_edge(random_nodes[i], random_nodes[i + 1])

            while G.number_of_edges() < self.edge:
                source, target = random.sample(random_nodes, 2)
            
                if not G.has_edge(source ,target):
                    G.add_edge(source, target)

                    if not nx.is_directed_acyclic_graph(G):
                        G.remove_edge(source, target)
        
            return G
        else:
            return self.absolute_topological()
        
    
