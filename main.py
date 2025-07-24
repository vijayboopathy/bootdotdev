from stats import words_in_book
from stats import chars_in_book
from stats import dict_to_list
from stats import sort_on

def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents

def pretty_print(book_path):
    file_contents = get_book_text(book_path)
    number_of_words = words_in_book(file_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {number_of_words} total words")
    print("-------- Character Count --------")

    char_count = chars_in_book(file_contents)
    char_list = dict_to_list(char_count)
    char_list.sort(reverse=True, key=sort_on)

    for x in char_list:
        print(x["char"] + ": " + str(x["num"]))

    print("============ END ==============")
    


def main():
    pretty_print("books/frankenstein.txt")

if __name__ == "__main__":
    main()
