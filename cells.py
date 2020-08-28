# define displays of Cells
class Start:
    def __init__(self):
        self.display = 'X'


class End:
    def __init__(self):
        self.display = 'Y'


class Air:
    def __init__(self):
        self.display = ' '


class Wall:
    def __init__(self):
        self.display = '*'


class Fire:
    def __init__(self):
        self.display = 'F'


class Water:
    def __init__(self):
        self.display = 'W'


class Teleport:
    def __init__(self, port_no):
        # require port_no to display
        self.display = port_no
