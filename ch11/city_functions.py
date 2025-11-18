# 11.1
def city_country(city, country, population=''):
    "generate a formatted city, county, and (optional) population"
    if population:
        formatted = f'{city.title()}, {country.title()} - population {population}'
    else:
        formatted = f'{city.title()}, {country.title()}'
    return formatted

# 11.3
class Employee:
    "takes in attributes about an employee "

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        attributes = []
    
    def give_raise(self, amount=5000):
        "default $5000 raise unless stated otherwise"
        self.salary += amount

