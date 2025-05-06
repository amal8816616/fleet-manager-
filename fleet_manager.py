from vehicle_node import Vehicle
class FleetManager:
    """
    A linked list-based fleet manager to handle ride-sharing vehicles.
    """

    def __init__(self):
        """
        Initialize an empty fleet.

        Example:
            >>> fleet = FleetManager()
            >>> print(fleet.head)
            None
        """
        self.head = None
        self.ongoing_rides=[]

    def add_vehicle(self, vehicle_id, vehicle_type, status, location,location_geo,driver_id,next_location=None, next_location_geo=None):
        """
        Add a new vehicle to the fleet.

        Args:
            vehicle_id (str): Unique ID of the vehicle.
            vehicle_type (str): Type of the vehicle.
            status (str): Status of the vehicle.
            location (str): Current location of the vehicle.
            location_geo (str): Geo-cordinates 
            driver_id (str): Unique ID of the driver.

        Example:
            >>> fleet = FleetManager()
            >>> fleet.add_vehicle("V001", "car", "available", "Burj Khalifa","25.1972, 55.2744",1)
            >>> fleet.add_vehicle("V002", "bike", "available", "Dubai Marina","25.0772, 55.1330",2)
        """
        new_vehicle = Vehicle(vehicle_id, vehicle_type, status, location,location_geo,driver_id,next_location, next_location_geo)
        new_vehicle.next = self.head
        self.head = new_vehicle
        print(f"Vehicle {vehicle_id} added.")

    def remove_vehicle(self, vehicle_id):
        """
        Remove a vehicle from the fleet by ID.

        Args:
            vehicle_id (str): The ID of the vehicle to be removed.
        Example:
            >>> fleet = FleetManager()
            >>> fleet.add_vehicle("V003", "bus", "available", "Burjuman Metro Station","25.2528, 55.3032",3)
            >>> fleet.remove_vehicle("V003")
            Vehicle V003 removed.
        """
        current = self.head
        prev = None
        while current:
            if current.vehicle_id == vehicle_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"Vehicle {vehicle_id} removed.")
                return
            prev = current
            current = current.next
        print(f"Vehicle {vehicle_id} not found.")

    def display_fleet(self):
        """
        Print details of all vehicles in the fleet.

        Example:
            >>> fleet = FleetManager()
            >>> fleet.add_vehicle("V004", "car", "available", "Dubai Mall",(25.1985, 55.2796),6)
            >>> fleet.display_fleet()
            ID: V004, Type: car, Status: available, Location: Dubai Mall
        """
        current = self.head
        if not current:
            print("No vehicles in the fleet.")
        while current:
          print(f"ID: {current.vehicle_id}, Type: {current.vehicle_type} Status: {current.status}, Location: {current.location}")
          current = current.next
            
            
    def get_available_vehicles(self):
      """
      Returns a list of all available vehicles in the fleet.
      """
      available = []
      current = self.head
      while current:
        if current.status == "available":
            available.append(current)
        current = current.next
      return available
    
    def update_vehicle_info(self, vehicle_id, driver_id=None, status=None, location=None, location_geo=None):
        """
        Update specified attributes of a vehicle in the fleet.

        Args:
            vehicle_id (str): Unique ID of the vehicle to update.
            driver_id (str, optional): New driver ID.
            status (str, optional): New status of the vehicle (e.g., 'available', 'occupied').
            location (str, optional): New location description.
            location_geo (str, optional): New geographic coordinates.

        Returns:
            bool: True if the vehicle was found and updated, False otherwise.

        Example:
            >>> fleet.update_vehicle_info("V001", status="occupied")
            >>> fleet.update_vehicle_info("V002", location="Dubai Mall", location_geo="25.1975, 55.2790")
        """
        current = self.head
        while current:
            if current.vehicle_id == vehicle_id:
                if driver_id is not None:
                    current.driver_id = driver_id
                if status is not None:
                    current.status = status
                if location is not None:
                    current.location = location
                if location_geo is not None:
                    current.location_geo = location_geo
                return True
            current = current.next
        return False
    
    def get_available_vehicles(self):
        """
        Returns a list of all available vehicles in the fleet.
        """
        available = []
        current = self.head
        while current:
          if current.status == "available":
            available.append(current)
            current = current.next
        return available
    
    def get_vehicle_by_id(self, vehicle_id):
        """
        Retrieves a vehicle from the fleet using its ID.

        Args:
          vehicle_id (str or int): The ID of the vehicle to find.
        Returns:
        Vehicle or None: The vehicle object if found, otherwise None.
        """
        current = self.head
        while current:
          if current.vehicle_id == vehicle_id:
            return current
          current = current.next
        return None
  


