import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)


def main():
    dictionary_file = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()
        dictionary_list.append(line)

    dictionary_file.close()

    print("--- Linear Search ---")

    book_file = open("AliceInWonderLand200.txt")

    current_line_pos = 0

    for line in book_file:
        current_line_pos += 1
        word_list = split_line(line)
        for word in word_list:
            current_list_pos = 0
            while current_list_pos < len(dictionary_list) and dictionary_list[current_list_pos] != word.upper():
                current_list_pos += 1
            if current_list_pos == len(dictionary_list):
                print("Line", current_line_pos, " possible misspelled word:", word)

    book_file.close()

    print("--- Binary Search ---")

    book_file = open("AliceInWonderLand200.txt")

    current_line_pos = 0

    for line in book_file:
        current_line_pos += 1
        word_list = split_line(line)
        for word in word_list:
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False
            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2
                if dictionary_list[middle_pos] < word.upper():
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > word.upper():
                    upper_bound = middle_pos - 1
                else:
                    found = True
            if not found:
                print("Line", current_line_pos, " possible misspelled word:", word)

    book_file.close()


main()
