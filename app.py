import streamlit as st
import networkx as nx
import plotly.graph_objects as go
from graph_tools import RandomDagGenerator
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

if button:
    st.write(node_number, edge_number, selected_order, selected_layout)

    dag_gen = RandomDagGenerator(node=node_number, edge=edge_number, order=ORDER[selected_order])
    G = dag_gen.generate_graph()
    pos = LAYOUT[selected_layout](G)

    edge_x = []
    edge_y = []

    for u, v in G.edges():
        ux, uy = pos[u]
        vx, vy = pos[v]
        edge_x += [ux, vx, None]
        edge_y += [uy, vy, None]


    edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    line=dict(width=1, color='skyblue'),
    hoverinfo='none',
    mode='lines')

    node_x = []
    node_y = []

    for node in G.nodes():
        x, y = pos[node]
        node_x += [x]
        node_y += [y]
    


    node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode='markers+text',
    text=[str(node) for node in G.nodes()],
    textposition="top center",
    hoverinfo='text',
    marker=dict(
        size=30,
        color='green',
        line=dict(width=2, color='gray')),
    textfont=dict(
        size=17,
        color="yellow"
    )
    )


    fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(l=0,r=0,t=0,b=0),
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                ))
    

    fig.update_layout(
    autosize=True,         # let Plotly auto-adjust figure size
    margin=dict(l=0,r=0,t=0,b=0)
    )

    st.plotly_chart(fig, use_container_width=True)






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
#     x0, y0 = pos[u]
#     x1, y1 = pos[v]
#     fig.add_annotation(
#         ax=x0, ay=y0,
#         x=x1, y=y1,
#         xref="x", yref="y", axref="x", ayref="y",
#         showarrow=True,
#         arrowhead=3,
#         arrowsize=1,
#         arrowwidth=1,
#         arrowcolor="gray"
#     )

# # Show in Streamlit
# st.plotly_chart(fig, use_container_width=True)
