from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


def read_lines(filename):
    """Read in a file and process them using parse()

    Arguments:
        filename -- the file name that will be read

    list: list of list of cells

    """
    # read file
    f = open(filename)
    text = f.read()

    lines = []
    line = ''
    index = 0

    # split string to list of strings
    while index < len(text):
        line += text[index]
        if text[index] == '\n':
            lines.append(line)
            line = ''
        index += 1

    # append the last line
    lines.append(line)
    return parse(lines)


def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list: contains list of lists of Cells
    """
    grid = []
    x_count = 0
    y_count = 0
    ports = {}

    for line in lines:
        buf = []  # list of Cells in one line

        # convert string to list of cells
        for ch in line:
            if ch == 'X':
                buf.append(Start().display)
                x_count += 1
            elif ch == 'Y':
                buf.append(End().display)
                y_count += 1
            elif ch == ' ':
                buf.append(Air().display)
            elif ch == '*':
                buf.append(Wall().display)
            elif ch == 'F':
                buf.append(Fire().display)
            elif ch == 'W':
                buf.append(Water().display)
            elif ch in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                buf.append(str(Teleport(int(ch)).display))
                if ch in ports.keys():
                    ports[ch].append(ch)
                else:
                    ports[ch] = [ch]
            elif ch == '\n':
                pass
            else:
                # find unknown letter
                raise ValueError("Bad letter in configuration file: " + ch)
        grid.append(buf)

    if x_count != 1:
        raise ValueError("Expected 1 starting position, got " + str(x_count) + ".")
    if y_count != 1:
        raise ValueError("Expected 1 ending position, got " + str(y_count) + ".")
    for port in ports.keys():

        # find teleport pad that does not come in pairs
        if len(ports[port]) != 2:
            raise ValueError("Teleport pad " + port + " does not have an exclusively matching pad.")
    return grid
