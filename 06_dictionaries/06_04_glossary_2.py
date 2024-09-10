glossary = {
    'Variable': 'A container for storing data values.',
    'String': "A sequence of characters enclosed in either single quotes ('') or double quotes (\" \").",
    'Loop': 'A statement that allows you to execute a block of code repeatedly.',
    'List': 'A data structure that stores an ordered sequence of items, or elements, of varying types.',
    'Function': 'A line of code which only runs when it is called.',
    'Dictionary': 'A data structure that stores pairs of keys and values. Each key is unique and maps to a value.',
    'Tuple': 'An immutable sequence of elements; its elements cannot be modified.',
    'Python': 'A high-level programming language known for its readability and simplicity.',
    'C++': 'A high-level programming language that includes object-oriented, procedural, and generic programming features.',
    'Import': 'A statement used to include the code from one module into another or a library.'
}

for k, v in glossary.items():
    print(f"A {k} is {v.lower()}")