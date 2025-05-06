class User:
    """
    Represents a user in the ride-sharing system.

    Attributes:
        user_id (str): Unique identifier for the user.
        name (str): Name of the user.
        role (str): Either 'driver' or 'passenger'.
        rating (float): Average user rating.
        ride_count (int): Total number of rides completed or taken.
    """

    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.rating = 0.0
        self.ride_count = 0

    def increment_ride_count(self):
        """
        Increments the user's ride count by one.
        """
        self.ride_count += 1

    def update_rating(self, new_rating):
        """
        Updates the average rating using cumulative average.

        Args:
            new_rating (float): The new rating to incorporate.
        """
        total_rating = self.rating * self.ride_count
        self.ride_count += 1
        self.rating = (total_rating + new_rating) / self.ride_count

    def __repr__(self):
        return f"{self.role.capitalize()}({self.name}, Rating: {self.rating:.1f}, Rides: {self.ride_count})"



class UserManager:
    """
    Manages users using a hash map for fast lookups by user ID.

    Example:
        manager = UserManager()
        manager.add_user(User("u123", "Alice", "driver", 4.5, 120))
        manager.get_user("u123")  # returns user object
    """

    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """
        Adds a user to the system.

        Args:
            user (User): A user object.
        """
        self.users[user.user_id] = user

    def get_user(self, user_id):
        """
        Retrieves a user by ID.

        Args:
            user_id (str): The user's unique ID.

        Returns:
            User or None: The user object or None if not found.
        """
        return self.users.get(user_id)

    def remove_user(self, user_id):
        """
        Removes a user from the system.

        Args:
            user_id (str): ID of the user to remove.
        """
        if user_id in self.users:
            del self.users[user_id]

    def all_users(self):
        """
        Returns a list of all users.

        Returns:
            list: All user objects in the system.
        """
        return list(self.users.values())

