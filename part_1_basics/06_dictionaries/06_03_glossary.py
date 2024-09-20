glossary = {
    'Variable' : 'A container for storing data values.',
    'String' : "A sequence of characters enclosed in either single quotes ('') or double quotes (“”)",
    'Loop' : 'A statement that allows you to execute a block of code repeatedly.',
    'List' : 'A data structure that stores an ordered sequence of items, or elements, of varying types.',
    'Function' : 'A line of code which only runs when it is called.'
}

for term in glossary:
    print(f"{term}:")
    print(f"\t{glossary[term]}\n")