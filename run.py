import sys
from game import Game
from game_parser import read_lines


def search_coords(game_coords, cell):
    """Search Cell in all Cell coordinates, figure its display if legal

    Arguments:
        game_coords -- coordinates distribution of all Cells
        cell -- coordinates of the cell to be searched for

    Returns:
        char or -1: char -> corresponding display
                      -1 -> illegal move

    """
    for key in game_coords.keys():
        if cell in game_coords[key]:
            return key
    return -1


def main():

    if len(sys.argv) < 2:
        print("Usage: python3 run.py <filename> [play]")
        sys.exit(0)

    file = sys.argv[1]
    game = Game(file)

    # *** get grid ***
    try:
        grid = read_lines(game.filename)
    except FileNotFoundError:
        print(file + " does not exist!")
        sys.exit(0)

    # *** get coords ***
    game_coords = game.collect_coords(grid)

    # set player to start point
    game.player.row = game_coords['X'][0][0]
    game.player.col = game_coords['X'][0][1]

    # display initial game board
    game_view = game.read_cells(grid)
    print(game_view)

    # *** initialize important parameters ***
    total_moves = 0
    move_record = ''
    result = 1  # 0 -> loss, 1 -> win
    port_no = -1

    while [game.player.row, game.player.col] != game_coords['Y'][0]:  # break when wins
        cmd = input("Input a move: ").lower()

        # read cmd
        if cmd == 's':
            will_move = game.game_move([1, 0])
        elif cmd == 'w':
            will_move = game.game_move([-1, 0])
        elif cmd == 'a':
            will_move = game.game_move([0, -1])
        elif cmd == 'd':
            will_move = game.game_move([0, 1])
        elif cmd == 'q':
            print("\nBye!")
            sys.exit(0)
        elif cmd == 'e':
            will_move = game.game_move([0, 0])
        else:
            print(game_view)
            print("Please enter a valid move (w, a, s, d, e, q).\n")
            continue

        # check if move is legal
        item = search_coords(game_coords, will_move)

        if item == '*' or item == -1:
            print(game_view)
            print("You walked into a wall. Oof!\n")
            continue

        elif item == 'W':
            game.player.num_water_buckets += 1
        elif item == 'F':
            game.player.num_water_buckets -= 1
        elif item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            for coords in game_coords[item]:
                if coords != will_move:
                    will_move = coords
                    break

        # reset previous location
        if port_no == -1:
            grid[game.player.row][game.player.col] = ' '
        else:
            # port should be restored
            grid[game.player.row][game.player.col] = str(port_no)
            port_no = -1

        # display start point
        if game_coords['X']:
            grid[game_coords['X'][0][0]][game_coords['X'][0][1]] = 'X'
        else:
            grid[game.player.row][game.player.col] = 'X'

        # *** move the player ***
        game.player.row = will_move[0]
        game.player.col = will_move[1]

        # update coords and view
        game_coords = game.collect_coords(grid)
        game_view = game.read_cells(grid)

        print(game_view)

        # record move numbers and details
        total_moves += 1
        move_record += cmd + ', '

        # additional displayed message
        if item == 'W':
            print("Thank the Honourable Furious Forest, you've found a bucket of water!\n")
        elif item == 'F':
            if game.player.num_water_buckets < 0:
                print("\nYou step into the fires and watch your dreams disappear :(.\n")
                result = 0
                break
            print("With your strong acorn arms, you throw a water bucket at the fire. "
                  + "You acorn roll your way through the extinguished flames!\n")
        elif item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Whoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.\n")
            port_no = int(item)

    if result == 1:
        # Victory Hint
        print("\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest "
              + "Throne,"
              + " restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n")
    else:
        # Defeat Hint
        print("The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash "
              + "and is scattered to the winds by the next storm... You have been roasted.\n")

    if total_moves == 1:
        print("You made 1 move.")
        print("Your move: " + move_record[:-2] + "\n")
    else:
        print("You made " + str(total_moves) + " moves.")
        print("Your moves: " + move_record[:-2] + "\n")

    if result == 1:
        # Victory Hint
        print("=====================\n"
              "====== YOU WIN! =====\n"
              "=====================")
    else:
        #  Defeat Hint
        print("=====================\n"
              "===== GAME OVER =====\n"
              "=====================")


if __name__ == '__main__':
    main()
