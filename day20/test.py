file_name = 'test_input1.txt'
file_name = 'input.txt'

with open(file_name, 'r') as fd:
    lines = fd.readlines()

fflops = {}
conjs = {}
graph = {}

for line in lines:
    source, dests = line.split(' -> ')
    dests = [x.strip() for x in dests.split(', ')]

    if source[0] in ['%', '&']:
        type = source[0]
        source = source[1:]
        if type == '%':
            fflops[source] = False
        elif type == '&':
            conjs[source] = {}

    graph[source] = dests

for source, dests in graph.items():
    for dest in dests:
        if dest in conjs:
            conjs[dest][source] = False

print(graph, conjs, fflops)


import networkx as nx
import matplotlib.pyplot as plt


# g = nx.DiGraph()
# g.add_nodes_from(graph.keys())
#
# for k, v in graph.items():
#     g.add_edges_from(([(k, t) for t in v]))
#
# pos = nx.spring_layout(g, k=0.3, iterations=20)
# nx.draw(g, pos, edge_color='black', width=1, linewidths=1,
#     node_size=500, node_color='pink', alpha=0.9,
#     labels={node: node for node in g.nodes()})
# plt.show()


for k, v in graph.items():
    for val in v:
        if k in fflops:
            print(f'{k} --> {val}[FF_{val}]')
        else:
            print(f'{k} --> {val}[CJ_{val}]')

