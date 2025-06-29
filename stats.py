def book_word_count(text):
    """
    counts the number of words in the book text.
    
    :param text: The content of the book as a string.
    :return: The number of words in the book text.
    """

    # split the text into words and count them.
    return len(text.split())

def repeat_character_count(text):
    """
    counts the number of times a specific character appears in the book text.

    :param text: The content of the book as a string.
    :return: The number of times a character appears in the book text.
    """

    # convert the text to lowercase to ensure case-insensitivity.
    text = text.lower()

    # create a dictionary to hold the character counts.
    character_counts = {}

    for char in text:
        # increment the count for each character in the dictionary.
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1

    return character_counts