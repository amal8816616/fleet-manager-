import heapq
from collections import defaultdict

class NavigationGraph:
    """
    A graph-based navigation system using Dijkstra's algorithm to find shortest paths.

    Attributes:
        graph (dict): A dictionary of location nodes and their neighbors with edge weights.

    Example:
        nav = NavigationGraph()
        nav.add_road("A", "B", 5)
        nav.add_road("A", "C", 10)
        nav.add_road("B", "C", 2)
        nav.shortest_path("A", "C")  # (7, ['A', 'B', 'C'])
    """

    def __init__(self):
        self.graph = defaultdict(list)

    def add_road(self, from_location, to_location, distance):
        """
        Adds a bidirectional road (edge) between two locations.

        Args:
            from_location (str): Starting location.
            to_location (str): Destination location.
            distance (int or float): Distance between locations.
        """
        self.graph[from_location].append((to_location, distance))
        self.graph[to_location].append((from_location, distance))

    def shortest_path(self, start, end):
        """
        Computes the shortest path from start to end using Dijkstra's algorithm.

        Args:
            start (str): Starting location.
            end (str): Destination location.

        Returns:
            (distance, path): Tuple of total distance and list of nodes in the shortest path.
        """
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        queue = [(0, start, [])]

        while queue:
            current_distance, current_node, path = heapq.heappop(queue)
            if current_node == end:
                return current_distance, path + [end]

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor, path + [current_node]))

        return float('inf'), []
