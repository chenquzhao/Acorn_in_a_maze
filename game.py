from grid import grid_to_string
from player import Player


class Game:
    def __init__(self, filename):
        self.filename = filename
        self.player = Player([0, 0])

    def game_move(self, move):
        """Apply a coordinates change to player, invoking move() from Player.

        Arguments:
            move -- coordinates change of player

        Returns:
            [int, int]: new coordinates of player

        """
        return self.player.move(move)

    def read_cells(self, grid):
        """Turns a grid and the default player into a string, invoking grid_to_string() from grid.py

        Arguments:
            grid -- list of list of Cells

        Returns:
            str: a string representation of the grid and default player

        """
        return grid_to_string(grid, self.player)

    def collect_coords(self, grid):
        """Turns a grid into a dictionary, using Cell display as keys.

        Arguments:
            grid -- list of list of Cells

        Returns:
            dict: coordinates distribution of Cells

        """
        coords = {'X': [], ' ': [], 'Y': [], '*': [], 'W': [], 'F': [], '1': [], '2': [],
                  '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], 'A': []}

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                cell = grid[i][j]

                # only one player may exist
                if cell == 'A':
                    coords['A'] = [[i, j]]
                else:
                    coords[cell].append([i, j])
        return coords
