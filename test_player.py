from player import Player


def test_player():

    player = Player([0, 1], 2)

    try:
        assert player.display == 'A'
        assert player.row == 0
        assert player.col == 1
        assert player.num_water_buckets == 2
        print("Test 02: Player Initialization passed!")
    except AssertionError:
        print("Test 02: Player Initialization failed!")

    try:
        assert player.move([1, 0]) == [1, 1]
        assert player.move([0, 1]) == [0, 2]
        print("Test 03: Player Move passed!")
    except AssertionError:
        print("Test 03: Player Move failed!")


def run_tests():
    test_player()