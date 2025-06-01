def describe_city(city, country='USA'):
    """Prints a sentence stating which country the city is in."""
    print(f"{city} is in {country}.")

# Calling the function for three different cities
describe_city('Reykjavik', 'Iceland')
describe_city('Paris', 'France')
describe_city('New York')  # Uses default country 'USA'