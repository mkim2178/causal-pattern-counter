import networkx as nx
import plotly.graph_objects as go

"""
WORK IN PROGRESS. DEBUG WITH THE APP.PY FILE
"""

LAYOUT = {"spring": nx.spring_layout,
          "spiral": nx.spiral_layout,
          "circular": nx.circular_layout,
          "random": nx.random_layout
          }



class RandomDagVisualizer:
    def __init__(self, graph, layout):
        self.graph = graph
        self.pos = LAYOUT[layout][self.graph]


    def customize_edges(self):

        edge_x = []
        edge_y = []


        for u, v in self.graph.edges():
            ux, uy = self.pos[u]
            vx, vy = self.pos[v]
            edge_x += [ux, vx, None]
            edge_y += [uy, vy, None]

        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=1, color='skyblue'),
            hoverinfo='none',
            mode='lines'
        )

        return edge_trace
    

    def customize_nodes(self):

        node_x = []
        node_y = []

        for node in self.graph.nodes():
            x, y = self.pos[node]
            node_x += [x]
            node_y += [y]
        
        node_trace = go.Scatter(
            x=node_x,
            y=node_y,
            mode='markers+text',
            hoverinfo='none',
            marker=dict(
                size=30,
                color='green',
                line=dict(width=2, color='gray')
            ),
            textfont=dict(
                size=17,
                color="white"
            )
        )

        return node_trace
    

    def visualize(self):

        edge_trace = self.customize_edges()
        node_trace = self.customize_nodes()

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(l=0,r=0,t=0,b=0),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
                            )
                        )
        
        fig.update_layout(
            autosize=True,
            margin=dict(l=0,r=0,t=0,b=0)
        )
