"""
This module makes operations with graphs.
"""


import graphviz


def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    list_of_graphs = list()
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if line[-1] == "\n":
                line = line[:-1]
            line = line.split(",")
            line[0] = int(line[0])
            line[1] = int(line[1])
            list_of_graphs.append(line)
    return list_of_graphs


def to_edge_dict(edge_list):
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    counter = edge_list
    for i in range(len(counter)):
        edge_list.append([edge_list[i][1], edge_list[i][0]])
    sorted_tops = sorted({sorted_tops[0]: [sorted_tops[1]]
                          for sorted_tops in edge_list})
    result = {top: [] for top in sorted_tops}
    for i in edge_list:
        for tops_in_list in sorted_tops:
            if i[0] == tops_in_list:
                result[tops_in_list].append(i[1])
                result[tops_in_list].sort()
    return result


def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    edge_list = list()
    for item in graph:
        for element in graph[item]:
            edge_list.append((item, element))
    return edge in edge_list


def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 3, 5], 2: [1, 4], 3: [1, 4], 4: [2, 3], 5: [1]}
    """
    edge_list = list()
    for item in graph:
        for element in graph[item]:
            edge_list.append((item, element))
    if edge not in edge_list:
        edge_list.append(edge)
        edge_list.append((edge[1], edge[0]))
    sorted_edge_list = sorted({part[0]: [part[1]] for part in edge_list})
    result = {top: [] for top in sorted_edge_list}
    for i in edge_list:
        for tops_in_list in sorted_edge_list:
            if i[0] == tops_in_list:
                result[tops_in_list].append(i[1])
                result[tops_in_list].sort()
    return result


def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    for i in graph:
        for counter in range(2):
            if i == edge[counter]:
                for numb in range(2):
                    if edge[numb] in graph[i]:
                        graph[i].remove(edge[numb])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph


def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph:
        del graph[node]
        for i in graph:
            for index in range(len(graph[i])):
                if graph[i][index] == node:
                    del graph[i][index]
    return graph


def convert_to_dot(graph):
    """
    (dict) -> (None)

    Save the graph to a file in a DOT format.
    """
    module_graph = graphviz.Graph()
    for element in graph:
        for top in graph[element]:
            module_graph.edge(str(element), str(top))
    with open("bruh.txt", "w", encoding="utf - 8") as file:
        for line in module_graph:
            file.write(line + "\n")
