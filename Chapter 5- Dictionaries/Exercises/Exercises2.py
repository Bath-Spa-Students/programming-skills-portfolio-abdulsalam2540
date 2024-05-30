# Glossary dictionary with programming words and their meanings
glossary = {
    'variable': 'A storage location paired with an associated symbolic name, which contains some known or unknown quantity of information referred to as a value.',
    'function': 'A block of organized, reusable code that is used to perform a single, related action.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is reached.',
    'dictionary': 'A collection of key-value pairs, where each key is unique and is used to store and retrieve data efficiently.',
    'list': 'A collection which is ordered and changeable. Allows duplicate members.'
}

# Print each word and its meaning with neat formatting
for word, meaning in glossary.items():
    print(f"{word.capitalize()}:\n{meaning}\n")
