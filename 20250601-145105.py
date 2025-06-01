Question 3________________
Write a function called describe_
city() that accepts the name of
a city and its country.
The function should print a simple
sentence, such as
Reykjavik is in Iceland. Give the 
parameter for the country a default
value.
Call your function for three
different cities,

solution _____________
def describe_city(city, country='USA'):
    """Prints a sentence stating which
    country the city is in."""
    print(f"{city} is in {country}.")
describe_city('Reykjavik', 'Iceland')
describe_city('Paris', 'France')
describe_city('New York')  
