# Define a dictionary with major rivers and the countries they run through
rivers = {
    "Nile": "Egypt",
    "Ganges River": "Amazon",
    "Mississippi River": "North America"
          }

# Loop through the dictionary and print and print a sentence about each river.
for river, country in rivers.items():
    print(f"The {river} run through {country}.")

# Print the name of each river
for river in rivers.keys():
    print(river)

# Print the name of each country
for country in rivers.values():
    print(country) 
