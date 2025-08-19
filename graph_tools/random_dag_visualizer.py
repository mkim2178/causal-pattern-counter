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
        self.pos = LAYOUT[layout](self.graph)


    def customize_edges(self):

        edge_x = []
        edge_y = []

        edge_annotations = []


        for u, v in self.graph.edges():
            ux, uy = self.pos[u]
            vx, vy = self.pos[v]
            edge_x += [ux, vx, None]
            edge_y += [uy, vy, None]

            edge_annotations.append(
                dict(
                    ax=ux,
                    ay=uy,
                    x=vx,
                    y=vy,
                    xref="x",
                    yref="y",
                    axref="x",
                    ayref="y",
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor="#812CCF",
                )
            )



        edge_trace = go.Scatter(
            x=edge_x,
            y=edge_y,
            line=dict(width=2, color="#812CCF"),
            hoverinfo='none',
            mode='lines'
        )

        return edge_trace, edge_annotations
    

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
            text=[str(node) for node in self.graph.nodes()],
            hoverinfo='text',
            marker=dict(
                size=30,
                color="#44B34F",
                line=dict(width=2, color='#977f7f')
            ),
            textfont=dict(
                size=20,
                color="#FFFFFF"
            )
        )

        return node_trace
    

    def visualize(self):

        edge_trace, edge_annotations = self.customize_edges()
        node_trace = self.customize_nodes()

        fig = go.Figure(data=[edge_trace, node_trace],
                        layout=go.Layout(
                            showlegend=False,
                            hovermode='closest',
                            margin=dict(l=0,r=0,t=0,b=0),
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            annotations=edge_annotations
                            )
                        )
        
        fig.update_layout(
            autosize=True,
            margin=dict(l=0,r=0,t=0,b=0)
        )

        return fig


    def visualize_with_pyplot(self):

        nx.draw(self.graph, self.pos, with_labels=True, arrows=True, node_color='skyblue')
