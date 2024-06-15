'''Make a list called sandwich_orders and fill it with the names of various sandwiches.\
   Then make an empty list called finished_sandwiches.
   Loop through the list of sandwich orders and print a message for each order,\
   such as I made your tuna sandwich. As each sandwich is made, 
   move it to the list of finished sandwiches. After all the sandwiches have been made,\
   print a message listing each sandwich that was made.'''

# List of sandwhich orders
sandwich_orders = ['tuna', 'chicken', 'beef', 'veggie', 'turkey']

# Empty list for finished sandwhiched
finished_sandwiches = []

# Start a loop that will iterate over each item in 'sandwich_orders'list.
for sandwich in sandwich_orders:

    # Print a message for each order that has been made.
    print(f"I made you {sandwich} sandwich.")

    # As each sandwich is made, move it to the list of 'finished_sandwiches'
    # This line adds the current sandwich to the 'finished_sandwiched', indicating that it had been made.
    finished_sandwiches.append(sandwich)   

    # Print a message listing each sandwich that was made
    print("\nThe following sandwiched have been made:")
    for sandwich in finished_sandwiches:
        print(sandwich)
