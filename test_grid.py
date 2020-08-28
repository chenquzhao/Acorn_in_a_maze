from grid import grid_to_string
from game_parser import read_lines
from player import Player


def test_grid():
    grid = read_lines("board_simple.txt")
    player = Player([0, 0])

    string_result_one = "A*X**\n*   *\n**Y**\n\nYou have 0 water buckets.\n"

    try:
        assert grid_to_string(grid, player) == string_result_one
        print("Test 08: Grid To String passed!")
    except AssertionError:
        print("Test 08: Grid To String failed!")


def run_tests():
    test_grid()
