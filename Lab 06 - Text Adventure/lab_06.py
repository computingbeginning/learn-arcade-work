class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    room_list = []
    room0 = Room("The Foyer of the mansion is grand, decorated with paintings and candlabras on the wall.\n"
                 "A chandelier hangs above the center of the room.\n"
                 "There are two doors present, one in the north face of the room, and one in the south face.",
                 4,
                 None,
                 1,
                 None)
    room_list.append(room0)

    room1 = Room("The full moon above illuminates the large courtyard. \n"
                 "The courtyard is filled with wilted flowers and a flowing fountain. \n"
                 "The east side of the courtyard has a tool shed, and the east side has a dog house. \n"
                 "The north shows the entrance to the mansion, and the south shows the locked gate.)",
                 0,
                 2,
                 12,
                 3)
    room_list.append(room1)

    room2 = Room("Tool Shed",
                 None,
                 None,
                 None,
                 1)
    room_list.append(room2)

    room3 = Room("Dog house with ghost dog",
                 None,
                 1,
                 None,
                 None)
    room_list.append(room3)

    room4 = Room("What a large hallway!\n"
                 "You are not able to see down to either end from where you are.\n"
                 "From where you are now, you can see two doors in front of you.",
                 5,
                 6,
                 0,
                 8)
    room_list.append(room4)

    room5 = Room("hole in wall",
                 None,
                 None,
                 4,
                 None)
    room_list.append(room5)

    room6 = Room("east hallway",
                 7,
                 None,
                 None,
                 4)
    room_list.append(room6)

    room7 = Room("Unnamed room",
                 None,
                 None,
                 6,
                 None)
    room_list.append(room7)

    room8 = Room("west hallway",
                 10,
                 4,
                 9,
                 None)
    room_list.append(room8)

    room9 = Room("Kitchen",
                 8,
                 None,
                 None,
                 None)
    room_list.append(room9)

    room10 = Room("Dining hall",
                  None,
                  11,
                  8,
                  None)
    room_list.append(room10)

    room11 = Room("Hidden room",
                  None,
                  11,
                  8,
                  None)
    room_list.append(room11)

    room12 = Room("Locked Gate",
                  None,
                  11,
                  8,
                  None)
    room_list.append(room12)

    current_room = 0

    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        user_input = input("Where would you like to go? ")
        if user_input.lower() == "north":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "east":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "south":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "west":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_input.lower() == "quit" or user_input.lower() == "quit game":
            done = True

        else:
            print("I don't understand what you typed.")


main()
print("Whats up")
