import networkx as nx
import random
import string


ALPHABETS = list(string.ascii_uppercase)

class DAG_Generator:

    def __init__(self, n):
        """
        self.n (int): a number of nodes
        self.minimum_edges (int): a minimum number of edges
        self.maximum_edges (int): a maximum number of edges
        """
        self.n = n # this might be removed and will be the parameter of each DAG generating function
        self.random_edges = random.randint(n - 1, (n * (n - 1)) // 2)


    
    def generate_random_dag(self):
        """
        This function creates an alphabetical random DAG.

        1. Select 'self.n' random nodes from 'ALPHABETS'
        2. Initialize a networkx.DiGraph() object (a directed graph).
        3. Run a while loop until the number of edges in the networkx.DiGraph() is equal to the 'self.random_edges'.
        4. Randomly select two nodes from the list from the first step.
        5. Create an edge between selected nodes
        6. Check if there is a cycle in our current graph (use networkx.is_directed_acyclic_graph).
        7. If a cycle exists, remove the edge that has been recently added.
        8. After the while loop, return the networkx.DiGraph() object.
        """

        alphabetical_nodes = random.sample(ALPHABETS, self.n)

        G = nx.DiGraph()

        while G.number_of_edges() < self.random_edges:
            source, target = random.sample(alphabetical_nodes, 2)
            G.add_edge(source, target)

            if not nx.is_directed_acyclic_graph(G):
                G.remove_edge(source, target)
        
        print(G.number_of_edges())
        return G


    def generate_random_topological_dag(self, order="DESC"):
        """
        This function creates a topological DAG.

        1. Create a 'self.n' numerical nodes with descending order (the descending order is a default order).
        2. Create an empty list to store every possible edge
        3. Check the order option -> if order is "ASC", re-initialize the numerical nodes list into an ascending order.
        4. Use a 2D for loop to add every possible edge with using a certain order.
        5. Randomly select edges using the 'self.random_edges'
        6. Initialize a networkx.DiGraph() object (a directed graph).
        7. Add all nodes and edges.
        8. Return the networkx.DiGraph() object.
        """

        numerical_nodes = list(range(self.n, 0, -1))
        possible_edges = []

        if order == "ASC":
            numerical_nodes = list(range(1, self.n + 1))

        for i in range(self.n):
            for j in range(i + 1, self.n):
                source = numerical_nodes[i]
                target = numerical_nodes[j]
                possible_edges.append((source, target))

        selected_edges = random.sample(possible_edges, self.random_edges)

        G = nx.Digraph()

        G.add_nodes_from(numerical_nodes)
        G.add_edges_from(selected_edges)

        return G



    # def generate_descending_topological_dag(self):
    #     """
    #     This function creates a descending topological DAG.

    #     Logic:
    #     1. Create all nodes and store them in a list with a descending order.
    #     2. Create an empty list that wills tore every possible topological edge (edges will be stored as a tuple).
    #     3. Use a 2D for loop to add every possible edge from a higher node to a lower node to the empty list.
    #     4. Select a random edge number from n - 1: self.minimum_edges, to (n * (n - 1)) // 2: self.maximum_edges.
    #     5. Randomly select edges using the number chosen from the previous step.
    #     6. Initialize a networkx.DiGraph() object (a directed graph).
    #     7. Add all nodes and edges.
    #     8. Return the networkx.DiGraph() object.
    #     """

    #     nodes = list(range(self.n, 0, -1)) # [5, 4, 3, 2, 1]
    #     possible_edges = []

    #     for i in range(self.n):
    #         for j in range(i + 1, self.n):
    #             source = nodes[i]
    #             target = nodes[j]
    #             possible_edges.append((source, target))
        
    #     random_edges = random.randint(self.minimum_edges, self.maximum_edges)
    #     edges = random.sample(possible_edges, random_edges)

    #     G = nx.DiGraph()

    #     G.add_nodes_from(nodes)
    #     G.add_edges_from(edges)

    #     return G


    # def generate_descending_topological_dag_cycle_check(self):
    #     """
    #     This function creates a descending topological DAG by checking for cycles each time an edge is added (less efficient).

    #     Logic:
    #     1. Select a random number of edges.
    #     2. Initialize a networkx.DiGraph() object (a directed graph).
    #     3. Run a while loop until the number of edges in the graph is equal to the randomly selected edge number.
    #     4. Randomly select two distinct nodes from 1 to n; assign the larger node as source and smaller as target.
    #     5. Add an edge from source to target.
    #     6. Check if there is a cycle in our current graph (use networkx.is_directed_acyclic_graph).
    #     7. If a cycle exists, remove the edge that has been recently added.
    #     8. After the while loop, return the networkx.DiGraph() object.
    #     """

    #     random_edges = random.randint(self.minimum_edges, self.maximum_edges)
    #     G = nx.DiGraph()

    #     while G.number_of_edges() < random_edges:
    #         u, v = random.sample(range(1, self.n + 1), 2)

    #         source = max(u, v)
    #         target = min(u, v)

    #         G.add_edge(source, target)
    #         if not nx.is_directed_acyclic_graph(G):
    #             G.remove_edge(source, target)
    
    #     return G

