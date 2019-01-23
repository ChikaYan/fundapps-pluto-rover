from enum import Enum


class Rover:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def move(self, command):
        pass

    def location(self):
        return


class Dir(Enum):
    N = 1
    E = 2
    S = 3
    W = 4
