from pyvis import network as net
import networkx as nx
import numpy as np

PARTY_COLOR = {'CDU': "#5264D3", 'CSU': "#D13E27", 'FDP': "#C727D1", 'Greens': "#13AD2B", 'Left': "#F70514", 'SPD': "DAF705"}

class NetworkView:
    """
    Class for network visualization
    """

    def __init__(self):
        pass

    @staticmethod
    def gen_simple_graph(adjacency_mat):

        G = nx.Graph()
        G.add_nodes_from(np.arange(adjacency_mat.shape[0]))

        for i in range(adjacency_mat.shape[0]):
            for j in range(i):

                if abs(adjacency_mat[i, j]) > 0:
                    G.add_edge(i, j, weight=adjacency_mat[i,j])

        return G

    @staticmethod
    def show_network_interactive(adjacency_mat, index_map=None):
        """
        Plots a network from adjacency_matrix
        """

        nw = net.Network(height="750px", width="100%", bgcolor="#E5E8E4", font_color="black")
        nw.barnes_hut()

        for i in range(adjacency_mat.shape[0]):
            if index_map is None:
                c = "#5264D3"
            else:
                name = index_map.get(i, None)
                if isinstance(name, dict):
                    c = PARTY_COLOR[name.get("organization")]
                else:
                    c = "#5264D3"

            nw.add_node(i, 
                        value=float(np.sum(abs(adjacency_mat[i,:]) > 0)), 
                        title=f'Id: {str(i)}', 
                        color=c)
                    

        for i in range(adjacency_mat.shape[0]):
            for j in range(i): 
                if abs(adjacency_mat[i, j]) > 0:
                    nw.add_edge(i, j, value=adjacency_mat[i,j])

        if index_map is not None:
            for node in nw.nodes:
                degree = np.sum(abs(adjacency_mat[int(node["id"]), :]) > 0)
                name = index_map.get(node["id"], "")

                if isinstance(name, dict):
                    party = name.get("organization", "")
                    name = name.get("name", "") 

                node["title"] += "<br>" + "Actor: " +  name  + "<br>" + "Orgganization:" + party \
                                 + "<br>" + "Degree: " + str(degree)
            # node["value"] = len(neighbor_map[node["id"]])
        
        return nw
