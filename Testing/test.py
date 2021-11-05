def main():
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open("super_villains.txt")

    name_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        line = line.strip()
        name_list.append(line)
        # print(line)

    my_file.close()
    print("There were", len(name_list), "names in the file.")

    key = "Draco of Viridian"

    lower_bound = 0
    upper_bound = len(name_list) - 1
    found = False

    while lower_bound <= upper_bound and not found:
        middle_pos = (lower_bound + upper_bound) // 2

        if name_list[middle_pos] < key:
            lower_bound = middle_pos + 1

        elif name_list[middle_pos] > key:
            upper_bound = middle_pos - 1

        else:
            found = True

    if found:
        print("Found at position:", middle_pos)

    if not found:
        print("Not found.")


main()

log2(n)  # quiz thing
