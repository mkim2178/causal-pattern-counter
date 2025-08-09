import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import math
from dag_generator import DagGenerator
from pattern_finder import PatternFinder
from graph_visualizer import GraphVisualizer
from independency_finder import IndependencyFinder




def main():

    dag_generator = DagGenerator()
    pattern_finder = PatternFinder()
    graph_visualizer = GraphVisualizer()
    independency_finder = IndependencyFinder()


    DAG = dag_generator.generate_connected_random_dag(26)
    print(DAG.number_of_edges())

    colliders = pattern_finder.three_node_colliders(DAG)
    forks = pattern_finder.three_node_forks(DAG)

    source, target = independency_finder.select_random_source_and_target(DAG)
    print(nx.find_minimal_d_separator(DAG, source, target))

    print(source, target)









    """
    ---------------------------------------TESTING A VISUALIZER---------------------------------------
    """
    graph_visualizer.visualize_single_graph(DAG)
    graph_visualizer.visualize_multiple_graphs(colliders, "Collider")
    # graph_visualizer.visualize_multiple_graphs(forks, "Fork", "lightgreen")
    """
    ---------------------------------------TESTING A VISUALIZER---------------------------------------
    """











if __name__ == "__main__":
    main()