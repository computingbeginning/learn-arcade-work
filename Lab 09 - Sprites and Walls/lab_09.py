"""
Lab 9 for Sprites and Walls

Sprites were retrieved from the Python Arcade Library
"""

import random
import arcade

SPRITE_SCALING = 0.5
COIN_SPRITE_SCALING = 0.4

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

COIN_COUNT = 15

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 100

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.25

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None
        self.score = 0

        self.physics_engine = None

        # Used in scrolling
        self.view_bottom = 0
        self.view_left = 0

        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        # Set up the player
        self.player_sprite = arcade.Sprite("zombie_idle.png",
                                           scale=0.5)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        for x in range(0, 800, 64):
            wall = arcade.Sprite("block_square.png")
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)

        for x in range(0, 800, 64):
            wall = arcade.Sprite("block_square.png")
            wall.center_x = x
            wall.center_y = 832
            self.wall_list.append(wall)

        for y in range(0, 800, 64):
            wall = arcade.Sprite("block_square.png")
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(0, 864, 64):
            wall = arcade.Sprite("block_square.png")
            wall.center_x = 832
            wall.center_y = y
            self.wall_list.append(wall)

        for x in range(576, 768, 64):
            wall = arcade.Sprite("snowCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = x
            wall.center_y = 128
            self.wall_list.append(wall)

        # Multiples of 64: 64, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704, 768

        coordinate_list = [[64, 192],
                           [128, 192],
                           [192, 192],
                           [192, 128],
                           [256, 128],
                           [384, 128],
                           [448, 128],
                           [448, 192],
                           [192, 320],
                           [256, 384],
                           [384, 384],
                           [448, 320]]

        for coordinate in coordinate_list:
            wall = arcade.Sprite("snowCenter_rounded.png", SPRITE_SCALING)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Manual placements were used for the slime blocks
        wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
        wall.center_x = 320
        wall.center_y = 256
        self.wall_list.append(wall)

        wall = arcade.Sprite("slimeBlock.png", SPRITE_SCALING)
        wall.center_x = 576
        wall.center_y = 70
        self.wall_list.append(wall)

        for i in range(COIN_COUNT):
            coin = arcade.Sprite("coinBronze.png", COIN_SPRITE_SCALING)

            coin_placed_successfully = False

            while not coin_placed_successfully:
                coin.center_x = random.randrange(64, 800)
                coin.center_y = random.randrange(64, 800)

                wall_hit_list = arcade.check_for_collision_with_list(coin, self.wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    coin_placed_successfully = True

            self.coin_list.append(coin)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.PURPLE_NAVY)

        # Set the viewport boundaries
        # These numbers set where we have 'scrolled' to.
        self.view_left = 0
        self.view_bottom = 0

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.coin_list.draw()
        self.player_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 40, arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, {self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

        # Draw the box that we work to make sure the user stays inside of.
        # This is just for illustration purposes. You'd want to remove this
        # in your game.
        left_boundary = VIEWPORT_MARGIN
        right_boundary = self.width - VIEWPORT_MARGIN
        top_boundary = self.height - VIEWPORT_MARGIN
        bottom_boundary = VIEWPORT_MARGIN
        arcade.draw_lrtb_rectangle_outline(left_boundary, right_boundary, top_boundary, bottom_boundary,
                                           arcade.color.RED, 2)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.
        This method will attempt to keep the player at least VIEWPORT_MARGIN
        pixels away from the edge.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        # --- Manage Scrolling ---

        # Scroll left
        left_boundary = self.view_left + VIEWPORT_MARGIN
        if self.player_sprite.left < left_boundary:
            self.view_left -= left_boundary - self.player_sprite.left

        # Scroll right
        right_boundary = self.view_left + self.width - VIEWPORT_MARGIN
        if self.player_sprite.right > right_boundary:
            self.view_left += self.player_sprite.right - right_boundary

        # Scroll up
        top_boundary = self.view_bottom + self.height - VIEWPORT_MARGIN
        if self.player_sprite.top > top_boundary:
            self.view_bottom += self.player_sprite.top - top_boundary

        # Scroll down
        bottom_boundary = self.view_bottom + VIEWPORT_MARGIN
        if self.player_sprite.bottom < bottom_boundary:
            self.view_bottom -= bottom_boundary - self.player_sprite.bottom

        if self.view_left < -32:
            self.view_left = -32

        if self.view_left > 64:
            self.view_left = 64

        if self.view_bottom > 264:
            self.view_bottom = 264

        # Viewpoint restrictions could be added here, but a different method needs to be used
        # There is no view right or view top to use

        # Scroll to the proper location
        position = self.view_left, self.view_bottom
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
