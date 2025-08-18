import networkx as nx
import unittest
from graph_tools import RandomDagGenerator

class TestRandomDagGenerator(unittest.TestCase):

    def setUp(self):
        self.valid_random_dag_with_4_nodes = RandomDagGenerator(4).generate_graph()

    """
    TESTING: validate_node
    """
    def test_validate_node_valid(self):
        self.assertEqual(RandomDagGenerator.validate_node(3), 3)
        self.assertEqual(RandomDagGenerator.validate_node(26), 26)
    
    def test_validate_node_invalid_type(self):
        invalid_node_type = ["4", True, 4.0, 'A']
        for invalid_type in invalid_node_type:
            self.assertRaises(TypeError, RandomDagGenerator.validate_node(invalid_type))

    def test_validate_node_invalid_value(self):
        invalid_node_value = [2, 27, 0, -1]
        for invalid_value in invalid_node_value:
            self.assertRaises(ValueError, RandomDagGenerator.validate_node(invalid_value))
    """
    TESTING: validate_node
    """




