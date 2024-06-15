'''Think of five programming words you`ve learned about in the previous chapters.\
   Use these words as the keys in your glossary, and store their meanings as values.'''

# Define the glossary 
glossary = {
    "Variable": "A reserved memory location to store values.",
    "Function": "A block of statements that return the specific task.",
    "List": "A mutable, ordered sequence of items; items can be of different types.",
    "Dictionary": "A mutable, collection of unique key-value pairs; fast access to vlaues using keys.",
    "Tuples": "An immutable, ordered sequence of items; items can be of different types."
           }

''' Define the word on the first line, then indent and print its definition on the next line.\
    Use the new line character (\n) to add a blank line between each pair of word and definition in ypur output'''
# Print each word and its meaning
for key, value in glossary.items():
    print(f"{key}:\n\t{value}")
