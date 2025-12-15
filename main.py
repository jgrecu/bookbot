from webbrowser import get
from stats import get_num_words, get_chars, get_chars_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    num_words = get_num_words(file_contents)
    chars_dict = get_chars(file_contents)
    chars_list = get_chars_list(chars_dict)
    print("=========== BOOKBOT ============")
    print(f"Analyzing {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in chars_list:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
