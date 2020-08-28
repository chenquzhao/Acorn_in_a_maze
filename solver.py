import sys
from game import Game
from game_parser import read_lines
from run import search_coords


def left(cell):
    """Apply a left move to target cell

    Arguments:
        cell -- target cell

    Returns:
        [int, int]: new coordinates after a left move

    """
    return [cell[0], cell[1] - 1]


def down(cell):
    """Apply a down move to target cell

    Arguments:
        cell -- target cell

    Returns:
        [int, int]: new coordinates after a down move

    """
    return [cell[0] + 1, cell[1]]


def right(cell):
    """Apply a right move to target cell

    Arguments:
        cell -- target cell

    Returns:
        [int, int]: new coordinates after a right move

    """
    return [cell[0], cell[1] + 1]


def up(cell):
    """Apply an up move to target cell

    Arguments:
        cell -- target cell

    Returns:
        [int, int]: new coordinates after an up move

    """
    return [cell[0] - 1, cell[1]]


def coords_sub(cell_one, cell_two):
    """Subtract the second cell from the first cell by row and column

    Args:
        cell_one -- the first coordinates
        cell_two -- the second coordinates

    Returns:
        int: row difference
        int: column difference

    """
    row_diff = cell_one[0] - cell_two[0]
    col_diff = cell_one[1] - cell_two[1]
    return row_diff, col_diff


def teleport_pair(cell, game_coords):
    """Search cell in all teleport pad coordinates, figure its partner pad coordinates if exists

    Arguments:
        cell -- coordinates of the cell to be searched for
        game_coords -- coordinates distribution of all Cells

    Returns:
        [int, int] or -1: [int, int] -> partner pad coordinates
                                  -1 -> not exist

    """
    # get cell display
    item = search_coords(game_coords, cell)

    if item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        for coords in game_coords[item]:
            # partner pad found
            if coords != cell:
                return coords

    # not a teleport pad
    return -1


def dfs(game, game_coords):
    """Apply depth first search algorithm to generate an optimal path

    Arguments:
        game -- the game object
        game_coords -- coordinates distribution of all Cells

    Returns:
        int: game result, 0 -> loss, 1 -> Win
        int: total steps count
        str: path details

    """
    # *** the main stack to record steps ***
    stack_moves = [[game.player.row, game.player.col]]

    # record path and illegal moves
    route = []
    declined_moves = []

    # met fire and no water on hand
    met_fire = False

    # keep looping until reaching end point
    while stack_moves[-1] != game_coords['Y'][0]:
        # main stack popped in last turn
        go_back = False

        # struggled more than three turns
        if len(route) > 3 and route[-1] == 3 and route[-2] == 3 and route[-3] == 3:
            return 0, 0, 0

        player_coords = [game.player.row, game.player.col]

        # try the first possible move: left, down, right, up, teleport, go back(pop)
        if left(player_coords) not in stack_moves and left(player_coords) not in declined_moves:
            will_move = left(player_coords)
            action = 1

        elif down(player_coords) not in stack_moves and down(player_coords) not in declined_moves:
            will_move = down(player_coords)
            action = 2

        elif right(player_coords) not in stack_moves and right(player_coords) not in declined_moves:
            will_move = right(player_coords)
            action = -1

        elif up(player_coords) not in stack_moves and up(player_coords) not in declined_moves:
            will_move = up(player_coords)
            action = -2

        elif search_coords(game_coords, stack_moves[-1]) in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # teleport from current location
            action = 3
            will_move = stack_moves[-1]

        else:
            # pop the last element in main stack
            declined_moves.append(stack_moves.pop())

            # back upon start point, loss!
            if not stack_moves:
                return 0, 0, 0

            # go back
            will_move = stack_moves[-1]
            action = -route[-1]
            go_back = True

        # check if move is legal
        item = search_coords(game_coords, will_move)

        if item == '*' or item == -1:
            declined_moves.append(will_move)
            continue
        elif item == 'W':
            game.player.num_water_buckets += 1
            if met_fire:
                # can put out fire now, therefore, seeking path using a fresh mind :)
                stack_moves = []
                declined_moves = []
                met_fire = False

            for i in range(len(game_coords['W'])):
                # water picked up, set current display from 'W' to ' ' in game_coords
                if game_coords['W'][i] == will_move:
                    game_coords['W'].pop(i)
                    game_coords[' '].append(will_move)
                    break
        elif item == 'F':
            if game.player.num_water_buckets < 1:
                # cannot put out fire, refuse this move :(
                declined_moves.append(will_move)
                met_fire = True
                continue
            game.player.num_water_buckets -= 1
        elif item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            for coords in game_coords[item]:
                if coords != will_move:
                    will_move = coords
                    break

        # *** append to main stack ***
        if not go_back:
            stack_moves.append(will_move)

        # *** move the player ***
        game.player.row = will_move[0]
        game.player.col = will_move[1]

        route.append(action)

    action_map = {1: 'a', 2: 's', -1: 'd', -2: 'w', 3: 'e'}

    # translate action to string of cmd
    trace = ''
    for action in route:
        trace += action_map[action] + ', '

    return 1, len(route), trace


