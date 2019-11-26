import networkx as nx
import matplotlib.pyplot as plt
import graph_generator as gg


# This module contains DrawGraph class with methods corresponding to drawing specific type of graph
# Uses graph_generator module methods for getting graph representations and then interprets them
# accordingly

class DrawGraph:
    # Default dirpath and gg class
    dirpath = "./"
    graph_gen = gg.GraphGenerator("./")

    # Constructor
    def __init__(self, dirpath):
        self.dirpath = dirpath
        self.graph_gen = gg.GraphGenerator(dirpath)

    # Draws file relationship graph
    def draw_file_graph(self):
        x = self.graph_gen.get_graph()

        G = nx.DiGraph()
        for i in range(0, len(x)):
            G.add_edge(x[i][0], x[i][1], length=x[i][2])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, edge_color='black', width=1, node_size=1000, node_color='lightgreen', with_labels=True)
        edge_labels = dict([((u, v,), d['length']) for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.2)
        plt.show()

    # Draws method relationship graph
    def draw_method_graph(self):
        pass

    # Draws file relationship graph

    def draw_module_graph(self):

        array = self.graph_gen.get_graph_func()[0]
        array2 = self.graph_gen.get_graph_func()[1]

        # TODO Array 2 returns empties

        graphx = nx.DiGraph()
        pos = nx.spring_layout(graphx)
        sum = [0] * len(array)

        for i in range(1, len(array)):
            for j in range(1, len(array)):
                sum[i] += int(array[i][j])

        for i in range(1, len(array)):
            for j in range(1, len(array)):
                if i != j and array[i][j] != "0":
                    graphx.add_edge(array[i][0] + "\n" + str(sum[i]), array[0][j] + "\n" + str(sum[j]), length=array[i][j])

        for i in range(1, len(array)):
            if len(array2[i - 1]) > 0:
                for j in range(0, len(array2[i - 1])):
                    graphx.add_edge(array2[i - 1][j], array[i][0] + "\n" + str(sum[i]), length="")

        color_map = []
        for node in graphx:
            if ".py" not in node:
                color_map.append('lightblue')
            else:
                color_map.append('lightgreen')


        nx.draw(graphx, pos, edge_color='black', width=0.5, node_size=1000, node_color=color_map, with_labels=True,
                font_size=10)
        edge_labels = dict([((u, v,), d['length']) for u, v, d in graphx.edges(data=True)])
        nx.draw_networkx_edge_labels(graphx, pos, edge_labels=edge_labels, label_pos=0.4)
        plt.show()


test = DrawGraph("./")
test.draw_module_graph()
