#!/usr/bin/python.py
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ? and:

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text based on the specified characters
    sentences = [sentence.strip() for char in ['.', '?', ':'] for sentence in text.split(char)]

    # Print each sentence with 2 new lines
    for sentence in sentences:
        print(sentence)
        print()

