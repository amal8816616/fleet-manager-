from collections import deque

class RideRequest:
    """
    Represents a user's request for a ride.

    Attributes:
        user_id (str): ID of the user requesting the ride.
        location (str): Pickup location.
        location_geo (str): Geographical coordinates of the pickup location.
        destination (str): Drop-off location.
        destination_geo (str): Geographical coordinates of the drop-off location.
        vehicle_type (str): Preferred type of vehicle.
    """

    def __init__(self, user_id, location, location_geo, destination, destination_geo, vehicle_type):
        """
        Initialize a ride request with pickup and drop-off details.

        Args:
            user_id (str): ID of the user making the request.
            location (str): Pickup location.
            location_geo (str): Pickup geographic coordinates.
            destination (str): Drop-off location.
            destination_geo (str): Drop-off geographic coordinates.
            vehicle_type (str): Preferred vehicle type for the ride.

        Example:
            >>> RideRequest("U123", "Dubai Marina", (25.0772, 55.1330), "Dubai Mall", (25.1975, 55.2790), "car")
        """
        self.user_id = user_id
        self.location = location
        self.location_geo = location_geo
        self.destination = destination
        self.destination_geo = destination_geo
        self.vehicle_type = vehicle_type

class RideRequestQueue:
    """
    Manages pending ride requests using a queue (FIFO).

    Example:
        queue = RideRequestQueue()
        queue.add_request(ride)
        queue.process_next_request()
    """
    def __init__(self):
        self.queue = deque()

    def add_request(self, ride):
        """Adds a new ride request to the queue."""
        self.queue.append(ride)

    def process_next_request(self):
        """Processes the next ride request (FIFO)."""
        return self.queue.popleft() if self.queue else None

    def pending_requests(self):
        """Returns all pending ride requests."""
        return list(self.queue)
