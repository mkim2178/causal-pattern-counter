import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

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
edge_number = st.number_input(label="Number of Edges (Optional)", value=None, min_value=node_number - 1, max_value=(node_number * (node_number - 1))//2, step=1)
is_topological = st.checkbox(label="Absolute Topological")



order = st.radio(label="Select the order of the topological sort.", options=["descending", "ascending"], index=None, disabled=not is_topological, key="topological_order")
    
button = st.button(label="Create")
col1, col2 = st.columns(2) # Creates two columns of equal width

if button:
    st.write(node_number, edge_number, order)




# # Generate random graph


# generator = DagGenerator()
# G = generator.generate_connected_random_dag(node_number)
# pos = nx.spring_layout(G, seed=42)

# # Extract edges
# edge_x, edge_y = [], []
# for u, v in G.edges():
#     x0, y0 = pos[u]
#     x1, y1 = pos[v]
#     edge_x += [x0, x1, None]
#     edge_y += [y0, y1, None]

# edge_trace = go.Scatter(
#     x=edge_x, y=edge_y,
#     mode="lines",
#     line=dict(width=1, color="gray"),
#     hoverinfo="none"
# )

# # Extract nodes
# node_x, node_y = zip(*[pos[node] for node in G.nodes()])
# node_trace = go.Scatter(
#     x=node_x, y=node_y,
#     mode="markers",
#     marker=dict(size=10, color="skyblue"),
#     text=[f"Node {n}" for n in G.nodes()],
#     hoverinfo="text"
# )

# # Combine into figure
# fig = go.Figure(data=[edge_trace, node_trace],
#                 layout=go.Layout(
#                     showlegend=False,
#                     hovermode="closest"
#                 ),
            
                
                
#                 )


    # for u, v in G.edges():
    #     graph.edge(str(u), str(v))

    # st.graphviz_chart(graph)

    # dag_gen = RandomDagGenerator(node=node_number, edge=edge_number, order=ORDER[selected_order])
    # G = dag_gen.generate_graph()

