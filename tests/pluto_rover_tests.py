import sys

sys.path.append("./../")
from pluto_rover.pluto_rover import Rover
from pluto_rover.pluto_rover import Dir


def test_rover_can_move_n():
    rover = Rover(0, 0, Dir.N)
    rover.move("F")
    assert rover.location() == [0, 1, Dir.N]


def test_can_move_at_all_dirs():
    rover = Rover(0, 0, Dir.N)
    rover.move("FFFB")
    assert rover.location() == [0, 2, Dir.N]

    rover = Rover(0, 0, Dir.E)
    rover.move("FFFB")
    assert rover.location() == [2, 0, Dir.E]

    rover = Rover(0, 0, Dir.S)
    rover.move("BBBF")
    assert rover.location() == [0, 2, Dir.S]

    rover = Rover(0, 0, Dir.W)
    rover.move("BBBF")
    assert rover.location() == [2, 0, Dir.W]
