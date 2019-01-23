import sys

sys.path.append("./../")
from pluto_rover.pluto_rover import Rover
from pluto_rover.pluto_rover import Dir


def test_rover_can_move_n():
    rover = Rover(0, 0, Dir.N)
    rover.run("F")
    assert rover.location() == [0, 1, Dir.N]


def test_can_move_at_all_dirs():
    rover = Rover(0, 0, Dir.N)
    rover.run("FFFB")
    assert rover.location() == [0, 2, Dir.N]

    rover = Rover(0, 0, Dir.E)
    rover.run("FFFB")
    assert rover.location() == [2, 0, Dir.E]

    rover = Rover(0, 0, Dir.S)
    rover.run("BBBF")
    assert rover.location() == [0, 2, Dir.S]

    rover = Rover(0, 0, Dir.W)
    rover.run("BBBF")
    assert rover.location() == [2, 0, Dir.W]


def test_can_turn_left_and_right():
    rover = Rover(0, 0, Dir.N)
    rover.run("L")
    assert rover.location() == [0, 0, Dir.W]

    rover.run("RR")
    assert rover.location() == [0, 0, Dir.E]

    rover.run("R")
    assert rover.location() == [0, 0, Dir.S]


def test_can_turn_360():
    rover = Rover(0, 0, Dir.N)
    rover.run("RRRR")
    assert rover.location() == [0, 0, Dir.N]
