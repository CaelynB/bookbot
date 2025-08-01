from sys import argv
from stats import book_word_count, repeat_character_count, sorted_list

def get_book_text(filename):
    """
    reads the content of a book from a file and returns it as a string.
    
    :param filename: The name of the file containing the book text.
    :return: The content of the book as a string.
    """

    # attempt to open the file and read its content.
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "The specified book file does not exist."

def main():
    # if no file path is provided, print usage instructions and exit.
    if len(argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    # get the file path from the command line arguments.
    file_path = argv[1]

    # read the book text from the specified file.
    book_text = get_book_text(file_path)

    # count the total number of words in the book text.
    word_count = book_word_count(book_text)

    # count the occurrences of each character in the book text.
    character_stats = repeat_character_count(book_text)

    # print the analysis results.
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    sorted_list(character_stats)
    print("============= END ===============")

main()