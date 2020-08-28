def grid_to_string(grid, player):
    """Turns a grid and player into a string.

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    # display player
    grid[player.row][player.col] = player.display

    # represent grid
    grid_str = ''
    for line in grid:
        grid_str += ''.join(line) + '\n'

    grid_str += '\n' + 'You have '

    # remove (bucket)'s' for '1'
    if player.num_water_buckets == 1:
        grid_str += '1 water bucket.\n'
    elif player.num_water_buckets == -1:
        grid_str += '0 water buckets.\n'
    else:
        grid_str += str(player.num_water_buckets) + ' water buckets.\n'
    return grid_str
