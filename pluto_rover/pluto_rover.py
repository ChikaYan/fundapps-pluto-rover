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

    def run(self, command):
        for c in command:
            if c == "F":
                self.__forward()
            elif c == "B":
                self.__backward()

    def __forward(self):
        if self.dir == Dir.N:
            self.y += 1
        elif self.dir == Dir.E:
            self.x += 1
        elif self.dir == Dir.S:
            self.y -= 1
        else:
            self.x -= 1

    def __backward(self):
        if self.dir == Dir.N:
            self.y -= 1
        elif self.dir == Dir.E:
            self.x -= 1
        elif self.dir == Dir.S:
            self.y += 1
        else:
            self.x += 1

    def location(self):
        return [self.x, self.y, self.dir]
