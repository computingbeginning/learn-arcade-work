import random
from room import Room
from create_rooms import create_rooms
from items import Item
from create_items import create_items


def main():
    room_list = create_rooms()
    item_list = create_items()

    current_room = 0
    chandelier_trigger = 0
    player_health = 5

    print("You wake up in a strange building, unsure of how you arrived there.\n"
          "One thing is clear: This building is haunted!\n"
          "You will need to explore the mansion in order to find an exit. Good luck!\n")

    done = False

    while not done:
        print()
        print(room_list[current_room].description)

        for item in item_list:
            if item.room_location == current_room:
                print(item.des_in_room)

        # if chandelier_trigger == 0 and current_room == 0:
            # if random.randrange(1, 21) == 1:
                # print()

        user_input = input("What is your command? ")

        command_words = user_input.split(" ")

        user_input = command_words[0]

        if len(command_words) == 2:
            second_word = command_words[1]
        else:
            second_word = None

        if len(command_words) == 3:
            third_word = command_words[2]
        else:
            third_word = None

        # This is for going north
        if user_input.lower() == "north" or (user_input.lower() == "go" and second_word.lower() == "north"):
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # This is for going east
        elif user_input.lower() == "east" or (user_input.lower() == "go" and second_word.lower() == "east"):
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # This is for moving south
        elif user_input.lower() == "south" or (user_input.lower() == "go" and second_word.lower() == "south"):
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # This is for moving west
        elif user_input.lower() == "west" or (user_input.lower() == "go" and second_word.lower() == "west"):
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Used for moving up
        elif user_input.lower() == "up" or (user_input.lower() == "go" and second_word.lower() == "up"):
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        # Used for moving down
        elif user_input.lower() == "down" or (user_input.lower() == "go" and second_word.lower() == "down"):
            next_room = room_list[current_room].down
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "get":
            for item in item_list:
                if item.name == second_word.lower() and item.room_location == current_room:
                    item.room_location = -1
                    print("You picked up the", item.name)
                elif item.name == third_word.lower() and item.room_location == current_room:
                    item.room_location -= 1
                    print("You picked up the", item.name)
                else:
                    print("I don't understand what you typed.")

        elif user_input.lower() == "inventory" or (user_input.lower() == "check" and second_word.lower() == "inventory"):
            inventory_count = 0
            for item in item_list:
                if item.room_location == -1:
                    inventory_count += 1
                    print(item.name, "\n", item.des_in_inventory)
            if inventory_count == 0:
                print("Your inventory is empty.")

        elif user_input.lower() == "drop":
            for item in item_list:
                if item.name == second_word.lower() and item.room_location == -1:
                    confirm_input = input("Are you sure you want to drop this item? ")
                    if confirm_input.lower() == "yes":
                        item.room_location = current_room
                        print("You dropped the item.")
                    elif confirm_input.lower() == "no":
                        print("You did not drop the item.")
                    else:
                        print("I didn't understand what you typed, so the item was not dropped.")

        elif user_input.lower() == "use":
            for item in item_list:
                if (item.name == second_word.lower() or item.name == third_word.lower()) and item.room_location == -1:
                    print("You tried to use the", item.name)
                    # Maybe put the item uses here.
                elif (item.name == second_word.lower() or item.name == third_word.lower()) and item.room_location != -1:
                    print("You do not have this item yet.")

        elif user_input.lower() == "quit" or (user_input.lower() == "quit" and second_word.lower() == "game"):
            done = True

        else:
            print("I don't understand what you typed.")


main()
