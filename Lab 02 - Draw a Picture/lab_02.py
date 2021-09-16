"""
This will be my code for making a picture for lab two
I need to remember that there are multiple things I need for the best grade:
Multiple colors, multiple graph functions including circles, lines, and rectangles
Also requires spaces between code lines, use of comments, spaces after commas, and no warnings.
"""

# Bring in the arcade library
import arcade

# Open a window to make a drawing in
arcade.open_window(800, 800, "Lab 2 Picture")

# Background color will go here
arcade.set_background_color(arcade.csscolor.DEEP_SKY_BLUE)

# Starts the drawing
arcade.start_render()

"""
This code consists of a blue background and a brown tree branch.
The body of the bird is made up of an arc on bottom, a rectangle for the main part, and
triangles for feathers on it's head.
It has two rectangles for legs, two black circles for eyes, and two polygons for it's wings.
Finally, it has a large rounded nose (because I thought it was funny) made from an eclipse.
"""

# This makes a tree branch for the bird
arcade.draw_lrtb_rectangle_filled(0, 800, 100, 0, arcade.csscolor.CHOCOLATE)

# First leg
arcade.draw_rectangle_filled(300, 150, 50, 200, arcade.csscolor.GOLD)

# Second leg
arcade.draw_rectangle_filled(500, 150, 50, 200, arcade.csscolor.GOLD)

# The main body will be made of an arc at the bottom and a square for the middle.

# Lower body
arcade.draw_arc_filled(400, 250, 500, 200, arcade.csscolor.GREEN, 180, 360)

# Upper body
arcade.draw_lrtb_rectangle_filled(150, 650, 550, 250, arcade.csscolor.GREEN)

# Triangles on the head for feathers
arcade.draw_triangle_filled(x1=150,
                            y1=550,
                            x2=150,
                            y2=700,
                            x3=275,
                            y3=550,
                            color=arcade.csscolor.GREEN)

arcade.draw_triangle_filled(x1=275,
                            y1=550,
                            x2=325,
                            y2=700,
                            x3=400,
                            y3=550,
                            color=arcade.csscolor.GREEN)

arcade.draw_triangle_filled(x1=400,
                            y1=550,
                            x2=450,
                            y2=700,
                            x3=525,
                            y3=550,
                            color=arcade.csscolor.GREEN)

arcade.draw_triangle_filled(x1=525,
                            y1=550,
                            x2=650,
                            y2=700,
                            x3=650,
                            y3=550,
                            color=arcade.csscolor.GREEN)

"""
This code was originally for a beak
However, I changed the nose of the bird to a rounded shape
Because of this, I decided to comment the code for the beak out
It is still here for reference though, just in case
"""
# arcade.draw_triangle_filled(400, 450, 400, 400, 475, 425, arcade.csscolor.YELLOW)

# Circles for eyes
arcade.draw_circle_filled(300, 500, 25, arcade.csscolor.BLACK)

arcade.draw_circle_filled(500, 500, 25, arcade.csscolor.BLACK)

# Polygon for wing
arcade.draw_polygon_filled(((175, 340),
                            (200, 260),
                            (225, 230),
                            (250, 260),
                            (275, 340)
                            ),
                           arcade.csscolor.GREENYELLOW)

# Polygon for wing 2
arcade.draw_polygon_filled(((525, 340),
                            (550, 260),
                            (575, 230),
                            (600, 260),
                            (625, 340)
                            ),
                           arcade.csscolor.GREENYELLOW)

# Lighter colored nose with ellipse
arcade.draw_ellipse_filled(400, 400, 200, 150, arcade.csscolor.GREENYELLOW)

# Finishes the drawing
arcade.finish_render()

# Keeps the window open until manually closed
arcade.run()
