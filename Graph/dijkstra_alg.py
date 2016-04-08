from collections import deque
import math
from graph_classes import GraphNode, Edge


def find_shortest_path_length(graph, start_node_id, end_node_id):
    """Finds the shortest path between two given nodes in the given graph. Uses dijkstra's algorithm to do this.

    A few notes:
        Not really use a priority queue but simulating its functionality with a normal deque.
        We lose some performance in doing this (I chose not to use queue.PriortyQueue for this exercise).
        This causes us to have a worst-case of O(|V|^2) where V is the set of nodes.

        Space is O(|V|) (excluding the graph given) for storing the distance mapping and the "priority queue".
    """
    if start_node_id not in graph or end_node_id not in graph:
        raise ValueError("Both nodes must be in the given graph.")
    elif start_node_id == end_node_id:
        return 0

    priority_q = deque(graph.values())
    distances = {start_node_id: 0}

    while priority_q:
        # Extract vertex with minimum distance
        cur_node = min(iter(priority_q), key=lambda node: distances.get(node.node_id, math.inf))
        priority_q.remove(cur_node)

        if cur_node.node_id == end_node_id:
            return distances[end_node_id]

        # Iterate through all current node's edges and do updates accordingly to distance mapping
        for edge in sorted(iter(cur_node.edges), key=lambda e: e.weight):
            cur_dist = distances[cur_node.node_id] + edge.weight
            other_node = edge.get_other(cur_node)
            if cur_dist < distances.get(other_node.node_id, math.inf):
                distances[other_node.node_id] = cur_dist


# Driver code for find_shortest_path_length for manual testing
if __name__ == "__main__":
    print("Please enter number of nodes and number of edges as space separated integers.")
    num_nodes, num_edges = map(int, input().split(" "))

    graph = {i: GraphNode(i) for i in range(1, num_nodes+1)}

    for i in range(1, num_edges+1):
        print("Please enter three of integers for edge {} (weight, start, end).".format(i))
        edge_weight, edge_start, edge_end = map(int, input().split(" "))
        edge = Edge(edge_weight, graph[edge_start], graph[edge_end])
        graph[edge_start].add_edge(edge)
        graph[edge_end].add_edge(edge)

    print("Please enter pair of integers for two nodes in the graph to find the shortest distance between the two")
    start_node, end_node = map(int, input().split(" "))

    print(find_shortest_path_length(graph, start_node, end_node))



