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
    first_item_trigger = 0
    max_player_health = 5
    current_player_health = max_player_health
    ghost_dog_trigger = 0
    chandelier_trigger = 0
    desk_blocking_door_trigger = 0
    wine_cabinet_trigger = 0

    print("\nYou wake up in a strange building, unsure of how you arrived there.\n"
          "One thing is clear: This building is haunted!\n"
          "You will need to explore the mansion in order to find an exit. Good luck!")

    done = False

    while not done:
        print()
        print(room_list[current_room].description)

        for item in item_list:
            if item.room_location == current_room:
                print(item.des_in_room)

        if chandelier_trigger == 0 and current_room == 0:
            print("There is a grand chandelier hanging above you.")
            if random.randrange(0, 16) == 1:
                print("Suddenly, the chandelier seems to shake... violently!")
                dodge_input = input("  Watch out! ")
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

        if chandelier_trigger == 0 and current_room == 14:
            print("You can see the chandelier much more clearly now. "
                  "But, upon further inspection, it seems a bit... unstable.\n"
                  "Perhaps the first floor foyer isn't the safest place to be..")
        elif chandelier_trigger == 1 and current_room == 14:
            print("Looking down, you can see the chandelier, embedded in the center of the foyer.")

        if ghost_dog_trigger == 0 and current_room == 3:
            print("You see a translucent dog sleeping in the dog house. It seems even the dog is ghostly!")
        elif ghost_dog_trigger == 1 and current_room == 3:
            print("The ghost dog is no longer here. You miss his company.")

        if ghost_dog_trigger == 1 and current_room == 1:
            print("The dog is sitting in the courtyard, chewing on the bone.")

        if desk_blocking_door_trigger == 0 and current_room == 7:
            print("There is a desk blocking the doorway out of the bedroom.")
        elif desk_blocking_door_trigger == 1 and current_room == 7:
            print("The desk from before is sitting in the corner of the room, away from the door.")

        if wine_cabinet_trigger == 0 and current_room == 10:
            print("As far as you can tell, you can only go back the way you came from.")
        elif wine_cabinet_trigger == 1 and current_room == 10:
            print("Now that the cabinet is moved, you can see the metal door in the eastern wall.")

        user_input = input("\n  What is your command? ")

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
                print("You go north.")
                previous_room = current_room
                current_room = next_room

        # This is for going east
        elif user_input.lower() == "east" or (user_input.lower() == "go" and second_word.lower() == "east"):
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                print("You go east.")
                previous_room = current_room
                current_room = next_room

        # This is for moving south
        elif user_input.lower() == "south" or (user_input.lower() == "go" and second_word.lower() == "south"):
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                print("You go south.")
                previous_room = current_room
                current_room = next_room

        # This is for moving west
        elif user_input.lower() == "west" or (user_input.lower() == "go" and second_word.lower() == "west"):
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                print("You go west.")
                previous_room = current_room
                current_room = next_room

        # Used for moving up
        elif user_input.lower() == "up" or (user_input.lower() == "go" and second_word.lower() == "up"):
            next_room = room_list[current_room].up
            if next_room is None:
                print("You can't go that way.")
            else:
                print("You go up.")
                previous_room = current_room
                current_room = next_room

        # Used for moving down
        elif user_input.lower() == "down" or (user_input.lower() == "go" and second_word.lower() == "down"):
            next_room = room_list[current_room].down
            if next_room is None:
                print("You can't go that way.")
            elif next_room == 7:
                print("You drop down the hole. \nYou end up landing on a very large bed, unscathed from damage.")
                previous_room = None
                current_room = next_room
            else:
                print("You go down.")
                previous_room = current_room
                current_room = next_room

        # Used for moving back to your previous room. Currently only tracks one room at a time, cannot be used
        # consecutively.
        elif user_input.lower() == "back" or (user_input.lower() == "go" and second_word.lower() == "back"):
            if previous_room is None:
                print("You can't go back to where you were.")
            elif previous_room == current_room:
                print("You are already in this room.")
            else:
                print("You go back.")
                temp = current_room
                current_room = previous_room
                previous_room = temp

        # Used to get items. Maybe should make another for 'pick up'? There is also a trigger being used to see if
        # the player has picked up an item before. If not, it will explain how to check the inventory.
        elif user_input.lower() == "get":
            found = False
            for item in item_list:
                if (second_word == item.name or third_word == item.name) and item.room_location == current_room:
                    item.room_location = -1
                    print("You picked up the", item.name)
                    found = True
                    if first_item_trigger == 0:
                        print("Hint: You can see your current health and items by typing \'inventory\'"
                              "or \'check inventory\'. Give it a try!")
                        first_item_trigger = 1
            if not found:
                print("I don't understand what you typed.")

        # Used to check inventory, consisting of items and health
        elif user_input.lower() == "inventory" or (user_input.lower() == "check" and second_word.lower() == "inventory"):
            inventory_count = 0
            print("Your health is currently", current_player_health, "out of", max_player_health)
            for item in item_list:
                if item.room_location == -1:
                    inventory_count += 1
                    print(item.name, "\n ", item.des_in_inventory)
            if inventory_count == 0:
                print("Your inventory is empty.")

        # Used for dropping items. Dropped items can be picked up in the room they were dropped in.
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

        # This holds the ability to use items. Most items will disappear after a single use.
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
                    elif item.name == "flashlight" and item.room_location == -1:
                        print("You tried to use the flashlight to light your way.")
                        if current_room == 4:
                            room_list[4] = Room("What a large hallway! \nEven with the flashlight on, you will have to "
                                                "walk further down the hallway to see more of it." 
                                                "\nFrom where you are now, you can either walk to the east side of the "
                                                "hallway, or the west side. \n"
                                                "There is a tear in the north wall in front of you, and behind you is"
                                                "the door to the foyer",
                                                north=5, east=6, south=0, west=8, up=None, down=None)
                            used = True
                        elif current_room == 15:
                            room_list[15] = Room("With the light of the flashlight, you can make out several doors.\n"
                                                 "Several of them seem boarded up. You will still need to walk further "
                                                 "down the hallway ahead of you to see the rest.",
                                                 north=16, east=None, south=14, west=None, up=None, down=None)
                            used = True
                        else:
                            print("You cannot use the flashlight here.")
                    elif item.name == "key" and current_room == 12 and item.room_location == -1:
                        # I could probably find some way to adjust the amount of print statements I had to something
                        # smaller and more manageable.
                        print("You used the key on the rusty door, and it creakily swings open.\n"
                              "As you step through the gates, you hear a sudden cackle of laughter from the mansion.\n"
                              "You turn to see.. ghosts! Dozens of ghosts, all focused on you.\n"
                              "You hear one of the ghosts cry out, \"Thanks for all the laughs! "
                              "You'll be back again, won't you?\"\n"
                              "You turn and run. You have no reason to return.\n"
                              "Well... except for the dog.\n"
                              "\nCongrats! You escaped successfully!\n")
                        if item_list[5].room_location == -1:
                            print("You even found the secret totem! You've done well!")
                        print("Thank you for playing!")
                        done = True
            if not used:
                print("You do not have this item yet.")

        # Used for moving or pushing the cabinet or the desk away from their respective doors.
        elif user_input.lower() == "move" or user_input.lower() == "push":
            if second_word == "desk" or (second_word == "the" and third_word == "desk"):
                if desk_blocking_door_trigger == 0 and current_room == 7:
                    print("You push the desk out of the way of the door, allowing you to use the door.")
                    desk_blocking_door_trigger = 1
                    room_list[7] = Room("You are in the master bedroom. \n"
                                        "You spot a queen sized bed, a fancy fur rug, and an elegant mirror. \n"
                                        "You also notice the hole in the ceiling. There is a door on the south wall.",
                                        north=None, east=None, south=6, west=None, up=None, down=None)
                    room_list[6] = Room("You walk east down the hallway, keeping your hand to the wall for safety. \n"
                                        "From here, there is a door in the north wall, and the hallway to the west "
                                        "where you came from.",
                                        north=7, east=None, south=None, west=4, up=None, down=None)
                else:
                    print("You can't do that here.")
            elif second_word == "cabinet" or (second_word == "the" and third_word == "cabinet"):
                if current_room == 10 and wine_cabinet_trigger == 0:
                    print("You push the wine cabinet, and it slides away easily. \n"
                          "You can now see a large metal door that was previously being obscured from view.")
                    wine_cabinet_trigger = 1
                    room_list[10] = Room("You are met with a grand dining hall, fit to serve over a dozen people. \n"
                                         "You can see trolleys for transporting the food, and the eastern wall is "
                                         "fitted with a large wine cabinet.",
                                         north=None, east=11, south=8, west=None, up=None, down=None)
                else:
                    print("You can't do that here.")
            else:
                print("You can't do that here.")

        # Lets the player search things, currently only for checking the doghouse
        elif user_input.lower() == "search":
            if second_word == "doghouse":
                if current_room == 3 and ghost_dog_trigger == 1:
                    print("You searched around the doghouse and discovered a picture lying on the ground!\n"
                          "You pick up the picture, wiping the dog slobber off of it.")
                    item_list[4].room_location = -1
                elif current_room == 3 and ghost_dog_trigger == 0:
                    print("You try to search the doghouse, but the dog bites you!\n"
                          "You will need to find a way to get the dog out of the doghouse.")
                    current_player_health -= 2
                else:
                    print("You can't do that here.")
            else:
                print("I don't understand what you typed.")

        # Gives the ability to pet the dog.
        elif user_input.lower() == "pet" or (user_input.lower() == "pet" and second_word.lower() == "dog"):
            if ghost_dog_trigger == 0 and current_room == 3:
                print("The dog growls before biting you on the arm!")
                print("You stumble back, away from the dog. It seems it doesn't trust you enough.")
                current_player_health -= 2
            elif ghost_dog_trigger == 1 and current_room == 1:
                print("You pet the dog, and they smile. You are certainly their friend now.")

        # Quitting the game
        elif user_input.lower() == "quit" or (user_input.lower() == "quit" and second_word.lower() == "game"):
            done = True

        else:
            print("I don't understand what you typed.")

        # If the player loses enough health, they die.
        if current_player_health <= 0:
            print("You fall back, defeated by your injuries, and you black out to the sound of cackling laughter.")
            print("Game over!")
            done = True


main()
restart_input = input("\n  Would you like to play again? ")
if restart_input.lower() == "yes":
    main()
else:
    print("Thank you for playing!")
