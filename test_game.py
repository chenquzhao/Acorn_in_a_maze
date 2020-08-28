from game import Game
from game_parser import read_lines


def test_game():
    game = Game("board_simple.txt")
    grid = read_lines(game.filename)

    coords_result = {'X': [[0, 2]], ' ': [[1, 1], [1, 2], [1, 3]], 'Y': [[2, 2]],
                     '*': [[0, 0], [0, 1], [0, 3], [0, 4], [1, 0], [1, 4], [2, 0], [2, 1], [2, 3], [2, 4]],
                     'W': [], 'F': [], '1': [], '2': [], '3': [], '4': [], '5': [], '6': [],
                     '7': [], '8': [], '9': [], 'A': []}

    try:
        assert game.collect_coords(grid) == coords_result
        print("Test 09: Coordinates Collection passed!")
    except AssertionError:
        print("Test 09: Coordinates Collection failed!")


def run_tests():
    test_game()
