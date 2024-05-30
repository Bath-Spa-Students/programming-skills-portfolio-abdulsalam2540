def describe_city(city, country='Unknown'):
    """Prints a simple sentence describing the city and its country."""
    print(f"{city} is in {country}.")

# Call the function for three different cities
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York", "USA")
