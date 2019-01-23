from enum import IntEnum


class Dir(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


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
            elif c == "L":
                self.__turn_left()
            elif c == "R":
                self.__turn_right()

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

    def __turn_left(self):
        self.dir = Dir((int(self.dir) - 1) % 4)

    def __turn_right(self):
        self.dir = Dir((int(self.dir) + 1) % 4)


    def location(self):
        return [self.x, self.y, self.dir]
