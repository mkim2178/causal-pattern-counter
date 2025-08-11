import networkx as nx
import unittest
import random
from dag_generator import DagGenerator
from pattern_finder import PatternFinder


class TestGenerateConnectedRandomDag(unittest.TestCase):

    def set_up(self):
        self.generator = DagGenerator()
        self.finder = PatternFinder()

    def test_connected_random_dag_is_dag_and_connected(self):

        for i in range(3, 27):

            graph = self.generator.generate_connected_random_dag(i)
            self.assertTrue(nx.is_directed_acyclic_graph(graph), "Graph should be directed and acyclic.")
            self.assertTrue(nx.is_weakly_connected(graph), "Graph should be weaklyu connected.")

    
    def test_connected_random_dag_using_topological_order_is_dag_and_connected(self):

        for i in range(3, 27):
            graph = self.generator.generate_connected_random_dag_using_topological_order(i, "DESC")
            self.assertTrue(nx.is_directed_acyclic_graph(graph), "Graph should be directed and acyclic.")
            self.assertTrue(nx.is_weakly_connected(graph), "Graph should be weakly connected.")

        
        for i in range(3, 27):
            graph = self.generator.generate_connected_random_dag_using_topological_order(i, "ASC")
            self.assertTrue(nx.is_directed_acyclic_graph(graph), "Graph should be directed and acyclic.")
            self.assertTrue(nx.is_weakly_connected(graph), "Graph should be weakly connected.")
    


    
        




if __name__ == '__main__':
    unittest.main()