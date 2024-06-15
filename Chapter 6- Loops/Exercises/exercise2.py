'''A movie theater charges different ticket prices depending on a person`s age.\
   If a person is under the age of 3, the ticket is free;\
   if they are between 3 and 12, the ticket is $10;\
   and if they are over age 12, the ticket is $15.\
   Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.'''

# Start an Infinite loop
while True:
    # Prompt the user to enter their age
    age = input("Please enter your age: ")
    # If the user enters 'quit', break the loop
    if age == 'quit':
        break
    # Convert the users input into an integer 
    age = int(age)
    # If the user is under the age 3 years old
    if age < 3:
        # Print that the movie ticket is free
        print("Your movie ticket is free.")
        # If the user is between the ages 3 years and 12 years old 
    elif age <= 12:
        print("Your movie ticket is $10.")
        # If the user is over the age 12 years old.
    else:
        print("Your movie ticket is $15.")
