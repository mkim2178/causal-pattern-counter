import random
import networkx as nx



class IndependencyFinder:

    
    def select_random_source_and_target(self, DAG):
        """
        This function returns source and target nodes that are not adjacent with each other.
        """

        source = target = None
        is_adjacent = True

        while is_adjacent:
            source, target = random.sample(list(DAG.nodes), 2)
            if not DAG.has_edge(source, target) and not DAG.has_edge(target, source):
                is_adjacent = False

        return source, target


    def get_all_paths(self, DAG, source, target):
        """
        This function returns all possible paths between source and target nodes.
        """

        return list(nx.all_simple_paths(DAG.to_undirected(), source, target))
    