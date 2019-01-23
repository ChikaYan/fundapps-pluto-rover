from enum import IntEnum


class Dir(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


class PlutoMap:
    def __init__(self, x, y, obstacles=None):
        self.x = x
        self.y = y
        self.obs = obstacles

    def has_obs(self, x, y):
        if self.obs is None:
            return False
        return (x, y) in self.obs


class Rover:
    def __init__(self, x, y, dir, map=PlutoMap(100, 100)):
        self.x = x
        self.y = y
        self.dir = dir
        self.map = map

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
        self.__wrap_edge()

    def __backward(self):
        if self.dir == Dir.N:
            self.y -= 1
        elif self.dir == Dir.E:
            self.x -= 1
        elif self.dir == Dir.S:
            self.y += 1
        else:
            self.x += 1
        self.__wrap_edge()

    def __wrap_edge(self):
        self.x = self.x % (self.map.x + 1)
        self.y = self.y % (self.map.y + 1)

    def __turn_left(self):
        self.dir = Dir((int(self.dir) - 1) % 4)

    def __turn_right(self):
        self.dir = Dir((int(self.dir) + 1) % 4)

    def get_location(self):
        return [self.x, self.y, self.dir]
