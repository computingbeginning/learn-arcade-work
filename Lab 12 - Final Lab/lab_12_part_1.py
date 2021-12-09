import random
from room import Room
from create_rooms import create_rooms
from items import Item
from create_items import create_items


def main():
    room_list = create_rooms()
    item_list = create_items()

    current_room = 0
    previous_room = None
    chandelier_trigger = 0
    max_player_health = 5
    current_player_health = max_player_health
    ghost_dog_trigger = 0

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

        if chandelier_trigger == 0 and current_room == 0:
            print("There is a grand chandelier hanging above you.")
            if random.randrange(0, 21) == 1:
                print("Suddenly, the chandelier seems to shake... violently!")
                dodge_input = input("Watch out! ")
                if dodge_input.lower() == "move" or dodge_input.lower() == "dodge":
                    print("You move out of the way in the nick of time, as the chandelier crashes to the ground!")
                    print("You can hear distant laughter. You are certainly not alone in this place.")
                    chandelier_trigger = 1
                else:
                    print("This was not the correct command.")
                    print("The chandelier crashes to the ground, pummelling you into the ground.")
                    current_player_health -= 3
                    if current_player_health >= 1:
                        print("Surprisingly, you survived, but you took three points of damage.")
                        print("You crawl out from under the chandelier, and you hear the cackling of distant laughter.")
                        chandelier_trigger = 1
                    else:
                        print("This is your unfortunate end, and you hear the cackling of laughter as your life ends.")
                        print("\nGame Over!")
                        done = True
        elif current_room == 0 and chandelier_trigger == 1:
            print("The large chandelier sits in the middle of the foyer, still elegant despite being shattered.")

        if ghost_dog_trigger == 0 and current_room == 3:
            print("You see a translucent dog sleeping in the dog house. It seems even the dog is ghostly!")
        elif ghost_dog_trigger == 1 and current_room == 3:
            print("The ghost dog is no longer here. You miss his company.")

        if ghost_dog_trigger == 1 and current_room == 1:
            print("The dog is sitting in the courtyard, chewing on the bone.")

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
                previous_room = current_room
                current_room = next_room

        # This is for going east
        elif user_input.lower() == "east" or (user_input.lower() == "go" and second_word.lower() == "east"):
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                previous_room = current_room
                current_room = next_room

        # This is for moving south
        elif user_input.lower() == "south" or (user_input.lower() == "go" and second_word.lower() == "south"):
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                previous_room = current_room
                current_room = next_room

        # This is for moving west
        elif user_input.lower() == "west" or (user_input.lower() == "go" and second_word.lower() == "west"):
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                previous_room = current_room
                current_room = next_room

        # Used for moving up
        elif user_input.lower() == "up" or (user_input.lower() == "go" and second_word.lower() == "up"):
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way.")
            else:
                previous_room = current_room
                current_room = next_room

        # Used for moving down
        elif user_input.lower() == "down" or (user_input.lower() == "go" and second_word.lower() == "down"):
            next_room = room_list[current_room].down
            if next_room is None:
                print("You can't go that way.")
            else:
                previous_room = current_room
                current_room = next_room

        elif user_input.lower() == "back" or (user_input.lower() == "go" and second_word.lower() == "back"):
            if previous_room is None:
                print("You can't go back to where you were.")
            else:
                current_room = previous_room

        elif user_input.lower() == "get":
            found = False
            for item in item_list:
                if (second_word == item.name or third_word == item.name) and item.room_location == current_room:
                    item.room_location = -1
                    print("You picked up the", item.name)
                    found = True
            if not found:
                print("I don't understand what you typed.")

        elif user_input.lower() == "inventory" or (user_input.lower() == "check" and second_word.lower() == "inventory"):
            inventory_count = 0
            print("Your health is currently", current_player_health, "out of", max_player_health)
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
            used = False
            for item in item_list:
                if (item.name == second_word or item.name == third_word) and item.room_location == -1:
                    print("You tried to use the", item.name)
                    # Maybe put the item uses here.
                    if item.name == "ice" and current_room == 9 and item.room_location == -1:
                        print("You put the ice down on the stove and turned it on.")
                        print("Soon, the ice has completely thawed, revealing a large bone.")
                        print("You take the bone and put it in your inventory.")
                        item_list[0].room_location = -3
                        item_list[3].room_location = -1
                        used = True
                    elif item.name == "bone" and current_room == 3 and item.room_location == -1:
                        print("You hold the bone up and the dog's ears perk up.")
                        print("You chuck the bone and the dog chases after it.")
                        ghost_dog_trigger = 1
                        item_list[3].room_location = -3
                        item_list[4].room_location = 3
                        used = True
                    elif item.name == "key" and current_room == 12 and item.room_location == -1:
                        # I could probably find some way to adjust the amount of print statements I had to something
                        # smaller and more manageable.
                        print("You used the key on the rusty door, and it creakily swings open.")
                        print("As you step through the gates, you hear a sudden cackle of laughter from the mansion.")
                        print("You turn to see.. ghosts! Dozens of ghosts, all focused on you.")
                        print("You hear one of the ghosts cry out, \"You'll be back again, won't you?\"")
                        print("You turn and run. You have no reason to return.\n")
                        print("Well... except for the dog.\n")
                        print("\nCongrats! You escaped successfully! Thank you for playing!")
                        done = True
            if not used:
                print("You do not have this item yet.")

        # Gives the ability to pet the dog.
        elif user_input.lower() == "pet" or (user_input.lower() == "pet" and second_word.lower() == "dog"):
            if ghost_dog_trigger == 0 and current_room == 3:
                print("The dog growls before biting you on the arm!")
                print("You stumble back, away from the dog. It seems it doesn't trust you enough.")
                current_player_health -= 2
            elif ghost_dog_trigger == 1 and current_room == 3:
                print("You pet the dog, and they smile. You are certainly their friend now.")

        elif user_input.lower() == "quit" or (user_input.lower() == "quit" and second_word.lower() == "game"):
            done = True

        else:
            print("I don't understand what you typed.")

        if current_player_health <= 0:
            print("You fall back, defeated by your injuries, and you black out to the sound of laughter.")
            print("Game over!")
            done = True


main()
restart_input = input("Would you like to play again? ")
if restart_input.lower() == "yes":
    main()
else:
    print("Thank you for playing!")
