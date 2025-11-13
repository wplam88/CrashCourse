"""This is a file that contains practice code for classes."""

# 9.1 Restaurant Class
class Restaurant:
    """A simple model of a restaurant."""
    
    def __init__(self, name, cuisine_type):
        """Initialize the restaurant's name and cuisine type."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number

    def increment_number_served(self, increment=1):
        """Increment the number of customers served by a given amount."""
        self.number_served += increment

# 9.2 Three Restaurants
restaurant1 = Restaurant("Pasta Palace", "Italian")
restaurant2 = Restaurant("Sushi Spot", "Japanese")
restaurant3 = Restaurant("Taco Town", "Mexican")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9.3 Users
class User:
    """A simple model of a user."""
    
    def __init__ (self, first_name, last_name, username, email, password):
        """Initialize the user's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f'Hello, {self.first_name}! Great to see you again!')

    def increment_login_attempts(self, increment=1):
        """Increment the number of login attempts."""
        self.login_attempts += increment

    def reset_login_attempts(self):
        """Reset the number of login attempts to zero."""
        self.login_attempts = 0

# 9.4 Three Users
user1 = User("Will", "Lam", "wplam", "lamwillp88@gmail.com", "Discipline88!")
user2 = User("Alice", "Johnson", "alicej", "alicejohnson@example.com", "Password123!")
user3 = User("Bob", "Smith", "bobsmith", "bobsmith@example.com", "MySecurePassword!")

# 9.5 Number Served
restaurant0 = Restaurant("The Dankery", "American")

# Print the initial number served
print(restaurant0.number_served)

# Set the number served to 10
restaurant0.set_number_served(10)
print(restaurant0.number_served)

# Increment the number served by 5
restaurant0.increment_number_served(5)
print(restaurant0.number_served)

# 9.6 Login Attempts

# Increment login attempts
user1.increment_login_attempts(3)
print(user1.login_attempts)

# Reset login attempts
user1.reset_login_attempts()
print(user1.login_attempts)

# 9.7 Ice Cream Stand
class IceCreamStand(Restaurant):
    """A model of an ice cream stand, inheriting from Restaurant."""
    
    def __init__(self, name, cuisine_type="Ice Cream"):
        """Initialize the ice cream stand with a name and default cuisine type."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        """Add a flavor to the ice cream stand."""
        self.flavors.append(flavor)

    def show_flavors(self):
        """Print the available flavors."""
        print(f"{self.name} offers the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Ice Cream Stand Example
ice_cream_stand = IceCreamStand("The Frozone")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.show_flavors()

# 9.8 Admin
class Admin(User):
    """A model of an Admin, inheriting from user."""

    def __init__ (self, first_name, last_name, username, email, password):
        """Initialize the users first name, last name, username, email, and password."""
        super().__init__(first_name, last_name, username, email, password)
        self.privelages = []

    def add_privelages(self, privelage):
        self.privelages.append(privelage)

    def show_privelages(self):
        for privelage in self.privelages:
            print(f"- {privelage}")





