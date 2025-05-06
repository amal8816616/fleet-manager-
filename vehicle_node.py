class Vehicle:
    """
    Represents a ride-sharing vehicle.

    Attributes:
        vehicle_id (str): Unique identifier for the vehicle.
        vehicle_type (str): Type of the vehicle (e.g., car, bike, bus).
        status (str): Current status (e.g., available, busy, maintenance).
        location (str): Current location of the vehicle.
        location_geo (str): Geo-coordinates of the current location.
        driver_id (str): Unique ID of the assigned driver.
        next_location (str): Next destination name.
        next_location_geo (str): Geo-coordinates of the next destination.
    """

    def __init__(self, vehicle_id, vehicle_type, status, location, location_geo, driver_id,
                 next_location=None, next_location_geo=None):
        """
        Initialize a new vehicle.

        Args:
            vehicle_id (str): Unique ID of the vehicle.
            vehicle_type (str): Type of the vehicle.
            status (str): Status of the vehicle.
            location (str): Current location of the vehicle.
            location_geo (str): Geo-coordinates of the current location.
            driver_id (str): Unique ID of the driver.
            next_location (str, optional): Name of the next destination.
            next_location_geo (str, optional): Geo-coordinates of the next destination.
        """
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.status = status
        self.location = location
        self.location_geo = location_geo
        self.driver_id = driver_id
        self.next_location = next_location
        self.next_location_geo = next_location_geo
