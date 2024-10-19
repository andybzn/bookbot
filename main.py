def main():
    path_to_book = "books/frankenstein.txt"
    book_content = read_book(path_to_book)
    word_count = count_words(book_content)
    character_count = count_characters(book_content)
    characters_sorted = make_dict_list(character_count)

    print("---------------------------------------------------")
    print(f" BOOK REPORT: {path_to_book}")
    print("---------------------------------------------------")
    print(f"This book contains {word_count} words \n")
    for item in characters_sorted:
        if item["char"].isalpha():
            print(f"The character `{item["char"]}` was found {item["count"]} times")
    print("\n---------------------------------------------------")
    print(" REPORT END")
    print("---------------------------------------------------")


def read_book(file_path):
    with open(file_path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts


def make_dict_list(dict):
    list = []
    for key in dict:
        list.append({"char": key, "count": dict[key]})
    list.sort(reverse=True, key=sort_on)
    return list


def sort_on(dict):
    return dict["count"]


main()
