'''Write a function called describe_city() that accepts the name of a city and its country.
   The function should print a simple sentence, such as Reykjavik is in Iceland.
   Give the parameter for the country a default value.
   Call your function for three different cities, at least one of which is not in the default country.'''

# Define a function called 'describe_city' that accepts two parameters, city and country 
# Set the default value for a country as 'UAE'
def describe_city(city, country='UAE'):
    # The function prints a sentence describing the city and its country.
    print(f"{city} is in {country}. ")

# Call the functions for three different cities.
describe_city("Dubai")
describe_city("Ajman")
describe_city("sharjah")
