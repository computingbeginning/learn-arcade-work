"""
Lab 4 will be focused on creating the camel game.
The code runs instructions for the player to follow.
They must progress forward a certain amount while being chased.
If they reach a certain marker, they win.
Code must match the steps provided, though things can be changed or added.
(Perhaps if i have time, I can make this Mario Party themed?
Bowser could be chasing us along the board.)
"""

import random


def main():
    # This will start the main program, showing the directions for the player
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and outrun the natives.")

    done = False

    # These set an initial value for the variables we use in the code
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance_traveled = -25
    canteen_drinks_remaining = 3

    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")
        print(" ")

        user_choice = input("What is your choice? ")

        # This runs the code of whether or not the player chooses to quit
        if user_choice.upper() == "Q":
            done = True

        # This runs the code for the status check, showing how far they traveled, how many drinks they have left
        # and how far the natives have traveled.
        elif user_choice.upper() == "E":
            print("Miles traveled " + str(miles_traveled))
            print("Drinks in canteen: " + str(canteen_drinks_remaining))
            print("The natives are " + str(miles_traveled - natives_distance_traveled) + " miles behind you.")
            print(" ")

        # This is the code for when the player stops for the night
        # This resets their camel tiredness, but the natives get a bit closer.
        elif user_choice.upper() == "D":
            print("You have stopped for the night.")
            camel_tiredness = 0
            print("The camel is feeling happy now!")
            new_distance = random.randrange(5, 16)
            natives_distance_traveled = (natives_distance_traveled + new_distance)

        # This is the code for when the user charges forward at full speed.
        # This lets them go farther, but their camel gets tired more quickly this way.
        elif user_choice.upper() == "C":
            print("You charge ahead at full speed.")
            new_distance = random.randrange(10, 21)
            miles_traveled = (miles_traveled + new_distance)
            print("You have traveled " + str(miles_traveled) + " miles")
            thirst += 1
            camel_tiredness += random.randrange(1, 4)
            new_distance = random.randrange(5, 16)
            natives_distance_traveled = (natives_distance_traveled + new_distance)

            # This is the code for finding an oasis.
            if not done and random.randrange(20) == 0:
                print("You have found an oasis!")
                print("Your canteen is filled, your thirst is gone, and your camel is rested!")
                canteen_drinks_remaining = 3
                thirst = 0
                camel_tiredness = 0

        # This is the code for moving at a moderate speed.
        # Your camel will not tire out as fast, but you run the risk of not outrunning the natives.
        elif user_choice.upper() == "B":
            print("You travel at a moderate speed.")
            new_distance = random.randrange(6, 13)
            miles_traveled = (miles_traveled + new_distance)
            print("You have traveled " + str(miles_traveled) + " miles.")
            thirst += 1
            camel_tiredness += 1
            new_distance = random.randrange(5, 16)
            natives_distance_traveled = (natives_distance_traveled + new_distance)

            # This is the code for finding an oasis.
            if not done and random.randrange(20) == 0:
                print("You have found an oasis!")
                print("Your canteen is filled, your thirst is gone, and your camel is rested!")
                canteen_drinks_remaining = 3
                thirst = 0
                camel_tiredness = 0

        elif user_choice.upper() == "A":
            if canteen_drinks_remaining > 0:
                if thirst > 0:
                    print("You take a drink from the canteen.")
                    canteen_drinks_remaining -= 1
                    thirst = 0
                elif thirst == 0:
                    print("You are not thirsty.")
            else:
                print("There are no drinks left in your canteen!")

        if not done and 4 < thirst <= 6:
            print("You are thirsty.")

        if not done and thirst > 6:
            print("You died of thirst!")
            done = True

        if not done and 5 < camel_tiredness <= 8:
            print("Your camel is tired.")

        if not done and camel_tiredness > 8:
            print("Your camel has died.")
            done = True

        if not done and natives_distance_traveled >= miles_traveled:
            print("The natives have caught up to you!")
            done = True
        elif not done and natives_distance_traveled >= (miles_traveled - 15):
            print("The natives are getting close!")

        if not done and miles_traveled >= 200:
            print("You have made it across the desert. You have finally escaped!")
            done = True


main()
print("Thank you for playing!")
