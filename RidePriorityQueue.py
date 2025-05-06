import heapq

class RidePriorityQueue:
    """
    Implements a priority queue (min-heap) to allocate rides to vehicles based on the lowest cost.

    Attributes:
        queue (list): The list maintaining the heap structure.
        entry_finder (dict): Maps vehicle IDs to heap entries for quick updates.
        counter (int): Unique sequence count to prevent comparison issues.

    Example:
        pq = RidePriorityQueue()
        pq.add_vehicle("car_101", 12)
        pq.add_vehicle("car_205", 7)
        pq.get_best_vehicle()  # ('car_205', 7)
        pq.remove_vehicle("car_205")
        pq.get_best_vehicle()  # ('car_101', 12)
    """

    def __init__(self):
        self.queue = []
        self.entry_finder = {}  # Maps vehicle_id -> entry
        self.REMOVED = "<removed-vehicle>"
        self.counter = 0

    def add_vehicle(self, vehicle_id, priority):
        """
        Adds or updates a vehicle in the priority queue.

        Args:
            vehicle_id (str): Unique identifier of the vehicle.
            priority (int or float): Cost/urgency value; lower = higher priority.
        """
        if vehicle_id in self.entry_finder:
            self.remove_vehicle(vehicle_id)
        entry = [priority, self.counter, vehicle_id]
        self.entry_finder[vehicle_id] = entry
        heapq.heappush(self.queue, entry)
        self.counter += 1

    def remove_vehicle(self, vehicle_id):
        """
        Marks a vehicle as removed.

        Args:
            vehicle_id (str): Vehicle to remove from the queue.
        """
        entry = self.entry_finder.pop(vehicle_id)
        entry[-1] = self.REMOVED

    def get_best_vehicle(self):
        """
        Returns the vehicle with the highest priority (lowest cost).

        Returns:
            tuple: (vehicle_id, priority) or None if no vehicles available.
        """
        while self.queue:
            priority, count, vehicle_id = heapq.heappop(self.queue)
            if vehicle_id is not self.REMOVED:
                del self.entry_finder[vehicle_id]
                return vehicle_id, priority
        return None

    def __len__(self):
        return len(self.entry_finder)
