from enum import Enum


class Dir(Enum):
    N = 1
    E = 2
    S = 3
    W = 4


class Rover:
    def __init__(self, x=0, y=0, dir=Dir.N):
        self.x = x
        self.y = y
        self.dir = dir

    def move(self, command):
        for c in command:
            if c == "F":
                self.__forward()

    def __forward(self):
        if self.dir == Dir.N:
            self.y += 1
        elif self.dir == Dir.E:
            pass
        elif self.dir == Dir.S:
            pass
        else:
            pass

    def location(self):
        return [self.x, self.y, self.dir]
