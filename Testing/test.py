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
    current_list_position = 0

    while current_list_position < len(name_list) and name_list[current_list_position] != key:
        current_list_position += 1

    if current_list_position < len(name_list):
        print("Found at:", current_list_position)
    else:
        print("Not found.")


main()