def bfs(game, game_coords):
    """Apply breadth first search algorithm to generate an optimal path

    Arguments:
        game -- the game object
        game_coords -- coordinates distribution of all Cells

    Returns:
        int: game result, 0 -> loss, 1 -> Win
        int: total steps count
        str: path details

    """
    # *** main queue to record steps and corresponding costs ***
    queue_moves = [[game.player.row, game.player.col]]
    cost_moves = [0]

    # record cost and illegal moves
    cost = 1
    declined_moves = []

    # record the moves in the previous turn(iteration)
    last_steps = [[game.player.row, game.player.col]]

    # ***** Step 1: Marking game board using cost *****
    while True:

        # struggled in a location, loss
        if not last_steps:
            return 0, 0, 0

        # collect all potential moves: left, down, right, up, teleport(if possible)
        potential_steps = []
        for step in last_steps:
            potential_steps.append(left(step))
            potential_steps.append(down(step))
            potential_steps.append(right(step))
            potential_steps.append(up(step))

            if search_coords(game_coords, step) in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                potential_steps.append(step)

        current_steps = []
        for step in potential_steps:
            if step in declined_moves:
                continue
            elif step in queue_moves:
                # the step existed in main queue, replace it if cost is lower, otherwise skip
                if cost >= cost_moves[queue_moves.index(step)]:
                    if step != queue_moves[-1]:
                        continue

            # check if move is legal
            will_move = step
            item = search_coords(game_coords, will_move)

            if item == '*' or item == -1:
                declined_moves.append(will_move)
                continue

            elif item == 'W':
                game.player.num_water_buckets += 1

                for i in range(len(game_coords['W'])):
                    # water picked up, set current display from 'W' to ' ' in game_coords
                    if game_coords['W'][i] == will_move:
                        game_coords['W'].pop(i)
                        game_coords[' '].append(will_move)
                        break

            elif item == 'F':
                if game.player.num_water_buckets < 1:
                    # cannot put out fire, refuse this move :(
                    declined_moves.append(will_move)
                    continue

                game.player.num_water_buckets -= 1
            elif item in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                for coords in game_coords[item]:
                    if coords != will_move:
                        will_move = coords
                        break

            current_steps.append(will_move)

            # append to main queue
            queue_moves.append(will_move)
            cost_moves.append(cost)

        cost += 1

        # reach end point
        if game_coords['Y'][0] in current_steps:
            break

        # last_steps <- current_steps
        last_steps = []
        last_steps.extend(current_steps)

    cost -= 1

    # ***** Step 2: recall through main queue to generate a path *****
    # *** Queue: last in first out ***
    recall_moves = queue_moves[::-1]
    recall_cost = cost_moves[::-1]
    cursor = recall_moves[0]

    # generated path
    route = []

    # 'action to cmd' translator
    action_map = {(1, 0): 'w', (-1, 0): 's', (0, 1): 'a', (0, -1): 'd'}

    for i in range(len(recall_moves)):
        if recall_cost[i] == cost - 1:
            x, y = coords_sub(recall_moves[i], cursor)

            # simple move: left, down, right, up
            if abs(x) + abs(y) == 1:
                cursor = recall_moves[i]
                cost -= 1
                route.insert(0, action_map[(x, y)])

            # teleport move
            elif teleport_pair(cursor, game_coords) != -1:
                pair = teleport_pair(cursor, game_coords)
                x, y = coords_sub(recall_moves[i], pair)

                # teleport after simple move
                if abs(x) + abs(y) == 1:
                    cursor = recall_moves[i]
                    cost -= 1
                    route.insert(0, action_map[(x, y)])

                # teleport after no move ('e')
                elif abs(x) + abs(y) == 0:
                    cursor = recall_moves[i]
                    cost -= 1
                    route.insert(0, 'e')

    # convert list of paths to string
    trace = ''
    for action in route:
        trace += action + ', '

    return 1, cost_moves[-1], trace


def main():

    if len(sys.argv) < 3:
        print("Usage: python3 solver.py <filename> <mode>")
        sys.exit(0)

    file = sys.argv[1]
    game = Game(file)

    # *** get grid ***
    grid = read_lines(file)

    # *** get coords ***
    game_coords = game.collect_coords(grid)

    # set player to start point
    game.player.row = game_coords['X'][0][0]
    game.player.col = game_coords['X'][0][1]

    if sys.argv[2] == "DFS":
        result, count, trace = dfs(game, game_coords)
    elif sys.argv[2] == "BFS":
        result, count, trace = bfs(game, game_coords)

    return result, count, trace


if __name__ == "__main__":
    solution_found = False
    result, count, trace = main()

    if result == 1:
        solution_found = True

    if solution_found:
        print("Path has " + str(count) + " moves.")
        print("Path: " + trace[:-2])
    else:
        print("There is no possible path.")