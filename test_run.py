from run import search_coords
from game import Game
from game_parser import read_lines


def test_run():
    game = Game("board_simple.txt")
    grid = read_lines("board_simple.txt")

    game_coords = game.collect_coords(grid)

    try:
        assert search_coords(game_coords, [1, 2]) == ' '
        assert search_coords(game_coords, [2, 2]) == 'Y'
        print("Test 10: Coordinates Search passed!\n")
    except AssertionError:
        print("Test 10: Coordinates Search failed!\n")


def run_tests():
    test_run()