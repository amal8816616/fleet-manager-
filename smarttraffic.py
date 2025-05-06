import heapq

class TrafficVehicle:
    """
    Represents a vehicle and its traffic delay.

    Attributes:
        vehicle_id (str): Unique identifier for the vehicle.
        delay (int): Traffic delay in minutes.

    Example:
        vehicle = TrafficVehicle("V123", 8)
        print(vehicle)  # Output: Vehicle(V123, Delay: 8min)
    """
    def __init__(self, vehicle_id, delay):
        self.vehicle_id = vehicle_id
        self.delay = delay

    def __lt__(self, other):
        return self.delay < other.delay

    def __repr__(self):
        return f"Vehicle({self.vehicle_id}, Delay: {self.delay}min)"


class TrafficManager:
    """
    Manages traffic delays using a min-heap to prioritize vehicles with the least delay.

    Example:
        tm = TrafficManager()
        tm.add_vehicle("V101", 10)
        tm.add_vehicle("V102", 5)
        next_vehicle = tm.get_next_vehicle()
        print(next_vehicle)  # Output: Vehicle(V102, Delay: 5min)
    """
    def __init__(self):
        self.heap = []
        self.vehicle_map = {}  # Maps vehicle_id to TrafficVehicle for quick updates

    def add_vehicle(self, vehicle_id, delay):
        """
        Adds a vehicle with its current delay to the heap.

        Args:
            vehicle_id (str): Unique ID for the vehicle.
            delay (int): Traffic delay in minutes.

        Example:
            tm.add_vehicle("V201", 12)
        """
        vehicle = TrafficVehicle(vehicle_id, delay)
        heapq.heappush(self.heap, vehicle)
        self.vehicle_map[vehicle_id] = vehicle

    def update_vehicle_delay(self, vehicle_id, new_delay):
        """
        Updates a vehicle's delay by removing and reinserting it into the heap.

        Args:
            vehicle_id (str): ID of the vehicle to update.
            new_delay (int): New delay value.

        Example:
            tm.update_vehicle_delay("V201", 7)
        """
        if vehicle_id in self.vehicle_map:
            # Rebuild heap without the old record
            self.heap = [v for v in self.heap if v.vehicle_id != vehicle_id]
            heapq.heapify(self.heap)

        # Add updated vehicle
        self.add_vehicle(vehicle_id, new_delay)

    def get_next_vehicle(self):
        """
        Returns the vehicle with the least traffic delay.

        Returns:
            TrafficVehicle or None: Vehicle object with lowest delay, or None if heap is empty.

        Example:
            vehicle = tm.get_next_vehicle()
            if vehicle:
                print(vehicle.vehicle_id)
        """
        while self.heap:
            vehicle = heapq.heappop(self.heap)
            if vehicle.vehicle_id in self.vehicle_map:
                del self.vehicle_map[vehicle.vehicle_id]
                return vehicle
        return None
