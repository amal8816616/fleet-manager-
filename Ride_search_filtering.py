class Ride:
    """
    Represents a ride with key attributes for searching and sorting.

    Attributes:
        ride_id (str): Unique identifier for the ride.
        location (str): The area where the ride originates or is available.
        vehicle_type (str): Type of vehicle (e.g., Car, Bike, Bus).
        driver_rating (float): Average rating of the driver (1.0 - 5.0).
        date (str): Date of the ride in 'YYYY-MM-DD' format.

    Example:
        ride = Ride("r001", "Downtown", "Car", 4.5, "2025-04-22")
    """
    def __init__(self, ride_id, location, vehicle_type, driver_rating, date):
        self.ride_id = ride_id
        self.location = location
        self.vehicle_type = vehicle_type
        self.driver_rating = driver_rating
        self.date = date  # can also be datetime.date for actual comparison
    def __repr__(self):
        return f"Ride({self.ride_id}, {self.vehicle_type}, Rating: {self.driver_rating}, Date: {self.date})"


class RideSearchManager:
    """
    Manages rides with fast lookup by location, filtering by vehicle/rating,
    and merge sorting by date or rating.

    Example:
        manager = RideSearchManager()
        ride1 = Ride("r001", "Downtown", "Car", 4.5, "2025-04-22")
        manager.add_ride(ride1)
        results = manager.search(location='Downtown', vehicle_type='Car')
        sorted_rides = manager.sort_rides(results, by='date')
    """
    def __init__(self):
        self.rides_by_location = {}

    def add_ride(self, ride):
        """Adds a ride to the hash-indexed storage by location."""
        if ride.location not in self.rides_by_location:
            self.rides_by_location[ride.location] = []
        self.rides_by_location[ride.location].append(ride)

    def search(self, location, vehicle_type=None, min_rating=None):
        """
        Returns a filtered list of rides by location, vehicle type, and minimum driver rating.
        """
        results = self.rides_by_location.get(location, [])
        if vehicle_type:
            results = [r for r in results if r.vehicle_type.lower() == vehicle_type.lower()]
        if min_rating:
            results = [r for r in results if r.driver_rating >= min_rating]
        return results

    def sort_rides(self, rides, by='date'):
        """Sorts the given list of rides using merge sort by 'date' or 'rating'."""
        return self.merge_sort(rides, key=by)

    def merge_sort(self, rides, key='date'):
        """Recursive merge sort implementation for sorting rides."""
        if len(rides) <= 1:
            return rides

        mid = len(rides) // 2
        left = self.merge_sort(rides[:mid], key)
        right = self.merge_sort(rides[mid:], key)
        return self.merge(left, right, key)

    def merge(self, left, right, key):
        """Helper merge function used in merge sort."""
        sorted_list = []
        while left and right:
            left_val = getattr(left[0], key)
            right_val = getattr(right[0], key)
            if left_val <= right_val:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        sorted_list.extend(left or right)
        return sorted_list
