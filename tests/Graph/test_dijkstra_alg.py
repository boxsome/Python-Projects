import pytest
from dijkstra_alg import find_shortest_path_length
from graph_classes import GraphNode, Edge


def test_invalid_input():
    with pytest.raises(ValueError):
        find_shortest_path_length({1 : GraphNode(1)}, 1, 2)
        find_shortest_path_length({1 : GraphNode(1)}, 2, 1)


def test_same_start_end():
    graph = {i: GraphNode(i) for i in range(1, 5)}
    assert find_shortest_path_length(graph, 1, 1) == 0
    assert find_shortest_path_length(graph, 2, 2) == 0
    assert find_shortest_path_length(graph, 3, 3) == 0
    assert find_shortest_path_length(graph, 4, 4) == 0


# example from dijkstra's algorithm wiki https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def test_undirected_graph():
    graph = {i: GraphNode(i) for i in range(1, 7)}
    edge = Edge(14, graph[1], graph[6])
    graph[1].add_edge(edge)
    graph[6].add_edge(edge)
    edge = Edge(9, graph[1], graph[3])
    graph[1].add_edge(edge)
    graph[3].add_edge(edge)
    edge = Edge(7, graph[1], graph[2])
    graph[1].add_edge(edge)
    graph[2].add_edge(edge)
    edge = Edge(15, graph[2], graph[4])
    graph[2].add_edge(edge)
    graph[4].add_edge(edge)
    edge = Edge(6, graph[5], graph[4])
    graph[5].add_edge(edge)
    graph[4].add_edge(edge)
    edge = Edge(9, graph[5], graph[6])
    graph[5].add_edge(edge)
    graph[6].add_edge(edge)
    edge = Edge(2, graph[6], graph[3])
    graph[3].add_edge(edge)
    graph[6].add_edge(edge)
    edge = Edge(10, graph[3], graph[2])
    graph[3].add_edge(edge)
    graph[2].add_edge(edge)
    edge = Edge(11, graph[3], graph[4])
    graph[3].add_edge(edge)
    graph[4].add_edge(edge)

    assert find_shortest_path_length(graph, 1, 1) == 0
    assert find_shortest_path_length(graph, 1, 2) == 7
    assert find_shortest_path_length(graph, 1, 3) == 9
    assert find_shortest_path_length(graph, 1, 4) == 20
    assert find_shortest_path_length(graph, 1, 5) == 20
    assert find_shortest_path_length(graph, 1, 6) == 11


# Example from shortest path problem wiki: https://en.wikipedia.org/wiki/Shortest_path_problem
def test_directed_graph():
    graph = {i: GraphNode(i) for i in "ABCDEF"}
    edge = Edge(4, graph["A"], graph["B"])
    graph["A"].add_edge(edge)
    edge = Edge(2, graph["A"], graph["C"])
    graph["A"].add_edge(edge)
    edge = Edge(5, graph["B"], graph["C"])
    graph["B"].add_edge(edge)
    edge = Edge(3, graph["C"], graph["E"])
    graph["C"].add_edge(edge)
    edge = Edge(4, graph["E"], graph["D"])
    graph["E"].add_edge(edge)
    edge = Edge(11, graph["D"], graph["F"])
    graph["D"].add_edge(edge)
    edge = Edge(10, graph["B"], graph["D"])
    graph["B"].add_edge(edge)

    assert find_shortest_path_length(graph, "A", "A") == 0
    assert find_shortest_path_length(graph, "A", "B") == 4
    assert find_shortest_path_length(graph, "A", "C") == 2
    assert find_shortest_path_length(graph, "A", "D") == 9
    assert find_shortest_path_length(graph, "A", "E") == 5
    assert find_shortest_path_length(graph, "A", "F") == 20
