class Player:
    def __init__(self, position, num_water_buckets=0):
        self.display = 'A'
        self.num_water_buckets = num_water_buckets
        self.row = position[0]
        self.col = position[1]

    def move(self, move):
        """Apply a coordinates change to player.

        Arguments:
            move -- coordinates change of player

        Returns:
            [int, int]: new coordinates of player

        """
        # [row, column]
        return [self.row + move[0], self.col + move[1]]
