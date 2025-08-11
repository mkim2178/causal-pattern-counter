import networkx as nx
from itertools import combinations

class PatternFinder:


    def find_all_colliders(self, DAG):
        """
        find all colliders
        """

        return set(nx.dag.colliders(DAG))
    
    def find_all_forks(self, DAG):
        """
        find all forks
        """

        forks = set()
        for node in DAG.nodes:
            for p1, p2 in combinations(DAG.successors(node), 2):
                fork = (p1, node, p2)
                forks.add(fork)
        return forks
    
    def find_all_chains(self, DAG):
        """
        find all chains
        """

        chains = set()

        pass
















    def three_node_colliders(self, DAG):

        colliders = list(nx.dag.colliders(DAG))

        if len(colliders) == 0:
            return []
    
        collider_graphs = []

        for collider in colliders:
            collider_graph = nx.DiGraph()
            collider_graph.add_edges_from([(collider[0], collider[1]), (collider[2], collider[1])])
            collider_graphs.append(collider_graph)
    
        return collider_graphs
    

    def three_node_forks(self, DAG):

        fork_graphs = []

        for node in list(DAG.nodes):
            child_nodes = list(nx.descendants_at_distance(DAG, node, 1))
            for i in range(len(child_nodes)):
                for j in range(i + 1, len(child_nodes)):
                    fork = nx.DiGraph()
                    fork.add_edges_from([(node, child_nodes[i]), (node, child_nodes[j])])
                    fork_graphs.append(fork)
        
        return fork_graphs