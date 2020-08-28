from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def test_cell():
    start = Start()
    end = End()
    air = Air()
    wall = Wall()
    fire = Fire()
    water = Water()
    port_one = Teleport('1')
    port_two = Teleport('2')
    port_three = Teleport('3')
    port_four = Teleport('4')
    port_five = Teleport('5')
    port_six = Teleport('6')
    port_seven = Teleport('7')
    port_eight = Teleport('8')
    port_nine = Teleport('9')

    try:
        assert start.display == 'X'
        assert end.display == 'Y'
        assert air.display == ' '
        assert wall.display == '*'
        assert fire.display == 'F'
        assert water.display == 'W'
        assert port_one.display == '1'
        assert port_two.display == '2'
        assert port_three.display == '3'
        assert port_four.display == '4'
        assert port_five.display == '5'
        assert port_six.display == '6'
        assert port_seven.display == '7'
        assert port_eight.display == '8'
        assert port_nine.display == '9'
        print("Test 01: Cell Initialization passed!")
    except AssertionError:
        print("Test 01: Cell Initialization failed!")


def run_tests():
    test_cell()
