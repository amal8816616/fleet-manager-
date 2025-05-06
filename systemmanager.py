from fleet_manager import FleetManager
from RidePriorityQueue import RidePriorityQueue
from ride_history import RideHistoryManager,RideLog
from user_manager import UserManager, User
from smarttraffic import TrafficManager
from Ride_search_filtering import RideSearchManager,Ride
from NavigationGraph import NavigationGraph
from AVLtree import UserAVLTree
from ride_request import RideRequest,RideRequestQueue  # You can define this simple class in ride_request.py
import math
import random
import uuid
import datetime

class SystemManager:
    """
    Coordinates and manages core operations in the ride-hailing platform.

    This class integrates multiple subsystems including fleet management, ride prioritization,
    ride history, traffic data, user accounts, and ride searching to deliver intelligent ride
    assignment and user service features.
    """

    def __init__(self):
        """
        Initializes all core managers and components required by the system.
        """
        self.fleet_manager = FleetManager()
        self.ride_priority_queue = RidePriorityQueue()
        self.ride_history_manager = RideHistoryManager()
        self.ride_request_queue = RideRequestQueue()
        self.user_manager = UserManager()
        self.traffic_manager = TrafficManager()
        self.ride_search_manager = RideSearchManager()
        self.navigation_graph=NavigationGraph()
        self.tree=UserAVLTree()
        self.ongoing_rides = {}

    def register_user(self, user_details):
        """
        Registers a new user in the system.

        Args:
            user_details (dict): Information needed to create a User object.
        """
        user = User(**user_details)
        self.user_manager.add_user(user)
        #add to tree

    def add_vehicle(self, vehicle_details):
        """
        Adds a vehicle to the fleet for ride allocation.

        Args:
            vehicle_details (dict): Contains vehicle_id, type, location, etc.
        """
        self.fleet_manager.add_vehicle(**vehicle_details)

    def request_ride(self, user_id, location, location_geo, vehicle_type,destination, destination_geo):
        """
        Submits a new ride request from a user.

        Args:
            user_id (str): ID of the requesting user.
            location (str): Textual pickup location.
            location_geo (tuple): Geographical coordinates of pickup location.
            vehicle_type (str): Requested type of vehicle (e.g., 'Sedan', 'SUV')
            next_location (str)  destination
            next_location_geo (tuple):Geographical coordinates of destination
        """
        ride_request = RideRequest(user_id, location, location_geo,destination, destination_geo,vehicle_type)
        self.ride_request_queue.add_request(ride_request)
        self.assign_vehicle_to_ride(ride_request)

    def assign_vehicle_to_ride(self, ride_request):
        """
        Assigns the best available vehicle to the given ride request
        based on location, delay, and urgency using a priority queue.

        Args:
            ride_request (RideRequest): The incoming ride request to fulfill.
        """
        vehicles = self.fleet_manager.get_available_vehicles()
        for vehicle in vehicles:
            distance = self.calculate_distance(vehicle.location_geo, ride_request.location_geo)
            delay = self.traffic_manager.get_delay(vehicle.vehicle_id)
            urgency = self.estimate_urgency(ride_request)

            priority = distance + delay - urgency  # lower is better
            self.ride_priority_queue.add_vehicle(vehicle.vehicle_id, priority)
        
        best_vehicle_id,priority_score = self.ride_priority_queue.get_best_vehicle()
        print(f"Best vehicle: {best_vehicle_id}, priority score: {priority_score}")
        if best_vehicle_id:
          current = self.fleet_manager.head
          while current:
            if current.vehicle_id == best_vehicle_id:
               current.status = "assigned"
               current.next_location = ride_request.destination
               current.next_location_geo = ride_request.destination_geo
               print(f"Assigned vehicle {current.vehicle_id} to user {ride_request.user_id}.")
               self.ongoing_rides[best_vehicle_id] = ride_request
               break
            current = current.next
            

    def search_rides(self, criteria):
        """
        Searches for rides that match specific criteria.

        Args:
            criteria (dict): Dictionary of filters (e.g., user_id, date range).

        Returns:
            list: Matching rides.
        """
        return self.ride_search_manager.search(criteria)

    def view_ride_history(self, user_id):
        """
        Retrieves the ride history for a specific user.

        Args:
            user_id (str): The ID of the user.

        Returns:
            list: List of past rides.
        """
        return self.ride_history_manager.view_history(user_id)

    def rebook_last_ride(self, user_id):
        """
        Attempts to rebook the user's most recent ride.

        Args:
            user_id (str): The ID of the user.
        """
        last_ride = self.ride_history_manager.rebook_last_ride(user_id)
        if last_ride:
            self.request_ride(user_id, last_ride.location, last_ride.vehicle_type)

    def update_traffic(self, vehicle_id, delay):
        """
        Updates the traffic delay for a specific vehicle.

        Args:
            vehicle_id (str): The ID of the vehicle.
            delay (float): Delay in minutes or other units.
        """
        self.traffic_manager.update_traffic(vehicle_id, delay)

    @staticmethod
    def calculate_distance(loc1, loc2):
        """
        Calculates the great-circle distance between two coordinates using the Haversine formula.

        Args:
            loc1 (tuple): (latitude, longitude) of point A.
            loc2 (tuple): (latitude, longitude) of point B.

        Returns:
            float: Distance in kilometers.
        """
        lat1, lon1 = loc1
        lat2, lon2 = loc2
        
        R = 6371.0  # Radius of the Earth in kilometers
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)
        
        a = math.sin(delta_phi / 2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        return distance

    @staticmethod
    def estimate_urgency(ride_request):
        """
        Estimates the urgency score for a ride request (currently randomized).

        Args:
            ride_request (RideRequest): The ride request being evaluated.

        Returns:
            float: An urgency score; higher values indicate higher urgency.
        """
        return random.uniform(0, 5)  # Simulated for now
      
    def end_ride(self, vehicle_id, arrived=True, current_location=None, current_location_geo=None, rating=5.0):
        """
        Ends the ride for the given vehicle and logs it into ride history.
        Args:
          vehicle_id (str): ID of the vehicle ending the ride.
          arrived (bool): Whether the vehicle has reached its destination.
          current_location (str, optional): Used if the vehicle hasn't arrived.
          current_location_geo (str, optional): Coordinates of the current location.
          rating (float): Rating for the ride (default is 5.0).
        """
        current = self.fleet_manager.head
        while current:
          if current.vehicle_id == vehicle_id:
            # Retrieve ride details
            vehicle = self.fleet_manager.get_vehicle_by_id(vehicle_id)
            if vehicle_id not in self.ongoing_rides:
              print(f"❗ Vehicle {vehicle_id} is not currently assigned to any ride.")
              return
            
            ride_request = self.ongoing_rides[vehicle_id]
            if arrived:
               current.location = current.next_location
               current.location_geo = current.next_location_geo
               end_location = current.next_location
            elif current_location and current_location_geo:
                 current.location = current_location
                 current.location_geo = current_location_geo
                 end_location = current_location
            else:
                print(f"❗ Cannot end ride — incomplete location data.")
                return

            current.next_location = None
            current.next_location_geo = None
            current.status = "available"

            # Log ride
            ride_id = str(uuid.uuid4())
            log = RideLog(
              ride_id=ride_id,
              user_id=ride_request.user_id,
              vehicle_id=vehicle_id,
              location=end_location,
              rating=rating
              )
            current_time = datetime.datetime.now()
            ride=Ride(ride_id,end_location,vehicle_id,rating, current_time)
            self.ride_history_manager.add_ride(log)
            self.ride_search_manager.add_ride(ride)
            if vehicle_id in self.ongoing_rides:
               del self.ongoing_rides[vehicle_id]
            print(f"❗ Vehicle {vehicle_id} ride ended.")
            return
          current = current.next

        print(f"❗ Vehicle {vehicle_id} not found in fleet.")

