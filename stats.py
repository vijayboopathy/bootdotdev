import time

def words_in_book(file_contents):
    words = file_contents.split()
    return len(words)

def chars_in_book(file_contents):
    # print(f"printing file content")
    # time.sleep(2)
    # print(file_contents)
    char_count = {}
    for char in file_contents:
        # print("I'm getting executed till here")
        # time.sleep(5)
        print(char)
        if char.isalpha() == True:
            char = char.lower()
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        print(char_count)
        return char_count

def dict_to_list(char_count_dict):
    char_list = []
    for k, v in char_count_dict.items():
        char_list.append({"char": k, "num": v})
    return char_list

def sort_on(char_list):
    return char_list["num"]
