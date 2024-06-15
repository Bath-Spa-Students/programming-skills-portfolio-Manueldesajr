# List of places to visit
places = ["US", "Paris", "London", "Canada", "Brazi"]

# Print the list in its original order
print("Original order:", places)

# Print the list in alphabetical order without modifying the actual list
print("Alphabetical order:", sorted(places))

# Show that the list is still in its original order
print("Original order:", places)

# Print the list in reverse alphabetical order without modifying the actual list
print("Reverse alphabetical order:", sorted(places, reverse=True))

# Show that the list is still in its original order
print("Original order:", places)

# Use reverse() to change the order of the list and print it
places.reverse()
print("Reversed order:", places)

# Use reverse() again to change the order of the list back to the original and print it
places.reverse()
print("Original order:", places)

# Use sort() to change the list so it's stored in alphabetical order and print it
places.sort()
print("Alphabetical order:", places)

# Use sort() to change the list so it's stored in reverse alphabetical order and print it
places.sort(reverse=True)
print("Reverse alphabetical order:", places)
