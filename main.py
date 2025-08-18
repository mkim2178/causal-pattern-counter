
import networkx as nx
import matplotlib.pyplot as plt
from graph_tools import RandomDagGenerator



def main():

    """
    4
    4, 3
    4, 3, asc
    4, 3, desc
    4, asc
    4, desc
    
    
    
    
    """
    test_every_possible_parameter = [(4,), (4, 3), (4, 3, "asc"), (4, 3, "desc")]

    for parameter in test_every_possible_parameter:

        gen = RandomDagGenerator(*(parameter))
        g = gen.generate_graph()
    




    random_dag_gen2 = RandomDagGenerator(4, order="asc")
    G2 = random_dag_gen2.generate_graph()

    random_dag_gen3 = RandomDagGenerator(4, order="desc")
    G3 = random_dag_gen3.generate_graph()


    # pos = nx.spring_layout(G, seed=42)
    # nx.draw(G, pos=pos, with_labels=True)
    # plt.show()

    print("NO EXCEPTION")





if __name__ == "__main__":
    main()
