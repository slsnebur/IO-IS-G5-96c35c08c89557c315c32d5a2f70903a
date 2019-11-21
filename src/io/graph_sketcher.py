import networkx as nx
import matplotlib.pyplot as plt
import graph_generator as pd

# SUPER DOKUMENTACJA:
# This module contains DrawGraph class with methods corresponding to drawing desired type of graph
# Uses graph_generator module methods for getting graph representations and then interprets them
# accordingly

# TODO
# second story
# making this work

class DrawGraph:
    # Default dirpath
    dirpath = "./"

    # Constructor
    def __init__(self, dirpath):
        self.dirpath = dirpath

    def draw_file_dependency_graph(self):
        G = nx.DiGraph()
        for i in range(0, len(x)):
            G.add_edge(x[i][0], x[i][1], length=x[i][2])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, edge_color='black', width=1, node_size=1000, node_color='lightgreen', with_labels=True)
        edge_labels = dict([((u, v,), d['length']) for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.2)
        plt.show()

    def draw_call_graph(self):
        pass

    def draw_module_dependency_graph(self):

        graph_representation = pd.GraphGenerator(self.dirpath)
        array = graph_representation.get_graph_func()[0]
        array2 = graph_representation.get_graph_func()[1]

        '''
        array = [["",        "main.py", "graphgen.py", "pgraphdraw.py"],
                 ["main.py",       "0",      "1",           "1"],
                 ["graphgen.py",   "0",      "0",           "0"],
                 ["pgraphdraw.py", "0",      "0",           "0"]]
        '''

        sum = [0] * len(array)

        for i in range(1, len(array)):
            for j in range(1, len(array)):
                sum[i] += int(array[i][j])

        for i in range(1, len(array)):
            for j in range(1, len(array)):
                if i != j and array[i][j] != "0":
                    G.add_edge(array[i][0] + "\n" + str(sum[i]), array[0][j] + "\n" + str(sum[j]), length=array[i][j])

        '''
        array2 = [[],
                  ["count_func", "filter_non_py", "get_imports", "get_graph",
                   "show_info", "get_func_list", "list_func_calls", "get_graph_func"],
                  ["drawGraph"]]
        '''

        for i in range(1, len(array)):
            if len(array2[i - 1]) > 0:
                for j in range(0, len(array2[i - 1])):
                    G.add_edge(array2[i - 1][j], array[i][0] + "\n" + str(sum[i]), length="")

        for node in G:
            if ".py" not in node:
                color_map.append('lightblue')
            else:
                color_map.append('lightgreen')

        nx.draw(G, pos, edge_color='black', width=0.5, node_size=1000, node_color=color_map, with_labels=True,
                font_size=10)
        edge_labels = dict([((u, v,), d['length']) for u, v, d in G.edges(data=True)])
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, label_pos=0.4)
        plt.show()


test = DrawGraph("./")
test.drawGraph()