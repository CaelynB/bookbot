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

    # for each character in the text.
    for char in text:
        # if the character is already in the dictionary, increment its count.
        if char in character_counts:
            character_counts[char] += 1
        # otherwise, add it to the dictionary with a count of 1.
        else:
            character_counts[char] = 1

    # return the character counts dictionary.
    return character_counts

def sorted_list(character_counts):
    """
    sorts the character count dictionary by the number of occurrences.
    
    :param character_counts: A dictionary with characters as keys and their counts as values.
    :return: A sorted list of tuples (character, count) in descending order.
    """

    # sort the character counts in descending order.
    for char, count in sorted(character_counts.items(), key=lambda item: item[1], reverse=True):
        # if the character is an alphabetic character, print it.
        if char.isalpha():
            print(f"{char}: {count}")