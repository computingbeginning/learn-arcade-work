"""
Need two for loops for this.
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
        if row < ROW_COUNT and column < COLUMN_COUNT:
            if self.grid[row][column] == 1:
                self.grid[row][column] = 0
            elif self.grid[row][column] == 0:
                self.grid[row][column] = 1

        # This is for total cells
        total_cells = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    total_cells += 1
        print("Total of", total_cells, "cells are selected.")

        # This is for the cells in a row
        for row in range(ROW_COUNT):
            total_rows = 0
            continuous_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    total_rows += 1
                    continuous_count += 1
                else:
                    if continuous_count > 2:
                        print("There are", continuous_count, "continuous blocks selected on row", row)
                    continuous_count = 0
            if continuous_count > 2:
                print("There are", continuous_count, "continuous blocks selected on row", row)

            print("Row", row, "has", total_rows, "cells selected.")

        # This is for the cells in a column
        for column in range(COLUMN_COUNT):
            total_columns = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    total_columns += 1
            print("Column", column, "has", total_columns, "cells selected.")


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
