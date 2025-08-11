import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import math
from dag_generator import DagGenerator
from pattern_finder import PatternFinder
from graph_visualizer import GraphVisualizer
from independency_finder import IndependencyFinder
from itertools import combinations



def main():

    dag_generator = DagGenerator()
    pattern_finder = PatternFinder()
    graph_visualizer = GraphVisualizer()
    independency_finder = IndependencyFinder()



    """
    ---------------------------------------TESTING A GENERATOR---------------------------------------
    """


    random_dag = dag_generator.generate_connected_random_dag(5)

    for node in list(random_dag.nodes):
        print(f"node: {node}, descendants with distance 2: {list(nx.descendants_at_distance(random_dag, node, 2))}")
        descendants_with_distance_two = list(nx.descendants_at_distance(random_dag, node, 2))

        for descendant in descendants_with_distance_two:
            print(list(nx.all_shortest_paths(random_dag, node, descendant)))
        

    colls = pattern_finder.find_all_colliders(random_dag)
    forks = pattern_finder.find_all_forks(random_dag)

    # print(colls)
    # print(forks)

    nx.draw(random_dag, with_labels=True)
    plt.show()




    # topological_random_dag = dag_generator.generate_connected_random_dag_using_topological_order(15, "DESC")
    """
    ---------------------------------------TESTING A GENERATOR---------------------------------------
    """



    """
    ---------------------------------------TESTING A PATTERN_FINDER---------------------------------------
    """
    # colliders = pattern_finder.three_node_colliders(random_dag)
    # forks = pattern_finder.three_node_forks(random_dag)
    """
    ---------------------------------------TESTING A PATTERN_FINDER---------------------------------------
    """



    """
    ---------------------------------------TESTING A VISUALIZER---------------------------------------
    """
    # graph_visualizer.visualize_single_graph(random_dag)
    # graph_visualizer.visualize_multiple_graphs(colliders, "Collider")
    # graph_visualizer.visualize_multiple_graphs(forks, "Fork", "lightgreen")
    """
    ---------------------------------------TESTING A VISUALIZER---------------------------------------
    """




    """
    ---------------------------------------TESTING AN INDEPEDENCY_FINDER---------------------------------------
    """
    # source, target = independency_finder.select_random_source_and_target(DAG)
    """
    ---------------------------------------TESTING AN INDEPEDENCY_FINDER---------------------------------------
    """



if __name__ == "__main__":
    main()