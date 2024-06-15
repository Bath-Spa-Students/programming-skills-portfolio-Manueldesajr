'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.\
   Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.'''

# Define a function called make_shirt that accepts two parameters, size and message.
# Set the default values for size as 'large' and message as 'I love python'.
def make_shirt(size='Large', message='I love Python'):
    # The function prints a message summarizing the size of the shirt and the message printed on it.
    print(f"The size of the shirt is {size} and the message printed on it is '{message}'. ")

# Call the function with no arguments to make a large shirt with the default message. 
make_shirt()

# Call the function with one argument to make a mediu shirt with the default meassage.
make_shirt(size='Medium')

# Call the function with two arguments to make a shirt of any size with a different message.
make_shirt(size='small', message='stay on vibe')
