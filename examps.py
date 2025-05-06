# Example of initializing the system and using the methods
karim = SystemManager()

# Register a driver
karim.register_user({
    'user_id': 1,
    'name': 'Ali',
    'role': 'driver'
})

# Register a driver
karim.register_user({
    'user_id': 2,
    'name': 'Mohammed',
    'role': 'driver'
})

# Register a driver
karim.register_user({
    'user_id': 3,
    'name': 'Fatma',
    'role': 'driver'
})


# Register a driver
karim.register_user({
    'user_id': 4,
    'name': 'Yousef',
    'role': 'driver'
})

# Register a passenger
karim.register_user({
    'user_id': 5,
    'name': 'Sara',
    'role': 'passenger',
})

# Register a passenger
karim.register_user({
    'user_id': 6,
    'name': 'Nassir',
    'role': 'passenger',
})

# Register a passenger
karim.register_user({
    'user_id': 7,
    'name': 'Abd',
    'role': 'passenger',
})

# Add a vehicle to the fleet
karim.add_vehicle({
  'vehicle_id':1, 
  'vehicle_type':'car',
  'status':'available',
  'location':'Burj Khalifa',
  'location_geo':(25.1972, 55.2744),
  'driver_id':1
})

# Add a vehicle to the fleet
karim.add_vehicle({
  'vehicle_id':2, 
  'vehicle_type':'bike',
  'status':'available',
  'location':'Dubai Marina',
  'location_geo':(25.0772, 55.1330),
  'driver_id':2
})

# Add a vehicle to the fleet
karim.add_vehicle({
  'vehicle_id':3, 
  'vehicle_type':'bus',
  'status':'available',
  'location':'Burjuman Metro Station',
  'location_geo':(25.2528, 55.3032),
  'driver_id':3
})


# Add a vehicle to the fleet
karim.add_vehicle({
  'vehicle_id':4, 
  'vehicle_type':'car',
  'status':'available',
  'location':'Dubai Mall',
  'location_geo':(25.1985, 55.2796),
  'driver_id':4
})


# Passenger requests a ride
karim.request_ride(user_id='passenger102', location='JBR', location_geo=(25.0773, 55.1344), destination='Mall of the Emirates', destination_geo=(25.1180, 55.2000), vehicle_type='car')
karim.end_ride(2)


ride1 = Ride("r001", "Downtown", "Car", 4.5, "2025-04-22")
ride2 = Ride("r002", "JBR", "Car", 4, "2025-04-22")
ride2 = Ride("r003", "Marina", "Car", 4, "2025-04-22")
karim.ride_search_manager.add_ride(ride1)
karim.ride_search_manager.add_ride(ride2)
karim.ride_search_manager.add_ride(ride2)
karim.ride_search_manager.search(location='Downtown', vehicle_type='Car')


# add vehicles

karim.traffic_manager.add_vehicle("V101", 10) 
karim.traffic_manager.add_vehicle("V102", 5)

#get next vehicle
print(karim.traffic_manager.get_next_vehicle())

# update vehicle delay
karim.traffic_manager.update_vehicle_delay("V102", 7)


