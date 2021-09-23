"""
This will be my code for lab 3, Drawing with Functions.
Everything will need to go into a function.
Three functions minimum are needed. (18 total points, 6 per function).
Function needs to be defined and called correctly.
The drawing functions need to be complex and consist of multiple lines of code.
Pass the x and y parameters, need to be positioned correctly.
Make sure image is centered around the x and y, not offset.
Call one of the functions more than once, and in a different location.
"""

# Brings in the library of code
import arcade

# Sets the parameters for the size of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def draw_small_fish(x, y):
    # This will draw a small fish
    arcade.draw_arc_filled(center_x=x,
                           center_y=y,
                           width=50,
                           height=50,
                           color=arcade.csscolor.DARK_RED,
                           start_angle=270,
                           end_angle=450)
    arcade.draw_ellipse_filled(x + 50, y, 75, 50, arcade.csscolor.FIREBRICK)
    arcade.draw_circle_filled(x + 65, y + 10, 7, arcade.csscolor.BLACK, num_segments=32)


def draw_medium_fish(x, y):
    # This is for a medium sized fish
    arcade.draw_arc_filled(x + 125, y, 75, 75, arcade.csscolor.GOLD, 90, 270)
    arcade.draw_ellipse_filled(x, y, 225, 75, arcade.csscolor.GOLDENROD)
    arcade.draw_arc_filled(x, y, 50, 25, arcade.csscolor.GOLD, 270, 450)
    arcade.draw_circle_filled(x - 50, y + 10, 7, arcade.csscolor.BLACK, num_segments=32)


def draw_sun_fish(x, y):
    # This is my third function for my sun fish (Not the most detailed, but I was a bit time pressed on this one.)
    arcade.draw_triangle_filled(x - 20, y + 50, x + 40, y + 50, x - 40, y + 150, arcade.csscolor.DARK_MAGENTA)
    arcade.draw_triangle_filled(x - 20, y - 50, x + 40, y - 50, x - 40, y - 140, arcade.csscolor.DARK_MAGENTA)
    arcade.draw_ellipse_filled(x, y, 125, 150, arcade.csscolor.DARK_ORCHID)
    arcade.draw_circle_filled(x + 30, y + 15, 7, arcade.csscolor.BLACK, num_segments=32)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab Three picture")
    arcade.set_background_color(arcade.csscolor.ROYAL_BLUE)
    arcade.start_render()

    # Defined functions will go here
    draw_small_fish(200, 500)
    draw_small_fish(150, 600)
    draw_small_fish(90, 540)
    draw_small_fish(600, 400)
    draw_small_fish(525, 475)
    draw_small_fish(350, 100)
    draw_small_fish(150, 200)
    draw_small_fish(75, 125)

    draw_medium_fish(250, 300)
    draw_medium_fish(550, 650)

    draw_sun_fish(550, 200)

    # Ends the drawing and runs it
    arcade.finish_render()
    arcade.run()


# Begins the program by calling main
main()
