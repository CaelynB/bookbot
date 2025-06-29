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

def sorted_list(character_counts):
    """
    sorts the character count dictionary by the number of occurrences.
    
    :param character_counts: A dictionary with characters as keys and their counts as values.
    :return: A sorted list of tuples (character, count) in descending order.
    """

    # sort the character counts in descending order and print them.
    for char, count in sorted(character_counts.items(), key=lambda item: item[1], reverse=True):
        # only print alphabetic characters.
        if char.isalpha():
            print(f"{char}: {count}")