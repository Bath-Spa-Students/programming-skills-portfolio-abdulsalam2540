# Initial glossary dictionary with five programming words and their meanings
glossary = {
    'variable': 'A storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is reached.',
    'dictionary': 'A collection of key-value pairs, where each key is unique and is used to store and retrieve data efficiently.',
    'list': 'A collection which is ordered and changeable. Allows duplicate members.'
}

# Add five more Python terms to the glossary
glossary.update({
    'tuple': 'A collection which is ordered and unchangeable. Allows duplicate members.',
    'set': 'A collection which is unordered and unindexed. No duplicate members are allowed.',
    'conditional': 'Statements that only run when a certain condition is true.',
    'string': 'A sequence of characters used to represent text.',
    'boolean': 'A data type that can hold one of two values: True or False.'
})

# Loop through the dictionary and print each word and its meaning with neat formatting
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n{meaning}\n")
