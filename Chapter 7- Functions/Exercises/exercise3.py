'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.\  
   The function should print a sentence summarizing the size of the shirt and the message printed on it.\
   Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.'''

# Define a function called make_shirt that accepts two parameters, size and message.
def make_shirt(size, message):
    # The function prints a sentence summarizing the size of the shirt and the message printed on it.
    print(f"The size of the shirt is {size} and the message printed on it is '{message}'. ")

# Call the function with positional arguments to make a shirt. 
make_shirt("Large", "stay on vibe")

# Call the function a second time with key-word arguments.
make_shirt(size='Medium', message='Be yourself!') 
