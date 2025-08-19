import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import graphviz
from graph_tools import RandomDagGenerator, RandomDagVisualizer
# App title
st.title("Random Connected DAG Visualizer")


LAYOUT = {"spring": nx.spring_layout,
          "spiral": nx.spiral_layout,
          "circular": nx.circular_layout,
          "random": nx.random_layout
          }

ORDER = {"descending": "desc",
         "ascending": "asc"
         }



node_number = st.number_input(label="Number of Nodes (Required)", min_value=3, max_value=26, step=1)
edge_number = st.number_input(label="Number of Edges (Optional)", min_value=node_number - 1, max_value=(node_number * (node_number - 1))//2, step=1)
is_topological = st.checkbox(label="Absolute Topological")


if not is_topological and "topological_order" in st.session_state:
    st.session_state.topological_order = None

selected_order = st.radio(label="Select the order of the topological sort",
                          options=["descending", "ascending"],
                          key="topological_order",
                          disabled=not is_topological
                          )

selected_layout = st.radio(label="Select the layout of graph",
                           options=["spring", "spiral", "circular", "random"]
                           )
    
button = st.button(label="Create")
col1, col2 = st.columns(2) # Creates two columns of equal width

if button:


    if selected_order is None:
        dag_gen = RandomDagGenerator(node=node_number, edge=edge_number, order=None)
    else:
        dag_gen = RandomDagGenerator(node=node_number, edge=edge_number, order=ORDER[selected_order])
    G = dag_gen.generate_graph()

    dag_vis = RandomDagVisualizer(G, selected_layout)

    with col1:
        fig = dag_vis.visualize()
        st.subheader("Plot with plotly")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Plot with pyplot")
        dag_vis.visualize_with_pyplot()
        st.pyplot(plt)

    st.write(node_number, edge_number, selected_order, selected_layout)

    # Create a directed graph





    
   



    # # Create a graphlib graph object
    # graph = graphviz.Digraph()

    # for u, v in G.edges():
    #     graph.edge(str(u), str(v))

    # st.graphviz_chart(graph)

    # dag_gen = RandomDagGenerator(node=node_number, edge=edge_number, order=ORDER[selected_order])
    # G = dag_gen.generate_graph()

