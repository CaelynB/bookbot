from stats import book_word_count

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
    # print the book text from the specified file.
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

    # count the total number of words in the book text.
    word_count = book_word_count(book_text)
    print(f"{word_count} words found in the document")

main()