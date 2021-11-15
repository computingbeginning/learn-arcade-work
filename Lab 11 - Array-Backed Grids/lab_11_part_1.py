"""
Do not adjust the on draw method. Keep what is here, and alter the on_click method.
Add if statements for if the clicking happens on the top, bottom, left, or right edges.
"""

import arcade

WIDTH = 60
HEIGHT = 60
MARGIN = 5

ROW_COUNT = 10
COLUMN_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * COLUMN_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        self.grid = []

        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)

        self.grid[3][4] = 1

    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()

        color = 0

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = (WIDTH / 2) + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN
                if self.grid[row][column] == 0:
                    color = arcade.color.LIGHT_CYAN
                elif self.grid[row][column] == 1:
                    color = arcade.color.LIGHT_GREEN

                arcade.draw_rectangle_filled(x, y,
                                             WIDTH, HEIGHT,
                                             color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)
        print("click", row, column)
        if self.grid[row][column] == 1:
            self.grid[row][column] = 0
        elif self.grid[row][column] == 0:
            self.grid[row][column] = 1


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
