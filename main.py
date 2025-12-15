def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_words(contents):
    words = contents.split()
    return words


def main():
    file_contents = get_book_text("./books/frankenstein.txt")
    words = count_words(file_contents)
    num_words = len(words)
    print(f"Found {num_words} total words")


main()
