import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import math
from dag_generator import DagGenerator
from pattern_finder import PatternFinder
from graph_visualizer import GraphVisualizer




def main():

    dag_generator = DagGenerator()
    pattern_finder = PatternFinder()
    graph_visualizer = GraphVisualizer()

    adj_counter = 0



    DAG = dag_generator.generate_connected_random_dag(26)
    is_adj = True

    source = target = None

    attepts = 0
    while is_adj:

        source, target = random.sample(list(DAG.nodes), 2)
        attepts += 1

        if not DAG.has_edge(source, target) and not DAG.has_edge(target, source):
            is_adj = False

    print(source, target)
    print(f"ATTEMPTS EXECUTED: {attepts}")

    for node in [source, target]:
        child_nodes = list(nx.descendants_at_distance(DAG, node, 1))
        print(f"child node of {node}: {child_nodes}")


    # all_paths = nx.all_simple_paths(DAG.to_undirected(), source, target)

    # for path in all_paths:
    #     print(path)

    graph_visualizer.visualize_single_graph(DAG, "DAG", "lightblue")



        # print(f"two random nodes: {random_two_nodes}")

        # for node in random_two_nodes:
        #     print(f"STARTING NODE: {node}")
        #     child_nodes = list(nx.descendants_at_distance(DAG, node, 1))
        #     print(child_nodes)


        # all_paths = nx.all_simple_paths(DAG.to_undirected(), source, target)
    
        # for path in list(all_paths):
        #     if len(path) == 2:
        #         # print("they are adjacent")
        #         adj_counter += 1
        #         break
        #     # print(path)
    # print(adj_counter)
    # graph_visualizer.visualize_single_graph(DAG, "DAG", "lightblue")

    



    # colliders = pattern_finder.three_node_colliders(DAG)
    # forks = pattern_finder.three_node_forks(DAG)

    # graph_visualizer.visualize_single_graph(DAG, "DAG", "lightblue")
    # graph_visualizer.visualize_multiple_graphs(colliders, "Collider", "lightgray")
    # graph_visualizer.visualize_multiple_graphs(forks, "Fork", "lightgreen")


    # for i in range(10):
    #     same = {}
    #     for j in range(3, 27):
    #         DAG = dag_generator.generate_connected_random_dag(j)
    #         colliders = pattern_finder.three_node_colliders(DAG)
    #         forks = pattern_finder.three_node_forks(DAG)

    #         if len(colliders) == len(forks):
    #             same[j] = "SAME"
    #         else:
    #             same[j] = "DIFFERENT"
            
    #     print(f"SIMULATION {i}:")
    #     print(same)
    #     print()



    # print(f"NUMBER OF DAG WITH HAVING A SAME AMOUNT OF COLLIDERS AND FORKS: {len(colliders)}")
        

    # nx.draw(DAG, with_labels=True, node_color="lightblue")
    # plt.show()
    

    



    # plots_per_row = 5
    # rows = math.ceil(len(forks) / plots_per_row)

    # fig, axes = plt.subplots(rows, plots_per_row, figsize=(plots_per_row * 4, rows * 4))

    # if rows == 1:
    #     axes = [axes]
    
    # axes_flat = []
    # for row_axes in axes:
    #     # axes row can be array or single axes
    #     if hasattr(row_axes, '__iter__'):
    #         axes_flat.extend(row_axes)
    #     else:
    #         axes_flat.append(row_axes)
    

    # for i, G in enumerate(forks):
    #     ax = axes_flat[i]
    #     pos = nx.spring_layout(G, seed=1234)
    #     nx.draw(G, pos=pos, with_labels=True, ax=ax, node_color="lightblue")
    #     ax.set_title(f"Graph {i + 1}")

    # for i in range(len(forks), len(axes_flat)):
    #     fig.delaxes(axes_flat[i])


    # plt.show()








    # has = 0
    # has_not = 0
    
    # for i in range(100000):

    #     DAG = dag_generator.generate_connected_random_dag_using_topological_order(5, "DESC")

    #     colliders = pattern_finder.find_all_colliders(DAG)
    #     print(i)
    #     if len(colliders) == 0:
    #         has_not += 1
    #         print("NO COLLIDERS")
    #     else:
    #         has += 1
    #         print("HAS COLLIDERS")

        # fig, axes = plt.subplots(1, len(colliders), figsize=(12, 4))

        # for i, (G, ax) in enumerate(zip(colliders, axes)):
        #     pos = nx.spring_layout(G, k=0.8, iterations=20, seed=1234)
        #     nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color="lightblue")

        # plt.tight_layout()
        # plt.show()

    # print("RATIO OF 1000 DAG'S COLLIDERS") 
    # print(f"COLLIDERS: {has}, NO COLLIDERS: {has_not}")


    # pos = nx.spring_layout(DAG, k=0.8, iterations=20)
    # nx.draw(DAG, pos, with_labels=True, arrows=True, node_color="lightblue")
    # plt.tight_layout()
    # plt.show()





    
    # fig, axes = plt.subplots(1, len(colliders), figsize=(12, 4))

    # for i, (G, ax) in enumerate(zip(colliders, axes)):
    #     pos = nx.spring_layout(DAG, k=0.8, iterations=20)
    #     nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color="lightblue")

    # plt.tight_layout()
    # plt.show()


    




    # DAG = create_DAG_alternative_ver(15)



    # DAGS = [cycle_check_DAG, DAG]


    # fig, axes = plt.subplots(1, len(DAGS), figsize=(12, 4))

    # for i, (G, ax) in enumerate(zip(DAGS, axes)):
    #     pos = nx.spring_layout(DAG, k=0.8, iterations=20)
    #     nx.draw(G, pos, with_labels=True, ax=ax, arrows=True, node_color="lightblue")

    # plt.tight_layout()
    # plt.show()

if __name__ == "__main__":
    main()