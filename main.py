import networkx as nx
import matplotlib.pyplot as plt
import random
import time
import math
from dag_generator import DagGenerator
from pattern_finder import PatternFinder




# --------------------------------------WORK IN PROGRESS--------------------------------------



def find_forks(test_DAG):

    print(test_DAG.edges)
# --------------------------------------WORK IN PROGRESS--------------------------------------
    








def main():

    dag_generator = DagGenerator()
    pattern_finder = PatternFinder()



    for i in range(10):
        same = {}
        for j in range(3, 27):
            DAG = dag_generator.generate_connected_random_dag(j)
            colliders = pattern_finder.three_node_colliders(DAG)
            forks = pattern_finder.three_node_forks(DAG)

            if len(colliders) == len(forks):
                same[j] = "SAME"
            else:
                same[j] = "DIFFERENT"
            
        print(f"SIMULATION {i}:")
        print(same)
        print()



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