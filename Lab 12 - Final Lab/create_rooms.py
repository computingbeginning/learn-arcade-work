from room import Room


def create_rooms():
    room_list = []

    # room0 is the foyer of the mansion, the starting point.
    room0 = Room("The Foyer of the mansion is grand, decorated with paintings and candelabras on the wall.\n"
                 "There are two doors present, one in the north face of the room, and one in the south face.",
                 4,
                 None,
                 1,
                 None,
                 None,
                 None)
    room_list.append(room0)

    # Room 1 is the courtyard
    room1 = Room("The full moon above illuminates the large courtyard. \n"
                 "The courtyard is filled with wilted flowers and a flowing fountain. \n"
                 "The east side of the courtyard has a tool shed, and the east side has a dog house. \n"
                 "The north shows the entrance to the mansion, and the south shows the locked gate.)",
                 0,
                 2,
                 12,
                 3,
                 None,
                 None)
    room_list.append(room1)

    # Room 2 is the tool shed
    room2 = Room("You walk up to the small wooden tool shed. Perhaps there is something here you could use to help. \n"
                 "All you can do now is go back the way you came.",
                 None,
                 None,
                 None,
                 1,
                 None,
                 None)
    room_list.append(room2)

    # Room 3 is the dog house
    room3 = Room("You stumble upon a small dog house in the corner of the courtyard. \n"
                 "It sounds like something is inside. \n"
                 "All you can do now is go back the way you came.",
                 None,
                 1,
                 None,
                 None,
                 None,
                 None)
    room_list.append(room3)

    # Room 4 is the main hallway
    room4 = Room("What a large hallway!\n"
                 "You are not able to see down to either end from where you are.\n"
                 "You will have to walk to different parts of the hallway to see some things. \n"
                 "From where you are now, you can either walk to the east side of the hallway, or the west side. \n"
                 "There is a tear in the north wall in front of you, and behind you is the door to the foyer",
                 5,
                 6,
                 0,
                 8,
                 None,
                 None)
    room_list.append(room4)

    # Room 5 is a hole in the wall of the hallway
    room5 = Room("You walk up to the hole in the wall, big enough to peak through. \n"
                 "You look inside and see an old dusty room, with paintings and covered furniture. \n"
                 "There is nothing else you can do but return to where you were before.",
                 None,
                 None,
                 4,
                 None,
                 None,
                 None)
    room_list.append(room5)

    # Room 6 is the east side of the hallway
    room6 = Room("You walk east down the hallway, keeping your hand to the wall for safety. \n"
                 "From here, there is a door in the north wall, and the hallway to the west you came from.",
                 7,
                 None,
                 None,
                 4,
                 None,
                 None)
    room_list.append(room6)

    # Room 7 is the master bedroom
    room7 = Room("You enter the master bedroom. \n"
                 "You spot a queen sized bed, a fancy fur rug, and an elegant mirror. \n"
                 "There is a door on the south wall.",
                 None,
                 None,
                 6,
                 None,
                 None,
                 None)
    room_list.append(room7)

    # Room 8 is the west side of the main hallway
    room8 = Room("You stumble down the hallway's western side. \n"
                 "From here, you see two doors, one on the south wall, and one on the north wall. \n"
                 "You can also go back east to return to the middle of the hallway.",
                 10,
                 4,
                 9,
                 None,
                 None,
                 None)
    room_list.append(room8)

    # Room 9 is the kitchen
    room9 = Room("You enter the room and find a large kitchen. \n"
                 "It is surprisingly clean, and the stove seems brand new. \n"
                 "There is a door on the north wall, and a large metal door embedded in the south end of the room.",
                 8,
                 None,
                 13,
                 None,
                 None,
                 None)
    room_list.append(room9)

    # Room 10 is the dining hall
    room10 = Room("You are met with a grand dining hall, fit to serve over a dozen people. \n"
                  "You can see trolleys for transporting the food, and the eastern wall is fitted with "
                  "a large wine cabinet. \n"
                  "As far as you can tell, you may only be able to return through the door on the southern wall.",
                  None,
                  11,
                  8,
                  None,
                  None,
                  None)
    room_list.append(room10)

    # Room 11 is the hidden room behind the wine cabinet
    room11 = Room("You pull on the wine cabinet, and it slides away from the wall, revealing a room hidden from the "
                  "view of the dining hall. \n"
                  "This room is filled with paintings, furniture, and a ring of keys."
                  "The only way out of the room is to return to the dining hall.",
                  None,
                  None,
                  None,
                  10,
                  None,
                  None)
    room_list.append(room11)

    # Room 12 is the metal gate in the courtyard.
    room12 = Room("You walk up to the large metal gates separating you from the outside world."
                  "It is fitted with a metal padlock. If only you had the key.. \n"
                  "For now, all you can do is walk north back to the courtyard.",
                  1,
                  None,
                  None,
                  None,
                  None,
                  None)
    room_list.append(room12)

    room13 = Room("Brr! This room is a freezer! It is filled with frozen meats and deserts.\n"
                  "The only exit is back the way you came.",
                  9,
                  None,
                  None,
                  None,
                  None,
                  None)
    room_list.append(room13)

    return room_list
