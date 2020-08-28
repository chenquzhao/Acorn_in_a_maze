from game_parser import read_lines

def test_parse():

    try:
        grid_bad_letter = read_lines("board_bad_letter.txt")
        assert False
    except ValueError:
        print("Test 04: Bad Letter Check passed!")
    except AssertionError:
        print("Test 04: Bad Letter Check failed! (did not throw an exception)")

    try:
        grid_no_starting = read_lines("board_no_starting.txt")
        assert False
    except ValueError:
        print("Test 05: Starting Point Check passed!")
    except AssertionError:
        print("Test 05: Starting Point Check failed! (did not throw an exception)")

    try:
        grid_no_ending = read_lines("board_no_ending.txt")
        assert False
    except ValueError:
        print("Test 06: Ending Point Check passed!")
    except AssertionError:
        print("Test 06: Ending Point Check failed! (did not throw an exception)")

    try:
        grid_mismatch_port = read_lines("board_mismatch_port.txt")
        assert False
    except ValueError:
        print("Test 07: Port Pad Match Check passed!")
    except AssertionError:
        print("Test 07: Port Pad Match Check failed! (did not throw an exception)")

def run_tests():
    test_parse()
