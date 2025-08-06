import networkx as nx
import unittest
from dag_generator import DagGenerator


class TestGenerateConnectedRandomDag(unittest.TestCase):

    def test_connected_random_dag_is_dag_and_connected(self):
        generator = DagGenerator()
        graph = generator.generate_connected_random_dag(3)

        self.assertTrue(nx.is_directed_acyclic_graph(graph), "Graph should be directed and acyclic.")
        self.assertTrue(nx.is_weakly_connected(graph), "Graph should be weaklyu connected.")
    
    def test_connected_random_dag_using_topological_order_is_dag_and_connected(self):
        generator = DagGenerator()
        graph = generator.generate_connected_random_dag_using_topological_order(10, "DESC")

        self.assertTrue(nx.is_directed_acyclic_graph(graph), "Graph should be directed and acyclic.")
        self.assertTrue(nx.is_weakly_connected(graph), "Graph should be weakly connected.")

if __name__ == '__main__':
    unittest.main()