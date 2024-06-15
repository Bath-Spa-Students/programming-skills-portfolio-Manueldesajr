'''Using the list sandwich_orders, make sure the sandwich 'pastrami' appears in the list at least three times.\
   Add code near the beginning of your program to print a message saying the deli has run out of pastrami,\
   and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.\
   Make sure no pastrami sandwiches end up in finished_sandwiches.'''

# List of sandwhich orders
sandwich_orders = ['tuna', 'chicken', 'beef', 'veggie', 'turkey', 'pastrami', 'pastrami', 'pastrami']

# A message saying that the deli has run out of pastrami
print("The deli has run out of pastrami.")

# Using a while loop to remove all occurances of pastrami.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove("pastrami")

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
        print(sandwich
