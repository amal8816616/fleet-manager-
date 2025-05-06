from collections import deque
from ride_request import RideRequestQueue
class RideLog:
    """
    Represents a single ride instance in the ride history.

    Attributes:
        ride_id (str): Unique ride identifier.
        user_id (str): ID of the user who took the ride.
        vehicle_id (str): Vehicle used in the ride.
        location (str): Start or destination.
        rating (float): User-given rating after the ride.
    """
    def __init__(self, ride_id, user_id, vehicle_id, location, rating):
        self.ride_id = ride_id
        self.user_id = user_id
        self.vehicle_id = vehicle_id
        self.location = location
        self.rating = rating

    def __repr__(self):
        return f"RideLog({self.ride_id}, {self.user_id}, {self.location}, Rating: {self.rating})"

class RideHistoryManager:
    """
    Manages ride history for rebooking using a stack (LIFO).

    Example:
        history = RideHistoryManager()
        history.add_ride(rideLog)
        history.rebook_last_ride()
    """
    def __init__(self):
        self.stack = []

    def add_ride(self, ride_log):
        """Pushes a ride onto the history stack."""
        self.stack.append(ride_log)

    def view_history(self):
        """Returns all rides in reverse order (latest first)."""
        return list(reversed(self.stack))

    def rebook_last_ride(self):
        """Returns the last ride without removing it (peek)."""
        return self.stack[-1] if self.stack else None


def merge_sort_rides(rides, key_func=lambda ride: ride.rating):
    """
    Sorts rides based on a key function (e.g., rating, date) using merge sort.
    
    Args:
        rides (list): List of Ride objects.
        key_func (function): Function to extract comparison key from a ride.

    Returns:
        List of sorted Ride objects.
    """
    if len(rides) <= 1:
        return rides

    mid = len(rides) // 2
    left = merge_sort_rides(rides[:mid], key_func)
    right = merge_sort_rides(rides[mid:], key_func)

    return merge(left, right, key_func)

def merge(left, right, key_func):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
