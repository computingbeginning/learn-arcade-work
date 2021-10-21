""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
MOVEMENT_SPEED = 7


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
    # This will draw a medium sized fish
    arcade.draw_arc_filled(x + 125, y, 75, 75, arcade.csscolor.GOLD, 90, 270)
    arcade.draw_ellipse_filled(x, y, 225, 75, arcade.csscolor.GOLDENROD)
    arcade.draw_arc_filled(x, y, 50, 25, arcade.csscolor.GOLD, 270, 450)
    arcade.draw_circle_filled(x - 50, y + 10, 7, arcade.csscolor.BLACK, num_segments=32)


def draw_sun_fish(x, y):
    # This will draw a sun fish
    arcade.draw_triangle_filled(x - 20, y + 50, x + 40, y + 50, x - 40, y + 150, arcade.csscolor.DARK_MAGENTA)
    arcade.draw_triangle_filled(x - 20, y - 50, x + 40, y - 50, x - 40, y - 140, arcade.csscolor.DARK_MAGENTA)
    arcade.draw_ellipse_filled(x, y, 125, 150, arcade.csscolor.DARK_ORCHID)
    arcade.draw_circle_filled(x + 30, y + 15, 7, arcade.csscolor.BLACK, num_segments=32)


class SmallFish:
    def __init__(self, x, y):
        self.position_x = x
        self.position_y = y

    def draw(self):
        arcade.draw_arc_filled(center_x=self.position_x,
                               center_y=self.position_y,
                               width=50,
                               height=50,
                               color=arcade.csscolor.DARK_RED,
                               start_angle=270,
                               end_angle=450)
        arcade.draw_ellipse_filled(self.position_x + 50, self.position_y, 75, 50, arcade.csscolor.FIREBRICK)
        arcade.draw_circle_filled(self.position_x + 65, self.position_y + 10, 7, arcade.csscolor.BLACK, num_segments=32)


class BigFish:
    def __init__(self, x, y, change_x, change_y):
        self.position_x = x
        self.position_y = y
        self.change_x = change_x
        self.change_y = change_y
        self.wall_bump_sound = arcade.load_sound(":resources:sounds/hurt3.wav")

    def draw(self):
        arcade.draw_arc_filled(self.position_x + 125, self.position_y, 75, 75, arcade.csscolor.GOLD, 90, 270)
        arcade.draw_ellipse_filled(self.position_x, self.position_y, 225, 75, arcade.csscolor.GOLDENROD)
        arcade.draw_arc_filled(self.position_x, self.position_y, 50, 25, arcade.csscolor.GOLD, 270, 450)
        arcade.draw_circle_filled(self.position_x - 50, self.position_y + 10, 7, arcade.csscolor.BLACK, num_segments=32)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        if self.position_x < 112:
            self.position_x = 112
            arcade.play_sound(self.wall_bump_sound)

        if self.position_x > SCREEN_WIDTH - 122:
            self.position_x = SCREEN_WIDTH - 122
            arcade.play_sound(self.wall_bump_sound)

        if self.position_y < 37:
            self.position_y = 37
            arcade.play_sound(self.wall_bump_sound)

        if self.position_y > SCREEN_HEIGHT - 36:
            self.position_y = SCREEN_HEIGHT - 36
            arcade.play_sound(self.wall_bump_sound)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.click_sound = arcade.load_sound(":resources:sounds/coin1.wav")

        self.set_mouse_visible(False)

        self.fish = SmallFish(300, 200)
        self.second_fish = BigFish(200, 700, 0, 0)

    def on_draw(self):
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

        self.fish.draw()
        self.second_fish.draw()

        # Ends the drawing and runs it
        arcade.finish_render()

    def on_mouse_motion(self, x, y, dx, dy):
        self.fish.position_x = x
        self.fish.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT or button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.click_sound)

    def update(self, delta_time):
        self.second_fish.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.second_fish.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.second_fish.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.second_fish.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.second_fish.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.second_fish.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.second_fish.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()
