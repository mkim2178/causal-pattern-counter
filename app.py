import streamlit as st
import networkx as nx
import plotly.graph_objects as go
from dag_generator import DagGenerator

# App title
st.title("Interactive Network Graph Visualizer")

# Sidebar controls



node_number = st.number_input(label="Number of Nodes", min_value=3, max_value=26, step=1)


# Generate random graph


generator = DagGenerator()
G = generator.generate_connected_random_dag(node_number)
pos = nx.spring_layout(G, seed=42)

# Extract edges
edge_x, edge_y = [], []
for u, v in G.edges():
    x0, y0 = pos[u]
    x1, y1 = pos[v]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]

edge_trace = go.Scatter(
    x=edge_x, y=edge_y,
    mode="lines",
    line=dict(width=1, color="gray"),
    hoverinfo="none"
)

# Extract nodes
node_x, node_y = zip(*[pos[node] for node in G.nodes()])
node_trace = go.Scatter(
    x=node_x, y=node_y,
    mode="markers",
    marker=dict(size=10, color="skyblue"),
    text=[f"Node {n}" for n in G.nodes()],
    hoverinfo="text"
)

# Combine into figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    showlegend=False,
                    hovermode="closest"
                ),
            
                
                
                )


for u, v in G.edges():
    x0, y0 = pos[u]
    x1, y1 = pos[v]
    fig.add_annotation(
        ax=x0, ay=y0,
        x=x1, y=y1,
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor="gray"
    )

# Show in Streamlit
st.plotly_chart(fig, use_container_width=True)
