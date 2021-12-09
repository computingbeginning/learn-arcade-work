from items import Item


# -1 means the item is in your inventory
# -2 means the item can be found, but only through special means.
# -3 means the item has been used and cannot be found or used again.
def create_items():
    item_list = []
    # Appended items

    item0 = Item("You see a large block of ice with something sticking out of the edge. What could it be?",
                 "This is a large block of ice, with a bone poking out of the edge. "
                 "You found it in the freezer. \n"
                 "Perhaps the bone could be useful if you could thaw it out.",
                 "ice",
                 13)
    item_list.append(item0)

    item1 = Item("You spot a key with a diamond handle hanging on the wall.",
                 "A key with a diamond shape built into the end of the handle.\n"
                 "Perhaps this is the key to the courtyard gate?",
                 "key",
                 11)
    item_list.append(item1)

    item2 = Item("There is a flashlight propped on a barrel.",
                 "This is the flashlight you found in the tool shed.",
                 "flashlight",
                 2)
    item_list.append(item2)

    item3 = Item(None,
                 "This is the bone you got from melting the ice. What can it be used for?",
                 "bone",
                 -2)
    item_list.append(item3)

    item4 = Item("Hmm? Is there something in the dog house?",
                 "This is a old picture of the mansion, showing the dining hall filled with people. \nJudging"
                 "by the familiar dog in the picture, it must have been taken before the residents were ghosts.\n"
                 "It seems to have been taken from where you enter the room, and shows trolleys carrying food, along "
                 "with a door at the other end of the room.",
                 "picture",
                 -2)
    item_list.append(item4)

    return item_list
