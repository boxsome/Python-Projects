class GraphNode:
    """Simple representation of a node in a graph. The graph itself would be a set of these graph nodes.
    The graph can be either directed or undirected, depending on if two connected nodes contain the edge for each other
    or not.
    """

    def __init__(self, node_id):
        self._node_id = node_id
        self._edges = set()

    def __eq__(self, other):
        if not isinstance(other, GraphNode):
            raise ValueError("Cannot compare a GraphNode with a non-GraphNode object.")

        return self.node_id == other.node_id

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash(self._node_id)

    @property
    def node_id(self):
        return self._node_id

    @property
    def edges(self):
        return self._edges

    def add_edge(self, new_edge):
        self._edges.add(new_edge)


class Edge:
    """Simple representation of an edge in a graph. Goes along with GraphNode.
    """
    def __init__(self, weight, start, end):
        self._weight = weight
        self._start = start
        self._end = end

    def __eq__(self, other):
        if not isinstance(other, Edge):
            raise ValueError("Cannot compare Edge object with non-Edge object.")

        return (self.weight, self.start, self.end) == (other.weight, other.start, other.end)

    def __ne__(self, other):

        return not self == other

    def __hash__(self):
        return hash(str(self.weight) + str(self.start) + str(self.end))

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    @property
    def weight(self):
        return self._weight

    def get_other(self, cur_node):
        if self._start == cur_node:
            return self._end
        elif self._end == cur_node:
            return self._start
        else:
            raise ValueError("*cur_node* provided is not part of this edge object.")

