""" Lab 8 for Sprites """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_GEM = 0.35
SPRITE_SCALING_BOMB = 0.5
GEM_COUNT = 50
BOMB_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Gem(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_y -= self.change_y
        self.center_x -= self.change_x

        if self.right >= SCREEN_WIDTH:
            self.change_x *= -1
        if self.left <= 0:
            self.change_x *= -1
        if self.bottom <= 0:
            self.change_y *= -1
        if self.top >= SCREEN_HEIGHT:
            self.change_y *= -1


class Bomb(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):
        super().__init__(filename, sprite_scaling)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.gem_list = None
        self.bomb_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.LIGHT_CORAL)

        self.gem_sound = arcade.load_sound("arcade_resources_sounds_coin4.wav")
        self.hit_sound = arcade.load_sound("arcade_resources_sounds_hit1.wav")

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.bomb_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("maleAdventurer_idle.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        for i in range(GEM_COUNT):
            gem = Gem("gemGreen.png", SPRITE_SCALING_GEM)
            gem.center_x = random.randrange(10, SCREEN_WIDTH - 10)
            gem.center_y = random.randrange(10, SCREEN_HEIGHT - 10)
            gem.change_x = random.randrange(-5, 6)
            gem.change_y = random.randrange(-5, 6)
            self.gem_list.append(gem)

        for i in range(BOMB_COUNT):
            bomb = Bomb("bomb.png", SPRITE_SCALING_BOMB)
            bomb.center_x = random.randrange(SCREEN_WIDTH)
            bomb.center_y = random.randrange(SCREEN_HEIGHT)
            self.bomb_list.append(bomb)

    def on_draw(self):
        arcade.start_render()
        self.gem_list.draw()
        self.player_list.draw()
        self.bomb_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 15, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        if self.score >= 45 and len(self.gem_list) == 0:
            # Figure out what goes here
        else:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        if self.score >= 45 and len(self.gem_list) == 0:
            # Figure out what goes here too, along with bomb update
        self.gem_list.update()

        gem_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)
        bomb_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bomb_list)

        for gem in gem_hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

        for bomb in bomb_hit_list:
            bomb.remove_from_sprite_lists()
            self.score -= 1
            arcade.play_sound(self.hit_sound)


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
