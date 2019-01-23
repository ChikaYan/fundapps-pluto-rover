from pluto_rover.pluto_rover import Rover
from pluto_rover.pluto_rover import Dir


def test_rover_can_move_n():
    rover = Rover(0, 0, Dir.N)
    rover.move("F")
    assert rover.location == [0, 1, Dir.N]
