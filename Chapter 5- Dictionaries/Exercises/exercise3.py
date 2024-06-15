'''add five more Python terms to your glossary.When you run your program again,\
   these new words and meanings should automatically be included in the output.'''

# define the glossary 
glossary = {
    "Variable": "A reserved memory location to store values.",
    "Function": "A block of statements that return the specific task.",
    "List": "A mutable, ordered sequence of items; items can be of different types.",
    "Dictionary": "A mutable, collection of unique key-value pairs; fast access to vlaues using keys.",
    "Tuples": "An immutable, ordered sequence of items; items can be of different types.",
    "Integers": "A whole number.",
    "String": "A sequence of characters.",
    "Boolean": "A type that has two values, TRUE and FALSE.",
    "Loop": "A series of instructions that is continually repeated until a certin condition is reached.",
    "Float": "A number that has a decimal point."
          }

'''Define the word on the first line, then indent and print its definition on the next line.\
    Use the new line character (\n) to add a blank line between each pair of word and definition in ypur output'''
# Print each word and it`s meaning
for key, value in glossary.items():
    print(f"{key}:\n\t{value}\n")
