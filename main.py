from stats import count_characters

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]
    book_content = read_book(path_to_book)
    word_count = count_words(book_content)
    character_count = count_characters(book_content)
    characters_sorted = make_dict_list(character_count)

    print("---------------------------------------------------")
    print(f" BOOK REPORT: {path_to_book}")
    print("---------------------------------------------------")
    print(f"Found {word_count} total words \n")
    for item in characters_sorted:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("\n---------------------------------------------------")
    print(" REPORT END")
    print("---------------------------------------------------")


def read_book(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def make_dict_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "count": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(dict):
    return dict["count"]


main()
